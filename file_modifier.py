def modify_file_content(filename):
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()

        modified_content = content.upper()
        new_filename = f"modified_{filename}"

        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")


if __name__ == "__main__":
    user_file = input("Enter the name of the file to modify: ")
    modify_file_content(user_file)
