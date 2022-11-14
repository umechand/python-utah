
# week6
#code along3

while True:
    file_name = input("Enter a fle name: ")
    try:
        fhandle = open(file_name, "a+")
        contents = fhandle.read()
        print(contents)


        while True:
            text = input("what do you want to write out? ")
            if text.lower() == "done":

              break

            fhandle.write(text + "\n")

    except Exception as ex:
        print(ex)
    else:
        break



