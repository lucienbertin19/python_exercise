'''
To design and implement a Python application that prints all
numbers between 1 and 100 with the square value in the allotted
time specified. 

• Create a Python application that will loop between 1 and 100

    for i in range(1, 101):
        print(i)

• The numbers are to be printed out alongside their squared value

     for i in range(1, 101):
        print(i + " " + i**)

• The app should stop when a squared value of 200 or more is reached

    if i**2 >= 200:
        break

• Reconfigure the application to take in a user value to produce
  squared values up to x
'''

# number to be inputed by user
numberInput = int(input("Please enter the number to be used\n"))

# loop through and check squared value is less than 200 else break
for i in range(1, numberInput + 1):
    if i**2 >= 200:
        break
    print("*****************  Number is {}  *****************".format(i))
    print("Number: {}\nSquare Value: {}\n".format(i, i**2))
