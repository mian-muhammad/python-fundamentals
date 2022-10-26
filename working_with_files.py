try:
    # Open a file for reading
    my_file = open("my_file.txt")

    # Open a file for reading or writing
    # This will replace any existing file
    my_file = open("my_file.txt", "w")

    # Open a file for reading or writing
    # This will append to the end of any any existing file
    my_file = open("my_file.txt", "a")

    # Context Managers
    with open("my_file.txt") as my_file:
        contents = my_file.read()
    print("here: ", my_file)
except FileNotFoundError as error:
    print(f"Something went wrong. Message: {error}")
