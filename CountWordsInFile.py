def main():
    try:
        file1 = open ("Demo.txt", "r")
        content = file1.read()
        word_count = content.split()
        print ("Number of words in file:" , len(word_count))

    except FileNotFoundError as file1:
        print ("File is not present")

if __name__ == "__main__":
    main()