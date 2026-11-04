import random
import string

def generatepass(length):
    chars = string.ascii_letters + string.digits
    pwd = ""
    for i in range(length):
        pwd += random.choice(chars)
    return pwd

def main():
    length = int(input("Enter password length: "))
    password = generatepass(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()