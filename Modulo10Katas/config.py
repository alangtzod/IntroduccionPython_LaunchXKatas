def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError: # Tipo de Exception 1
        print("Couldn't find the config.txt file!")
    except IsADirectoryError: # Tipo de Exception 2
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError): # Tipo de Exception 3
        print("Filesystem under heavy load, can't complete reading configuration file")

if __name__ == '__main__':
    main()