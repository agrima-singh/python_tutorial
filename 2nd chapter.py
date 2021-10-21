# String Concatenation
first_name="Agrima"
Last_name="Singh"
Full_name=first_name + " " + Last_name
print(Full_name)

#We can't add string and integer
#We can convert integer into string and then add
#We can multiply string and integer
print(first_name +"3")
print(first_name*3)

# User input by using input() function
name= input("Type your name : ")
print("Hello " + name)
# user input always takes default input as string
# if we want to take integer input then we have to use int() function
number_one= int(input("Enter the first number: "))
number_two= int(input("Enter the first number: "))
Total = number_one + number_two
print("Total " + str(Total))
# we can add int and float and output will be float

name, age = "Agrima" , 21
print("Hello " + name + " your age is " + str(age))


# take two inputs from user in one line
# by using .split()
name1, age1 = input("Enter your name and age").split(",")
#or
#name, age = input("Enter your name and age").split()
print(name1)
print(age1)
                
#String Formating: to shorten the code
Name= "Agrima"
Age="23"
print(f"Hello {name} your age is {age} ")


#String Indexing
# starts with 0
# spaces also get count
# we use square bracket [] in python indexing
name="Agrima"
print(name[3])
# Nagative Indexing
# if we want to find last index
print(name[-1])
# Slicing / sub sequences
# syntax [start_argument : stop_argument + 1]
print(name[1:3])
# if we won't give any of the argument (start or stop) it will automatically select the end
print (name [ :3]) # it will print from start to index 2
print (name [0: ]) # it will print from start to end


#Step argument
#if we want to jump / skip some values
print (name[0: :2])


#String Methods
#len() function : to find the length
print(len("Agrima Singh"))  #it will also count spaces
#lower() method : all charaters in lower
Name2= "Agrima Singh"
print(Name2.lower())
#upper() method : all charaters in capital
print(Name2.upper())
#title() method : Only first letter capital
print(Name2.title())
#count() method : it count the letter
print(Name2.count("a"))
      

#Strip Method : used to remove spaces
name= "     Agrima     "
dots= "........"
print(name + dots)
print(name.lstrip() + dots )
print(name.rstrip() + dots )
print(name.strip() + dots )


# Find and Replace Method
string = "she is beautiful and she is good dancer"
print(string.replace("is","was",2)) #it will replace both is with was
print(string.replace("is","was",1)) #it will replace only first is with was
print(string.find("is"))
print(string.find("is",7))  #it will give the position of second is


#Center Method
a="Agrima"
print(a.center(10, "$"))


#Strings are Immutable : means strings are unchnageable
# we can use replace method it will make another variable store it
strring= "String"
name_string= strring.replace("S","s")
print(name_string)


      
