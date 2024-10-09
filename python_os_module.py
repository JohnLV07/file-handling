# Task 1: Disrectory Inspector:

'''
Problem Statement:
    Create a Python script that lists all files and subdirectories in a given directory.
    Your script should prompt the user for the directory path and then display the contents.


Expected Outcome:
    The script should correctly list all files and subdirectories in the specified directory.
    Handle exceptions for invalid paths or inaccessible directories.
    
     
'''

# Code Example:
# import os

# def list_directory_contents(path):
# # List and print all files and subdirectories in the given path




import os

def list_directory_contents(path):
    try:
        if not os.path.exists(path):
            print(f"The directory '{path}' does not exist.")
            return
        
        contents = os.listdir(path) # This should print the subdirectories
        
        if not contents:
            print(f"The directory '{path}' is empty.")
            return
        
        print(f"Contents of directory '{path}':")
        for item in contents:
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                print(f"[Directory] {item}")
            else:
                print(f"[File] {item}")
    
    except FileNotFoundError:
        print(f"The directory '{path}' was not found.")
    except PermissionError:
        print(f"You are not allowed to enter: '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:

        path = input("Enter the directory path (run it using your own desktop): ") # This should allow the user to select what subdirectory wants to open
           
        list_directory_contents(path)
        
        # if path == 'exit'.lower():
        #     break

        # else:
        #     print("Invalid input.")

if __name__ == "__main__":
    main()
