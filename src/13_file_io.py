"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
f = open('src/foo.txt', 'r', encoding="utf-8")

contents = f.read()
print(contents)

f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
print("------")

f = open('src/bar.txt', 'w', encoding="utf-8")

f.write("Just writing some things here.\n")
f.write("I don't know if this works.\n") 
f.write("Hopfully it does.\n")

f.close()

f = open('src/bar.txt', 'r', encoding="utf-8")

contents = f.read()
print(contents)

f.close()