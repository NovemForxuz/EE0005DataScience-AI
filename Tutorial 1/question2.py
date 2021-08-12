# define function for Q2
def q2():
    # exception handler for i/o
    try:
        # read from file
        visitors_users = open('visitors.txt', 'r')

        visitorlist = visitors_users.read().split('\n')

        # iterate each user from list of visitors
        count = len(visitorlist)

        # iterate each user from list of visitors
        denied_access = [user for user in visitorlist if user in getBlocklist()]

        # print the no. of visitors online
        print("Visitors online: " + str(count))

        # print users that was denied access
        print("Denied access: ")
        for user in denied_access:
            print(user)

    # catch exception 
    except FileNotFoundError as err:
        print(err)

    # close resources
    visitors_users.close()


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
q2()
