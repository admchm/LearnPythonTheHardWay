import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
    
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)     # creating coded string 
    cooked_string = raw_bytes.decode(encoding, errors=errors) # recoding coded string. Could also just use print(next_lang)
    
    print(raw_bytes, "<===>", cooked_string)
    
languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)

#python3 -m pydoc io.IOBase.seek
#python3 -m pydoc str.strip
#python3 -m pydoc str.encode

#https://docs.python.org/3/library/stdtypes.html#bytes.decode

# calling the script:
#python3 ex22.py "utf-8" "strict"
#python3 ex22.py "utf-16" "ignore"
#python3 ex22.py "big5" "replace"