############ packages and library
import pickle

    # slno     id          pass      bank_name       location             balance last_withdraw  
data=["1","9938406590","suryasahoo","Axis Bank","kakatpur, puri, odisha","30000","10-1-2021"]
with open ("bank_data.dat","rb+") as file:
    x=pickle.load(file)
    print(x)
    

account_list={"9938406590":"suryasahoo"}


