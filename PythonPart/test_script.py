print('demo: ')
print(2 + 3)
num = 4 + 5


def mean(num_list):
    return sum(num_list) / len(num_list)

def add_five(num_list):
    return [n + 5 for n in num_list]



# Check this out!
# For anything, like tests, that you don't want to be exported, Python has a reserved __name__ function!

# This gets exported and printed out:
print("\nTesting mean function")
n_list = [34, 44, 23, 46, 12, 24]
correct_mean = 30.5
assert(mean(n_list) == correct_mean)

print("Testing add_five function:")
correct_list = [39, 49, 28, 51, 17, 29]
assert( add_five(n_list) == correct_list)

print("All tests passed!")
# To test this, run `python imports.py` on the command line
# Note that everything above is run AS WELL AS whatever code is in imports.py
# BUT nothing below this is printed out!


# However, if you write it in this __name__ function, it will only print **if you run THIS file!**
# It will not get exported at all.

if __name__ == '__main__': # meaning, if the file run is THIS file
    print("\nPRINT EVERYTHING AGAIN!")
    print("Testing mean function AGAIN")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing add_five function AGAIN:")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert( add_five(n_list) == correct_list)

    print("All tests passed AGAIN!")
# To test THIS, run `python test_script.py` in the command line. You'll see it printed out!

# The hidden stuff can also be written as follows:
def main():
    print("\nTHIRD TIME'S A CHARM!")
    print("Testing Times 3")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing Times 3:")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert( add_five(n_list) == correct_list)

    print("Triple play!")

if __name__ == '__main__':
    main()
