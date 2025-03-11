Name = "SanaUllah"
    #  0 1 2 3 4 5 6 7 8  a trick for finding negative slicing
    # -9-8-7-6-5-4-3-2-1        
nameshort = Name[0:3] #excluding character 0 index will be included but 3rd index exclude
print(nameshort)   
# nameslice = Name[-4:-1] #excluding character 0 index will be included but 3rd index exclude
# print(nameslice)
print(Name[1:4])
print(Name[-4:-1])
print(Name[5:8])
print(Name[:4]) # is same as print(name[0:4])
print(Name[1:])  # is same as print(name[1:5])
print(Name[1:5]) 

a = "abcdefghijklmnopqrstuvwxyz"
print(a[1:20:3])  # skip values with differ 3 and upto 20 characters starting from 1 character
print(a[:7])
print(a[10:])