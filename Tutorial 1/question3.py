# define function for Q3
def q3():
    # initialize variables
    offenders = set()
    filename = 'blocklist.txt'
    blocklist = getBlocklist()  # retrieve blocked list

    # loop as long as true - infinite loop
    while True:
        # get user input and save to newoffender
        newoffender = input("Add new offenders(enter '.' to stop) ")

        # if user type '.' break out of loop
        if newoffender == ".":
            break
        # otherwise, add new newoffender to offenders
        else:
            # if newoffender does not exist in blocklist
            if newoffender not in blocklist:    # prevent redundant entries
                offenders.add(newoffender)
    print(offenders)

    # exception handler for i/o
    try:
        blockfile = open(filename, 'a')  # open file with append permission

        # iterate through each user in offenders set
        for user in offenders:
            # append each user into file
            blockfile.write(user + '\n')

    except FileNotFoundError:
        print(filename + ' does not exist.')

    # release resources
    blockfile.close()


def getBlocklist():
    # exception handler for i/o
    try:
        # read from file
        blocked_users = open('blocklist.txt', 'r')

        # convert into a unique list
        blocklist = list(set(blocked_users.read().split('\n')))

    # catch exception
    except FileNotFoundError as err:
        print(err)

    # close resources
    blocked_users.close()

    return blocklist


# execute function
q3()
