# define function for Q1
def q1():
    # exception handler for i/o
    try:
        # read from file
        blocked_users = open('blocklist.txt', 'r')

        print("Blocked user:")
        # convert into a unique list
        blocklist = list(set(blocked_users.readlines()))

        # iterate each line as an element from block list
        for user in blocklist:
            print(user)

    # catch exception
    except FileNotFoundError as err:
        print(err)

    # close resources
    blocked_users.close()


# execute function
q1()

