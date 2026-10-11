import os

while True:
    cmd=input("-> ")
    if cmd in ["n","N"]:
        break
    else:
        try:
            os.system(cmd)
        except:
            print("Invalid input")