print("ORIGNALLY THE TEXT FILE CONTAINS THIS: ")
# OPENED A FILE AND READ IT
file = open('buh.txt')
print(file.read())
file.close()

#OPENED THE FILE AGAIN IN WRITE MODE AND OVERWROTE IT
file = open('buh.txt','w')
file.write("Hello Antony Paula")
file.close()
print(" ")
print("NOW THE TEXT FILE CONTAINS THIS: ")

#OPENED THE FILE AGAIN IN READ MODE AND PRINTED IT
file = open('buh.txt','r')
print(file.read())
file.close()
print(" ")
print("NOW THE NEWLY OVERWROTE TEXT FILE GETS APPENDED AND BECOMES THIS: ")

#OPENEING THE FILE AGAIN IN APPEND MODE AND WRITING TEXT ON IT
file = open('buh.txt','a')
file.write("\n")
file.write("GEORGIA MARTIN")
file.close()

#OPENING IT AND THEN PRINTING THE APPENDED TEXT
file = open('buh.txt','r')
print(file.read())
file.close()
