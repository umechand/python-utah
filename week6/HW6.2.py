
# Exercise #2:

username = input("Enter a username: ")
password = input("Enter a password: ")

fn = open("security.txt", "w")
fn.write(username + "\n")
fn.write(password)
fn.close()
print("-------------")

