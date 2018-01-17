"""top_3=(2,3,5,6,8,4,2,1)

def top_three(input_list):
    \"""Returns a list of the three largest elements input_list in order from largest to smallest.
    If input_list has fewer than three elements, return input_list element sorted largest to smallest
    \"""
    input_list=sorted(input_list, reverse=True)

    if len(input_list)>=3:
        input_list=input_list[:3]
    return input_list

def top_three(input_list):
    return sorted(input_list, reverse=True)[:3]

print (top_three(top_3))"""



"""def median(numbers):
#    import statistics
#    return statistics.median(numbers)

    numbers.sort() #The sort method sorts a list directly, rather than returning a new sorted list
    print (numbers)
    if len(numbers)%2!=0:
        m_ind = int(len(numbers)/2)
        med=numbers[m_ind]
        return med
    else:
        m_ind=len(numbers)//2
        mean=float((numbers[m_ind-1]+numbers[m_ind])/2.0)
        print (mean)
        return mean


test1 = median([1,2,3])
print("expected result: 2, actual result: {}".format(test1))

test2 = median([1,2,3,4])
print("expected result: 2.5, actual result: {}".format(test2))

test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))


def list_sum(input_list):
    sum = 0
    for element in input_list:
        sum += element
    return sum

def list_sum(input_list):
    sum = 0
    # todo: Write a for loop that adds the elements
    # of input_list to the sum variable
    for index in range(len(input_list)):
        sum=sum+input_list[index]
    return sum


def tag_count(tokens):
#The code counts number of XML tags
    count = 0
    for token in tokens:
        if token[0] == '<' and token[-1] == '>':
            count += 1
    return count

#Or other option
def tag_count(list2):
#The code counts number of XML tags
    i=0
    for element in list2:
        if element[0] == '<' and element[-1]=='>':
            i=i+1
    return i"""

#testing code
#count = tag_count(list1)
#print("Expected result: 2, Actual result: {}".format(count))

#define the  html_list function

"""def html_list(elements):
    string="<ul>\n"
    for element in elements:
       string+="<li>{}</li>\n".format(element)
    string+='</ul>'
    return string

names = ['charlotte hippopotamus turner', 3.0, 'nigel incubator-jones', 'philip diplodocus mallory']
string=html_list(names)
print (string)"""

'''
def nearest_square (limit):
    best=limit**0.5
    bot = (int(best))**2
    top = (int(best+1))**2
    if (top-limit)>(limit-bot):
            nrsq=bot
    elif (top-limit)<=(limit-bot):
            nrsq=top
#    else:
#            nrsq=str('Equally '+top+' and '+bot)
    return nrsq
test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))
'''

#Or the same with while steps:

'''
def nearest_square(limit):
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2
'''

'''def nt (headlines):
# TODO: set news_ticker to a string that contains no more than 140 characters long.
    length=0
    nhl = ""
#Set a string with headlines that contains no more than 140 characters long.
    for headline in headlines:
        nhl+="{}".format(headline)
    while len(nhl)>140:
        nhl=nhl[:-1] #short string by one last letter
    return nhl
print (nt(headlines))

headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]
print (len(nt(headlines)))'''


'''
def check_answers(given_ans,correct_ans):
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    given_ans are answers received from user
    correct_ans are correct answers
    """
    results= [False]*len(correct_ans)
#This checks answers and accumulate correct answers:
    for i,given_an in enumerate(given_ans):
        if given_an  == correct_ans[i]:
            results[i] = True

#This provides the success rate of a quiz:
    total=sum(results)
    if total/len(results) > 0.7:
        print ("Congratulations, you passed the test! You scored " + str(total) + " out of "+str(len(results))+".")
    else:
        print ("Unfortunately, you did not pass. You scored " + str(total) + " out of "+str(len(results))+".")

check_answers ([1,2,4,5,6],[1,2,3,5,7])
check_answers([1,2,3,4,5],[1,2,3,4,5])
check_answers ([1,2,4,5,6,8],[1,2,4,5,7,8])
check_answers([1,2,3,4,5],["badger","badger","badger","badger","badger"])'''



'''def remove_duplicates (elements):
# Define the remove_duplicates function
    target=[]
     for element in elements:
      if element is not in target:
          target.append(element)
    return target
print (remove_duplicates(target))'''

"""
def nearest_square(limit):
#populate "squares" with the set of all of the integers less than 2000 that are square numbers
    squares = set()
    i = 1
    while i**2 < limit:
        squares.add(i**2)
        i+=1
    return squares
print (nearest_square(200))"""

population = {'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}
print (population['Mumbai'],population['Karachi'])
#if 'Karachi' in population:
print ('Population includes ', population['Karachi'])
