def add_word(word, dictionary):
        if word in dictionary.keys():
            dictionary[word] = dictionary[word] + 1
        else:
            dictionary[word] = 1

def process_line(line, dictionary):
        for word in line.split():
            add_word(word, dictionary)

def pretty_print (dictionary):


def main():
        gba_file = open('gettysburg.txt', 'r')
        for line in gba_file:
            print("Hello")
            pretty_print(dictionary)
