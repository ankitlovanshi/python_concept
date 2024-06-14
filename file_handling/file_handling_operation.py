# open the file
# f = open('example.txt', mode = 'r')
# print("file opened")


# # close file
# f.close()
# print("file closed")

# # read operation
# f = open('example.txt', mode = 'r')
# contain = f.read()
# print(contain)
# f.close()


# # write operation
# f = open('example.txt', mode = 'w')
# f.write("Hello ankit")
# f.close()

# # append operation
# f = open('example.txt', mode = 'a')
# f.write("Hello ankit")
# f.close()

'''with open('example.txt', 'r') as file:
    print(file.tell())
    file.read(5)
    print(file.tell())
    file.seek(0)
    print(file.tell())
'''


# read file using with
with open('example.txt', 'r') as file:
    contain = file.read()
    print(contain)


# read the file using with statement (by the path)
with open('/home/developer/Documents/temp.txt', 'r') as file:
    contain = file.read()
    print(contain)


# exception handling in the file handling
try:
    with open("example1.txt", 'r') as file:
        print(file.read())
    
except:
    print("file is not found")