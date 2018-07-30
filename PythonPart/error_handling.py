# while True:
#     try:
#         x = int(input('Enter a number: '))
#         break
#     except:
#         print("\nThat's not a valid number!")
#     else:
#         print('\nNo problems!')
#         # This should be printing if no exceptions, but it isn't!
#     finally:
#         print('\nExtra input\n')

# Above commented out to work on the following puzzle.

def party_planner(cookies, people):
    leftovers = None
    num_each = None
    try:
        num_each = cookies // people
        leftovers = cookies % people
    except Exception as e:
        print("Exception occurred: {}".format(e))
        print("It isn't a party without people! ")
    return(num_each, leftovers)

# The main code block is below; do not edit this
lets_party = 'y'
while lets_party == 'y':

    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    lets_party = input("\nWould you like to party more? (y or n) ")
