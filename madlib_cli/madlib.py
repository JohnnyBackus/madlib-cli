user_input = []
madlib = ''

print('''
      Welcome to Madlib Game!
      I will prompt you for some words, which I will use to complete a story. Type the words and then press enter.
      ''')

def game_start():
    first_adjective = input('Enter an adjective: ')
    second_adjective = input('Enter another adjective: ')
    first_noun = input('Enter a noun: ')
    user_input.append(first_adjective, second_adjective, first_noun)

def read_template(file_path):
    global madlib
    try:
        with open(file_path, 'r') as file:
            madlib = file.read().strip()
            print("madlib: ", madlib)
            return madlib
    except FileNotFoundError:
        raise FileNotFoundError("Invalid file path.")

read_template('assets/dark_and_stormy_night_template.txt')

def parse_template(template):
    language_parts_tuple = []
    parsed_string = ""
    words = template.split()

    for word in words:
        if word.endswith("}"):
            language_parts_tuple.append(word[1:-1])
            parsed_string += "{} "
            print(word[1:-1])
        elif word.endswith("}."):
            language_parts_tuple.append(word[1:-2])
            parsed_string += "{}."
            print(word[1:-2])
        else:
            parsed_string += word + " "
            print(word)
    parsed_string = parsed_string.strip()
    print("parsed string: ", parsed_string, tuple(language_parts_tuple))
    return parsed_string, tuple(language_parts_tuple)

parse_template(madlib)