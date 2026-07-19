def main():
    try:
        fobj = open("Demo.txt", "r")
        print ("Files get opened")

        Rows = fobj.readlines()
        print ("Number of lines in Demo file", len(Rows))

        words = fobj.read()
        text = words.split()
        print ("Number of words in file", len(text))

    except:
         print ("File is not present in current directory")    
    

if __name__ == "__main__":
    main()