# Try to open a file and handle FileNotFoundError

def open_file():
    filename = input("Enter file name: ")

    try:
        file = open(filename, "r")
        content = file.read()
        print("File content:")
        print(content)
    except FileNotFoundError:
        print("Error: File", filename, "not found.")
    finally:
    
        try:
            file.close()
        except:
            pass

if __name__ == "__main__":
    open_file()