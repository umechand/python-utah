
#Exercise #7:

f_names = []

while(1):
    name = input("Enter your first name: ")
    if name not in f_names:
        f_names.append(name)
    else:
        print("Duplicate names are  not allowed")
    if name.lower() == "end":
        break

print(f_names)
