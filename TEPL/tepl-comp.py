import subprocess
import os
import shutil

def replace_multiple_patterns(content):
    replacements = [
        ("func", "def"),  # Replace 'func(' with 'def('
        (";", ","),         # Replace ';' with ','
        ("pri", "print"),# print with pri
        (".", ":"), # for func
        ("use", "import"), # to import
        ("back", "return"), # return = back
        ("destroy", "break"), # break = destroy
        ("printnt", "print") # fix nonsense error
    ]
    for old, new in replacements:
        content = content.replace(old, new)

    return content

def extract_error_line(error_message, original_content):
    return original_content

def compile_and_run(filename):
    # Create a backup of the original file
    backup_filename = filename + ".backup"
    shutil.copyfile(filename, backup_filename)

    # Read the original file
    with open(filename, 'r') as file:
        original_content = file.read()

    # Modify the content to replace multiple patterns
    modified_content = replace_multiple_patterns(original_content)

    # Write the modified content back to the file
    with open(filename, 'w') as file:
        file.write(modified_content)

    try:
        # Run the modified file
        result = subprocess.run(["python", filename], text=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        error_message = e.stderr
        error_line = extract_error_line(error_message, original_content)
        if error_line:
            print("Error: You did not define a string or variable:", error_line)
            print("Error message:", error_message)
    else:
        # Print the standard output if the process runs successfully
        print(result.stdout)

    # Revert changes by writing the original content back to the file
    with open(filename, 'w') as file:
        file.write(original_content)

    # Remove the backup file
    os.remove(backup_filename)

# Example usage
filename = input("FileName : ")
if filename == "":
   filename = "write.txt"
compile_and_run(filename)
