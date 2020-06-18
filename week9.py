# Hedyeh Erfani
# Week 9
# Purpose: Modification of week 8 to generate text file from output rather than print to screen

def add_word(w, d):
    # if we've seen the word already, increment it
    if w in d:
        d[w] += 1
    # otherwise set it to 1
    else:
        d[w] = 1


# Removes unnecessary fillers
def process_line(l, d):
    for w in l.split():
        add_word(w.strip(",.;:!-").lower(), d)


def pretty_print(d):
    # get rid of blank in dictionary
    del d['']
    print("Length of the dictionary:", len(d))
    print("Word\t\tCount")
    print()
    print("-" * 25)
    for w in sorted(d, key=d.get, reverse=True):
        print(f"{w:12}           {d[w]}")

# Prints to file instead of to the screen
def process_file(d, f):
    # get rid of blank in dictionary
    del d['']
    with open(f, 'w') as output_file:
        output_file.write("Length of the dictionary: " + str(len(d)) + "\n")
        output_file.write("Word\t\tCount\n")
        output_file.write("")
        output_file.write("-" * 25 + "\n")
        for w in sorted(d, key=d.get, reverse=True):
            output_file.write(f"{w:12}           {d[w]}\n")


# Opens the file and prints length of dictionary to the file 
def main():
    d = {}
    filename = input("Enter a filename: ")
    with open('gettysburg.txt', 'r') as f:
        for l in f:
            process_line(l, d)
    with open(filename, 'a+') as fobj:
        fobj.write("Length of dictionary: " + str(len(d.keys())) + "\n")
        fobj.close()
        process_file(d, filename)


if __name__ == "__main__":
    main()
