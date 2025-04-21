# Task 1
try:
    file_1 = open("Sample.txt","r")
    file_read = file_1.readlines()
    file_1.close()

    file_1 = open("Sample.txt","w")
    file_1.write("This is a sample text file.\nThis contains multiple lines.")
    file_1.close()

    file_1 = open("Sample.txt","r")
    file_read = file_1.readlines()
    ln=1
    for line in file_read:
        # print(f"line {ln}:{line}")
        print("line "+str(ln)+":"+line,end="")
        ln+=1
    file_1.close()
except FileNotFoundError:
    print("Error:The file 'Sample.txt' was not found")

#Task2
try:
    file_name  = "output.txt"
    file_1 = open(file_name,"w")
    file_1.write(input("\n\nEnter text to write to the file: "))
    file_1.close()
    print(f"Data successfully written to {file_name}.")
    file_1 = open(file_name, "a")
    file_1.write("\n"+input("Enter additional text to append: "))
    file_1.close()
    print(f"Data successfully appended\n")

    file_1 = open(file_name,"r")
    print(f"Final content of {file_name}:")
    for ln in file_1.readlines():
        print(ln,end="")
    file_1.close()
except FileNotFoundError:
    print(f"Error:The file {file_name} was not found")