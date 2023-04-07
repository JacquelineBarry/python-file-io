import re

# Define the regular expression pattern to search for
pattern = r'\bheritab(?:il|le|ly|ility|lely|leness|les|listic)\b|\binherit(?:s|ed|able|ance|or|able|ibility|antly|ee|ing)\b'

if __name__ == "__main__":
    # Open the input file for reading and the output file for writing
    with open('origin.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
        # Iterate over each line in the input file
        for line_number, line in enumerate(input_file, start=1):
            # Search for the pattern in the line
            matches = re.findall(pattern, line)
            # If matches are found, write them to the output file
            if matches:
                for match in matches:
                    output_file.write(f'{line_number}\t{match}\n')
    with open('output.txt','r') as f:
        for text in f:
            print(text)
