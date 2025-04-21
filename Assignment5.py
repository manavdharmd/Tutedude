#Task1
My_Dict = {'A':80,'B':90,'Alice':85}
print(My_Dict.get(input("Enter the student's name: "),"Student not found"))


# Task2
list_1 = list(range(1,11))
print("\nOriginal List: ",list_1)
f_five = list_1[:5]
print("Extracted first five element: ",f_five)
print("Extracted last five element: ",f_five[::-1])