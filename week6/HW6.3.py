
#Exercise 3:


try:
    myfile = open('security.txt', 'r')
    contents_file = myfile.read()
    line = contents_file.strip().split("\n")
    username = line[0]
    password = line[1]
    username_value = input("Enter a username: ")
    password_value = input("Enter a password: ")
    if (username_value == username) and (password_value == password):
        print("Logged in Successfully!")
        myfile.close()
    else:
        print("Username/Password entered do not match values stored in file!")

except Exception as excep:
    print(f"Error: {excep}")


