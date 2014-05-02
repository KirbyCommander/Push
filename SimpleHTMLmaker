#providing name for the file to be created
filename = raw_input("Give name for the file: ")
#This will create the file in the same location you run this file out of.
file = open (filename, 'a') ## a will append, w will over-write 
#Providing the content for the file

body = raw_input("What would you like in your body paragraph?:  ")
title = raw_input("What would you like as your title ")

#Writing the title and body to the file we just created
print "enter the desired information to be added to the file"
file.write('<!DOCTYPE html>')
file.write('<html>')
file.write('\n<head>')
file.write('\n<title>')
file.write(title)
file.write('</title>')
file.write('\n</head>')
file.write('\n<body>')
file.write('\n<p>')
file.write(body)
file.write('\n</p>')
file.write('</body>')
file.write('</html>')

#Providing information that writing task is completed
print "The text pieces have been added to the file"
file.close()
