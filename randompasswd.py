import secrets
import string

print("*" * 50) 
print("Welcome to the password generator\n ")
print("*" * 50)
pass_lenght = int(input("Please enter the password length: Please choose betwwen 12 and 20: "))

if pass_lenght < 12 or pass_lenght > 20:
    print("Please choose between 12 and 20")
else:
    print("*" * 50)
    password = "".join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(pass_lenght))
    password1 = "".join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(pass_lenght))
    password2 = "".join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(pass_lenght))
    print(f"1): {password}\n2): {password1}\n3): {password2}")
    print("*" * 50)          
