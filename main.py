__author__ = 'leigh'

from prettytable import PrettyTable

text_doc = 'Library.txt'


def read_text_file():
    """ Receives a text file, reads it, and "configures" the data into a dictionary

    Returns the Dictionary
    """
    with open(text_doc, 'r') as file:
        lines = [l.strip() for l in file.readlines()]

    return {lines[n*4].strip('title: '): tuple(lines[n*4:n*4+4]) for n in range(len(lines)//4)}

# a kickstarter you could say... (Default)
World_Dictionary = read_text_file()


def print_all_books():
    for key, value in World_Dictionary.items():

        value = list(value)
        print("{title}\n"
              "`| {author}\n"
              "`| {genre}\n"
              "`| {status}\n".format(title=key, author=value[1], genre=value[0], status=value[2]))


def print_book(title4):
    """ Prints a book in the format of:

    coiling dragon
    -| author: IET
    -| genre: action, adventure, romance, drama, light-novel
    -| status: -Reading
    """
    for key, value in World_Dictionary.items():
        if key == title4:
            value = list(value)
            print("{title}\n"
                  "-| {author}\n"
                  "-| {genre}\n"
                  "-| {status}\n".format(title=key, author=value[1], genre=value[0], status=value[2]))
    # show "book not found" if not found.


def remove_book(title3):
    """ Just as the title says
    """
    with open(text_doc, 'r') as file:
        # find the line number that the 'title' is on
        lines = file.readlines()
        for num, line in enumerate(lines):
            if title3 in line:
                lines = lines[:num] + lines[num+4:]
    with open(text_doc, 'w') as file:
        file.writelines(lines)


def change_book_info(title2, info_type2, info2):
    with open(text_doc, 'r') as file:
        # find the line number that the 'title' is on
        lines = file.readlines()
        for num, line in enumerate(lines):
            if title2 in line:
                if info_type2 == 'title':
                    lines[num] = 'title: ' + info2 + '\n'
                if info_type2 == 'genre':
                    lines[num+1] = 'genre: ' + info2 + '\n'
                if info_type2 == 'author':
                    lines[num+2] = 'author: ' + info2 + '\n'
                if info_type2 == 'status':
                    lines[num+3] = 'status: -' + info2 + '\n'

    with open(text_doc, 'w') as file:
        file.writelines(lines)


def add_book(title1, genre1, author1, status1):
    with open(text_doc, 'a') as file:

        file.write('title: ' + title1 + '\n')
        file.write('genre: ' + genre1 + '\n')
        file.write('author: ' + author1 + '\n')
        file.write('status: ' + status1)


if __name__ == '__main__':
    print("\nLeigh's Library Catalog.")
    print("To receive help, type: 'help()'\n")

    noQuit = True
    while noQuit:
        said = str(input("-| "))
        if said == "help()":
            help_table = PrettyTable(['Command', 'Description'])
            help_table.padding_width = 2

            # COMMANDS
            help_table.add_row(['^Show All Books', 'Shows all current books in catalog.'])
            help_table.add_row(['^Show Book', 'Shows the book inputed after typed.'])
            help_table.add_row(['^Remove Book', 'Removes the book inputed after typed by title.'])
            help_table.add_row(['^Change Book Info', 'Changes the inputed books info based on input.'])
            help_table.add_row(['^Add Book', 'Adds the inputed Book after typed.'])

            print("(^) at the start of the sentence issues a command.")
            print(help_table)

        elif said == "^Show All Books":
            print_all_books()

        elif said == "^Show Book":
            certain_book = str(input("Give Title to us | "))
            print_book(certain_book)

        elif said == "^Remove Book":
            certain_book = str(input("We shall remove the given book | "))

        elif said == "^Change Book Info":
            certain_book = str(input("Give us title of Book | "))
            info_type = str(input("What shall you change? | "))
            info = str(input("What should it be changed to? | "))

            change_book_info(certain_book, info_type, info)

        elif said == "^Add Book":
            title = str(input("The title | "))
            genre = str(input("The genres | "))
            author = str(input("The author | "))
            status = str(input("Current status | "))

            add_book(title, genre, author, status)

        elif said == "^Quit":
            noQuit = False

        else:
            print("Unknown Keyword.")
