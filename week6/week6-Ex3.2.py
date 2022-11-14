

#2 File IO
while True:
    filename = input ("Enter a file name:")
    try:
        filehandle = open(filename, "r+")
        txt = filehandle.read()
        print(txt)


        while True:
            txt = input("Enter your context: ")
            if txt.lower() == "done":
                break


            filehandle.write(txt + "\n")
            filehandle.close()
    except Exception as excep:
        print(excep)
    else:
        break

