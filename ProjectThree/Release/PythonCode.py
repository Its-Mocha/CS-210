import re
import string

frequencies = {}

def CreatFrequencyFile():
    in_file_name = "CS210_Project_Three_Input_File.txt"
    out_file_name = "frequency.dat"

    frequencies = {}

    with open(in_file_name, "r") as f:
        for item in f.read().splitlines():
            frequencies[item] = frequencies.get(item, 0) + 1

    with open(out_file_name, "w") as f:
        for item, frequency in frequencies.items():
            print("{} {}".format(item, frequency), file=f)
    

def DisplayItemFrequency():
    in_file_name = "CS210_Project_Three_Input_File.txt"
    #print("Start reading the file")
    
    with open(in_file_name, "r") as f:
        for item in f.read().splitlines():
            frequencies[item] = frequencies.get(item, 0) + 1

    for item, frequency in frequencies.items():
        print("{} {}".format(item, frequency))
       # print("End of function")
       
def LookUp(itemm):
    in_file_name = "CS210_Project_Three_Input_File.txt"
    #print("Start reading the file")
    
    with open(in_file_name, "r") as f:
        for item in f.read().splitlines():
            frequencies[item] = frequencies.get(item, 0) + 1
 
    return frequencies.get(itemm, 0)

def DisplayHistogram():
    in_file_name = "CS210_Project_Three_Input_File.txt" 
    
    with open(in_file_name, "r") as f:
        for item in f.read().splitlines():
            frequencies[item] = frequencies.get(item, 0) + 1

    for item, frequency in frequencies.items():
        print (item + " " , end = "") 
        for n in range (frequency):
            print ("*" , end = "")
        print ()
      
       # print("End of function")