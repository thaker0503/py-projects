#Creating a python program to generate strong passwords

print(" \n")
print("Auto Password Generator \n")
print("Created by Yatharth Thaker \n")
import random #Here we have imported random library, to generate random entity from a string

#Defining variable for lower case alphabets data set and storing a string with all the alphabets in small in it. 
lower_case = "abcdefghijklmnopqrstuvwxyz" 

#Defining variable for upper case alphabets data set and storing a string with all the alphabets in capital in it. 
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Defining variable for numbers data set and storing a string with all the numbers in it. 
number = "0123456789"

#Defining variable for symbolss data set and storing a string with all the possible symbols in it. 
symbols = "@!#$&*?\/"

#Here we have created a variable password which stores all the data sets we created earlier.
password = lower_case + upper_case + number + symbols

#pass_len defines the length of the password you want to generate.
pass_len = 8

#gen_pass is the variable where we will store the generated password.
#here we have used random module's sample variable .
#Sample variable chooses k unique random elements from a population sequence or set.
#here password is our set of data and pass_len variable is the unique number of random elements that are to generted.
gen_pass = "".join(random.sample(password,pass_len))

#Printing the genrated password in terminal.
print("Your Password is:",gen_pass)
print(" \n")