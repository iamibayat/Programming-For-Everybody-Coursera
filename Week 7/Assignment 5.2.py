'''
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers.
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and
ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
'''



flag = True

while True:
    var = input("Enter a number: ")
    if var == "done":
        break
    try:
        int_var = int(var)
    except:
        print("Invalid input")

    if flag == True:
        lar = int_var
        smal = int_var
        flag = False


    if int_var > lar:
        lar = int_var
    if int_var < smal:
        smal = int_var

print("Maximum is", lar)
print("Minimum is", smal)
