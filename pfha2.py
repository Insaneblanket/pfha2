file_read = open('pfha1.txt','r')
print("File in read mode -")
print(file_read.read())
file_read.close()



file_write = open('pfha1.txt','w')

file_write.write("File in writing mode ...")
file_write.write("Hi! I am a student.")
file_write.close()



file_append = open('pfha1.txt','a')

file_append.write("\n File in append mode...")
file_append.write("This is append mode")
file_append.close()
