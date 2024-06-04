## Study Drill #4: 
## Research online what the seek function for file does. Try pydoc file, and see if you can figure it out from there. Then try pydoc file.seek to see what seek does.

# Answer:
# for this exercise, use: python3 -m pydoc io.IOBase.seek
# call from terminal for reading documentation: python3 -m pydoc -b

# Help on method_descriptor in io.IOBase:

# io.IOBase.seek = seek(self, offset, whence=0, /)
#     Change the stream position to the given byte offset.
    
#       offset
#         The stream position, relative to 'whence'.
#       whence
#         The relative position to seek from.
    
#     The offset is interpreted relative to the position indicated by whence.
#     Values for whence are:
    
#     * os.SEEK_SET or 0 -- start of stream (the default); offset should be zero or positive
#     * os.SEEK_CUR or 1 -- current stream position; offset may be negative
#     * os.SEEK_END or 2 -- end of stream; offset is usually negative
    
#     Return the new absolute position.