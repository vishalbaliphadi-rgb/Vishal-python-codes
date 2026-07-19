def main():
    try:
        word = input("Enter word to search from file:")
        source_file = open ("ABC.txt", "r")
        content = source_file.read()

        if word in content:
            print ("Word is present in file")
        else:
            print ("Word is not present in file")

    except:
        print ("File is not present in current directory") 


if __name__ == "__main__":
    main()

