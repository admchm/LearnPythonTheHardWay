## Study Drill #2:
## See how short you can make the script. I could make this one line long.

in_file = open("test.txt")
input("Ready, hit RETURN to continue, CTRL-C to abort:")

out_file = open("new_test.txt", 'w')
out_file.write(in_file.read())

out_file.close(), in_file.close()

# My comment:
# I could make it shorter. However, I wanted this code to remain readable.