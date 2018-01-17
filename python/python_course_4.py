'''def hours2days(hours):
    h2d=hours/24,hours%24
    days, hours = divmod(hours, 24)
    return days,hours
print hours2days(90005)

hours=input("Input number of hours you want to convert into days:")
print ("Converting "+hours+" hours to days... ")'''


'''def print_list(l, numbered=False, bullet_character='-'):
    """Prints a list on multiple lines, with numbers or bullets

    Arguments:
    l: The list to print
    numbered: set to True to print a numbered list
    bullet_character: The symbol placed before each list element. This is
                      ignored if numbered is True.
    """
    for index, element in enumerate(l):
        if numbered:
            print("{}: {}".format(index+1, element))
        else:
            print("{} {}".format(bullet_character, element))

print_list(["cats", "in", "space"],True)'''

'''k=[]
l='200,3,5,6,8,4,2,1'

k=l.split(',',1)
print(k[0])
'''
