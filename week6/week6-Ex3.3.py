
#3 Name

filename = input("Enter file name: ")

try :
    fn = open(filename)

except:
    print('Cannot open the file ',filename ,'please try again')
    quit()

for line in fn:
    line = line.upper()
    line = line.rstrip()
    print(line)

