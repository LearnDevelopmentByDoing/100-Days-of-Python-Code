file_path = 'sample.txt'  # Replace with the path to your text file

with open(file_path, 'r') as file:
    text = file.read()
    word_count = len(text.split())
    print(f"Number of words in the file: {word_count}")
