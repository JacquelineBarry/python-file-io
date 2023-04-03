#!/usr/bin/env python


import re
if __name__ == "__main__":
    print('Opening origin.txt')
    with open('origin.txt', 'r') as in_stream:
        print('Opening output.txt')
        with open('output.txt', 'w') as out_stream:
            for idx, line in enumerate(in_stream):
                if re.search(r"herit|HERIT", line):
                    for word in re.split(r'\s|--',line):
                        if re.search(r"herit|HERIT", word):
                            filtered_word = re.sub(r'[^a-zA-Z]', '', word)
                            out_stream.write(f"{idx+1}  \t{filtered_word}\n")
			    ## Will print an output.txt file with filtered occurrence data ##				

    print("Done!")
    print('origin.txt is closed?', in_stream.closed)
    print('output.txt is closed?', out_stream.closed)
