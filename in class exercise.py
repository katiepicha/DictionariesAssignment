# This program writes three lines of data to a file. 
def main(): 
# Open a file named philosophers.txt. 
    outfile = open("philosophers.txt", 'w')

# Write the names of three philosphers to the file – 
# John Locke, David Hume and Edmund Burke
    outfile.write('John Locke' + '\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke')

# Close the file.
    outfile.close()

# Call the main function.
main()


# add your name to the bottom of the list (append)
def main1():

    outfile = open("philosophers.txt", 'a')

    outfile.write('\nKatie Picha')

    outfile.close()

main1()


# reading from the philosophers file

def main2():

    infile = open("philosophers.txt", 'r')

    # read the file's contents
    file_contents = infile.read()

    line1 = infile.readline().rstrip('\n')
    line2 = infile.readline()
    line3 = infile.readline()

    print(line1)
    print(line2.rstrip('\n'))
    print(line3)


main2()