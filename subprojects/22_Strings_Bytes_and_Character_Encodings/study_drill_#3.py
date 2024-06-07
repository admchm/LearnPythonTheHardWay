## Study Drill #3: 
## Can you break the encodings by damaging the file? How much do you need to remove to cause Python to break? How 
## much can you remove to damage the string output, but pass Python's decoding system?

# Answer: To corrupt the file, we could open languages.txt in a binary editor (or use a programming 
# tool to manipulate it programmatically). Next, change or delete some bytes in the middle of 
# a multi-byte character. For instance, in UTF-8, characters outside the basic ASCII set are encoded
# using multiple bytes (2-4 bytes). Altering one of these bytes can make the sequence invalid.