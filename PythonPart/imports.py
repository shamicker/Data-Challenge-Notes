import test_script

print(4)


# for imports.py to read `num`, you need to tell it to look for the object!
print(test_script.num) # finds and runs it
print( type(test_script) )
# print(num) # produces an error!
# Need to comment out the above line in order to run anything that follows! :P


scores = [88, 92, 79, 93, 85]

mean = test_script.mean(scores)
curved = test_script.add_five(scores)

mean_c = test_script.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, " Curved Mean:", mean_c)

print("\n",__name__)
print(test_script.__name__)


# PRETEND THIS IS THE BEGINNING OF A NEW FILE:
import math

print(math.factorial(4))


# A module can have sub-modules. In this case, the module is called a Package.
# They are imported like this:
import os.path
