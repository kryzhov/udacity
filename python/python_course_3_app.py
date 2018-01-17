from countries import country_list

# Note: since the list is so large, it's tidier
# to put in in a separate file. We'll learn more
# about "import" later on.

'''country_counts = {}
for item in country_list:
    #todo: insert countries into the country_count dict.
    # If the country isn't in the dict already, add it and set the value to 1
    # If the country is in the dict, increment its value by one to keep count
    if item in country_counts:
        country_counts[item]+=1
    else:
        country_counts.update({item:1})

print (country_counts)


#Or otherwise
for country in countries:
    if country in country_counts:
        country_counts[country] += 1
    else:
        country_counts[country] = 1'''

Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963,
                       "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
                       "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
                       "Sgt. Pepper's Lonely Hearts Club Band": 1967,
                       "Magical Mystery Tour": 1967, "The Beatles": 1968,
                       "Yellow Submarine": 1969, 'Abbey Road': 1969,
                       "Let It Be": 1969}

'''def most_prolific (disc):
#defines most prolific (year-repetition) year based on discography
#k=list(prolific.keys())
#v=list(disc.values())

    prolific={1967:0,1968:0}
    for item in disc:
        if disc[item] in prolific:
            prolific[disc[item]]+=1
        else:
            prolific[disc[item]]=1
    print(prolific)

    m=max(prolific.values())
    r=[]

    print m
    print prolific.keys()
    print prolific.values()


    for item in prolific:
        if prolific[item]==m:
            r.append(str(item))
    return r'''

# get list with year-values and repetitions-keys
'''print("Most prolific year(s): {}".format(most_prolific(Beatles_Discography)))

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True
print elements'''

monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}

'''def total_takings(yearly_record):
    t=0
    for item in yearly_record:
        k=yearly_record[item]
        for i in range(len(k)):
            t+=int(k[i])
    return t'''


def total_takings(yearly_record: object) -> object:
    t = 0
    for item in yearly_record:
        t += sum(yearly_record[item])
    return t


'''def total_takings(yearly_record):
    #total is used to sum up the monthly takings
    total = 0
    for month in yearly_record.keys():
        #I use the Python function sum to sum up over
        #all the elements in a list
        total = total + sum(yearly_record[month])
    return total'''

print(total_takings(monthly_takings))
