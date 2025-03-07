import os

def list_directories_files(path):
    print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    print("All:", os.listdir(path))

def check_path_access(path):
    print(f"Exists: {os.path.exists(path)}")
    print(f"Readable: {os.access(path, os.R_OK)}")
    print(f"Writable: {os.access(path, os.W_OK)}")
    print(f"Executable: {os.access(path, os.X_OK)}")

def check_path_info(path):
    if os.path.exists(path):
        print(f"Filename: {os.path.basename(path)}")
        print(f"Directory: {os.path.dirname(path)}")
    else:
        print("Path does not exist")

def count_lines_in_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            print("Number of lines:", sum(1 for _ in f))
    else:
        print(f"Error: {file_path} does not exist.")

def write_list_to_file(file_path, data_list):
    with open(file_path, 'w') as f:
        f.writelines("\n".join(data_list))

def generate_alphabet_files():
    for letter in range(65, 91):  
        with open(f"{chr(letter)}.txt", 'w') as f:
            f.write(f"This is file {chr(letter)}.txt")

def copy_file(source, destination):
    if os.path.exists(source):
        with open(source, 'rb') as src, open(destination, 'wb') as dest:
            dest.write(src.read())
        print(f"Copied {source} to {destination}")
    else:
        print(f"Error: {source} does not exist.")

def delete_file(file_path):
    if os.path.exists(file_path) and os.access(file_path, os.W_OK):
        os.remove(file_path)
        print("File deleted successfully")
    else:
        print("File cannot be deleted or does not exist")

with open("example.txt", "a") as f:
    f.write("""Hello, this is a test file.
It contains multiple lines.
Let's check how many lines are in this file.
Python is great for file handling.
This is the last line.
""")

with open("source.txt", "w") as f:
    f.write("This is a test file for copying.")

list_directories_files(".")
check_path_access("example.txt")
check_path_info("example.txt")
count_lines_in_file("example.txt")
write_list_to_file("output.txt", ["Line 1", "Line 2", "Line 3"])
generate_alphabet_files()
copy_file("source.txt", "destination.txt")
delete_file("example.txt")