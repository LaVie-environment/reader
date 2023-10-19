import sys

class CatCommand:
    def __init__(self):
        pass

    def cat_files(self, file_paths):
        for file_path in file_paths:
            try:
                with open(file_path, 'r') as file:
                    content = file.readlines()
                    print(f"Content of {file_path}:\n{content}")
            except FileNotFoundError:
                print(f"Error: File '{file_path}' not found.")
            except Exception as e:
                print(f"Error reading file '{file_path}': {e}")

if __name__ == "__main__":
    cat_command = CatCommand()

    # Check if file paths are provided as command-line arguments
    if len(sys.argv) >= 1:
        files_to_cat = sys.argv[1:]
        cat_command.cat_files(files_to_cat)
    else:
        print("Usage: python tac.py [file1] [file2] ...")
