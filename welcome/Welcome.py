import os 
class Welcome:
    def __init__(self):
        pass

    def Configure(self, filename):
        word = input("Enter a sentence: ")
        fail = True
        for root, dirs, files in os.walk("C:\\Users\\tenth\\OneDrive\\Desktop\\"):
            if filename in files:
                print("File Found")
                file1 = open(filename, "a")
                file1.write(word)
                file1.flush()
                file1.close()
                print(word + " added to " + filename)
                fail = False
        if fail:
            print("File Not Found")

    def Print_welcome_message(self, filename):
        fail = True
        for root, dirs, files in os.walk("C:\\Users\\tenth\\OneDrive\\Desktop\\"):
            if filename in files:
                print("File Found")
                file1 = open(filename, "r")
                x = file1.read()
                print(x)
                file1.close()
                fail = False 
        if fail:
            print("File Not Found")

newWel = Welcome()
newWel.Configure("test.txt")
newWel.Print_welcome_message("test.txt")

