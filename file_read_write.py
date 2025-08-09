try:
    input_filename = input("Enter the input filename (e.g., input.txt): ")

   
    with open(input_filename, 'r') as file:
        text = file.read()

    
    modified_text = text.upper()

   
    words = text.split()
    word_count = len(words)

   
    with open('output.txt', 'w') as file:
        file.write(modified_text)
        file.write(f"\nWord count: {word_count}\n")

    print(f"Successfully read {input_filename}, converted to uppercase, and wrote to output.txt with word count.")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found. Please check the filename and try again.")
except PermissionError:
    print(f"Error: Permission denied when accessing '{input_filename}' or writing to 'output.txt'. Check file permissions.")
except IOError as e:
    print(f"Error: An I/O error occurred: {e}")
except Exception as e:
    print(f"Unexpected error occurred: {e}")