def main():
    try:
        source_file = open ("ABC.txt", "r")
        content = source_file.read()

        dest_file = open ("Demo.txt", "w")
        dest_file.write(content)

        source_file.close()
        dest_file.close()
    except FileNotFoundError as source_file:
        print ("File not found")


if __name__ =="__main__":
    main()
    