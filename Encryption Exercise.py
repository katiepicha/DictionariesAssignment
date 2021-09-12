codes = {'A' : '!', 'a' : '1', 'B' : '@', 'b' : '2', 'C' : '#', 'c' : '3', 'D' : '$', 'd' : '4', 'E' : '%', 'e' : '5',
'F' : '^', 'f' : '6', 'G' : '&', 'g' : '7', 'H' : '*', 'h' : '8', 'I' : '(', 'i' : '9', 'J' : ')', 'j' : '0', 'K' : '_',
'k' : '-', 'L' : '<', 'l' : ',', 'M' : '>', 'm' : '.', 'N' : '?', 'n' : '/', 'O' : '+', 'o' : '=', 'P' : '{', 'p' : '[',
'Q' : '}', 'q' : ']', 'R' : '|', 'r' : '~', 'S' : '00', 's' : '01', 'T' : '[]', 't' : '+=', 'U' : '()', 'u' : '<>',
'V' : '*!', 'v' : '??', 'W' : '01', 'w' : '@$', 'X' : '\/', 'x' : '#%', 'Y' : '^>', 'y' : '&$', 'Z' : '02', 'z' : '99',
' ' : '%&', '.' : ':', ':' : '++'}

def main():
    
    security_file = open("info_security.txt", 'r')
    input_file = security_file.read()
    security_file.close

    outfile = open("encrypted_file.txt", 'w')

    for character in input_file:
      outfile.write(codes[character])


    outfile.close

main()
