
print('''
      Welcome to Madlib Game!
      I will prompt you for some words, which I will use to complete a story. Type the words and then press enter.
      ''')

def read_template(file_path):
    with open(file_path, 'r') as file:
        return file.read()

