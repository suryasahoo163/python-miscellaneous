import socket
import selectors
import threading

# Server Code
def accept_wrapper(sock, sel):
    conn, addr = sock.accept()  # Should be ready to read
    print(f"Accepted connection from {addr}")
    conn.setblocking(False)
    data = {"addr": addr, "inb": b"", "outb": b""}
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)

def service_connection(key, mask, sel):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data["outb"] += recv_data
            print(f"Received {recv_data!r} from {data['addr']}")
        else:
            print(f"Closing connection to {data['addr']}")
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data["outb"]:
            sent = sock.send(data["outb"])  # Should be ready to write
            data["outb"] = data["outb"][sent:]

def server(host, port):
    sel = selectors.DefaultSelector()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Allow reuse of address
    sock.bind((host, port))
    sock.listen()
    print(f"Listening on {(host, port)}")
    sock.setblocking(False)
    sel.register(sock, selectors.EVENT_READ, data=None)

    try:
        while True:
            events = sel.select(timeout=None)
            for key, mask in events:
                if key.data is None:
                    accept_wrapper(key.fileobj, sel)
                else:
                    service_connection(key, mask, sel)
    except KeyboardInterrupt:
        print("Caught keyboard interrupt, exiting")
    finally:
        sel.close()

# Client Code
def client(host, port, messages):
    sel = selectors.DefaultSelector()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    try:
        sock.connect_ex((host, port))
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = {"messages": messages, "outb": b"", "inb": b"", "sent": 0}
        sel.register(sock, events, data=data)

        while True:
            events = sel.select(timeout=1) #small timeout for responsiveness
            for key, mask in events:
                service_client_connection(key, mask, sel)
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        sel.close()
        sock.close()

def service_client_connection(key, mask, sel):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            print(f"Client received {recv_data!r}")
            data["inb"] += recv_data
        else:
            print("Closing client connection")
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if not data["outb"] and data["sent"] < len(data["messages"]):
            message = data["messages"][data["sent"]].encode("utf-8")
            data["outb"] += message
            data["sent"] += 1
        if data["outb"]:
            sent = sock.send(data["outb"])
            data["outb"] = data["outb"][sent:]

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 65432
    messages = ["Hello, server!", "How are you?", "Goodbye!"]

    # Start server in a separate thread
    server_thread = threading.Thread(target=server, args=(host, port))
    server_thread.daemon = True #close server thread when main thread closes.
    server_thread.start()

    # Start client
    client(host, port, messages)