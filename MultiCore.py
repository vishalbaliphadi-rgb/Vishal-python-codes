import os

print ("current process id:", os.getpid())

def main():
    print ("Number of cores are:", os.cpu_count())

if __name__ == "__main__":
    main()