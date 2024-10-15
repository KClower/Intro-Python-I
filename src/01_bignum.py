# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

# YOUR CODE HERE
import sys
sys.set_int_max_str_digits(100000)

result = 2 ** 65536
first_12_digits = str(result)[:12]
print(first_12_digits)