## Study Drill #1:
## This script is really annoying. There's no need to ask you before doing the copy, and it prints too much out to
## the screen. Try to make the script more friendly to use by removing features.

from_file = "test.txt"
to_file = "new_test.txt"

print(f"Copying from {from_file} to {to_file}.")

in_file = open(from_file)
indata = in_file.read()

print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print(f"Allright, all done for study drill #1.")

out_file.close()
in_file.close()