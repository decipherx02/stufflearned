# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Padwan')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

'''import random
def computerguess():

    low = int(input("enter a low number: "))
    high = int(input("enter a high number: "))
    guess = random.randint(low, high)
    print(guess)

computerguess()

import random
a = 5
b = 66
guess = random.randint(a,b)
print(guess)'''

#def guesscomputer(x):
 #   import random
  #  guess = random.randint(1,x)
   # a = 0

    #while a!= guess:
     #   a = int(input(f'Guess a number between 1 and {x}: '))
      #  if a > guess:
       #     print("Too high, guess again")
        #elif guess > int(a) :
         #   print ("Too low, guess again")
        #else:
         #   return print(f'you guessed {guess} correctly!')
#guesscomputer(10)

#def stutter(abc):
 #   word = str(abc)
  #  print(word[0]+word[1]+"..."+word[0]+word[1]+'..'+word[2:len(word)])

#stutter("guttentarg")


#x = "house"
#y = "job"
#print("i like to live in a {} but first i need a {}".format(x,y))
#print("job TjUMjS".count('j',0,8))

'''x = "I am an old man, who, lives in an anorak"
y = ["cat", 2, True, "face"]
z = ["2","3.3","4.5","5","8.2"]
print(x.index("an"))
print(x.rfind("an"))
print(x.count("a"))
print(x.split())
print("old" in x, "man" not in y)
print(y[:2])
print(y[3:])
y[2] = "bold"
print(y)
y[1]+=1
print(y)
print("-".join(z))
z.append("-")
print(z)
x1 = [" man " , " hat " , " house " , " cow "]
print("\n".join(x1))
print("and".join(x1))
print("without".join(sorted(x1)))'''

#a = [1,2,3,5]
#print(type(a))
#for i in range(0,len(a)):
#    a[i] += 1
#print(a)
#print(f"I live at number {a[1]} Churchill Road")

'''dimensions = 10,11, 44
width, height, length = dimensions
print(f"The dimensions are {length}, {height}")

date = 11,2,2021
day, month, year = date
a = [(11,4,2020), (12,3,2021), (11,3,2021), (10,10,2010), (10,11,2001), (11,11,11), (9,8,20)]
print(len(a))



for i in range(0,len(a)):
    if (a[i][1]) == 11:
        print(True)
    else:
        print(False)'''

#sets and datas and stuff
'''a = ["India", "Germany", "England", "England", 'India', 'Brazil', 'America', 'Jordan', 'Georgia', 'Peru', 'India', "England"]
b = ["France", "Denmark", "Norway", "Ecuador"]
print(sorted(set(a)))
print(len(set(a)))
c = set(a)
print(c)
print('India' in c)
print('India' not in a)
c.add('Italy')
print(c)
print("Brazil" in a)
print(c.pop())
print(c)
d = {2,4,14,22,9}
e = {44,22,15,77,90,4}
de = d | e
f = d&e
print(de)
#print(e.union(d))
#print(e.intersection(d))
all_countries = a + b
print(all_countries)
print(f)'''

#dic1 = {'hydrogen': 1, 'helium': 2, 'carbon': 6, 'oxygen': 8}
'''dic1['lithium'] = 3
print(dic1)
print(dic1.get('carbon'))
print(dic1.get(2))
print(dic1["oxygen"])
newterm = dic1.get('boron')
joker = newterm is not None #is not none returns True
print(joker)
print(dic1.get('oxygen', 'No chance buster'))
print(dic1.get('boron', 'No chance buster'))'''

#animals = {'dogs': [20, 10, "mark", "Cramer", False, 8, 32, 15],
 #          'cats': [3, 4, 2, 8, 2, 4],
  #         'rabbits': [2, 3, 3],
   #        'fish': [0.3, 0.5, 0.8, 0.3, 1],
    #       ('hats','scarves'): 'jump'}

#print(animals.get('rabbits'[1]))
#print(animals['rabbits'][1])
#animals["goats"] = [6,4,15, "Billy"]
#print(animals)
#print(animals["goats"][2])
#print(animals.get("goats")[3])
#x = animals['dogs'][3:(len(animals['dogs']))]
#print(x)

#animals['cats'][3] = "John"
#print(animals['cats'])
#jack = animals[('hats', 'scarves')]
#print(jack)
#animals['dogs'].append('tall')
#print(animals)
#print(animals['dogs'][2])

#dic1 = {'hydrogen': {'weight': 1, 'colour': 'blue'}, 'helium': 2, 'carbon': 6, 'oxygen': 8}
#dic1['hydrogen']['height'] = 'negligible'
#print(dic1)

#x = "I like to see my friends from time to time, however they can be a bit difficult to get ahold of, owing to their very busy lives. However sometimes they're free and would've liked to hang out."
#print(x.split())
#print(len(x.split()))



'''points = 74  
prize = ""

# use the value of points to assign prize to the correct prize name
if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <= 180:
    prize = "wafer-thin mint"
elif points >= 200:
    prize = "penguin"

# use the truth value of prize to assign result to the correct message
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)'''

#cities = "london amsterdam paris rotterdam chennai colombo copenhagan porto"
#Cities = cities.split()
#print(Cities)
#for city in Cities:
#    print(city.title())
#new_cities1 = ("Tokyo", "Canberra", "Beijing", "Toronto")
#new_cities = Cities.append(new_cities1)
#print(Cities) # cannot print new_cities - returns None

'''sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
setness = ["camel", "top", "house"]
# Write a for loop to print out each word in the sentence list, one word per line
for word in sentence:
    print(word)

for word in range(len(sentence) - 6):
    setness[word] = setness[word].title()
print(setness)'''

#names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
#usernames = []

#for name in range(len(names)):
 #   names[name] = names[name].lower()
#usernames = names

#for name in range(len(usernames)):
#    usernames[name] = usernames[name].replace(" ","_")


#print(usernames)

'''Can also be done as below to reduce number of lines'''
'''names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append(name.lower().replace(" ", "_"))
print(usernames)

for name in range(len(names)):
    names[name] = names[name].lower().replace(" ","_")'''

#x = "Yes"
#print(x.lower())
#x = x.replace("Y","N")
#print(x)

'''tokens = ['<greeting>', 'Hello World!', '</greeting>']

count = 0
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)'''

#formatting new lines and stuff
'''items = ['first string', 'second string']
html_str = "<ul>\n"          # The "\n" here is the end-of-line char, causing
                             # chars after this in html_str to be on next line


for item in items:
    html_str += f'<li>{item}</li>\n'
#    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)'''

#dictionary counting
'''book = "This is my story of how I came from nothing, faced many hurdles, and finally made something of my life. I will begin with my first memory, well maybe not the first memory, but one of the earlier memories."
book = book.split()
print(book)
book_words = {}

for word in book:
    book_words[word] = book_words.get(word,0) + 1
#above is a simplified version of below:
   # if word not in book_words:
   #     book_words[word] = 1
   # else:
   #     book_words[word] += 1
print(book_words)'''

#cast = {
#           "Jerry Seinfeld": "Jerry Seinfeld",
#           "Julia Louis-Dreyfus": "Elaine Benes",
#           "Jason Alexander": "George Costanza",
#           "Michael Richards": "Cosmo Kramer"
#       }

#print("Iterating through keys:")
#for key in cast:
#    print(key)

#print("\nIterating through keys and values:")
#for key, value in cast.items():
#    print("Actor: {}    Role: {}".format(key, value))

'''carddeck = [2,4,3,11,10,5,1,6]
hand = []

while sum(hand) <= 17:
    hand.append(carddeck.pop())

print(hand)'''

'''def factorial(n):
#    if n == 1:
#        return 1
#    elif n == 2:
#        return 2
#    elif n == 2:
#        return 6
#    else:
#        return n * (factorial(n-1))
#print(factorial(5))

number = 5
current = 1
product = 1
while current <= number:
    product *= current    #first iteration, where curret = 1, product = 1(current)*1(product) = 1
                          #second iteration, where current =2, product = 2(current)*1(old_product) = 2
                          #third iteration, where current = 3, product = 3(current)*2(old_product)  = 6
    current +=1
print(product)

for index in range(2,number +1):
    product *= index
print(product)'''

'''limit = 1009
number = 1

#for number in range(limit):
#    if number * number <= limit:
#        result = number

print(result)

while number**2 <= limit:
    number +=1
    result = (number-1)**2
print(result)

print(961**0.5)
print(32**2)'''

#Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together.
#If there are more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers,
#add all of the odd numbers.

#my attempt
'''num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69,
            113, 166]
x = []
for number in num_list:
    if number % 2 != 0:
        x.append(number)

print(x)

a = []
while number in x < 5:

for number in range(0, 5):
    y = x[number]
    print(y)
    a.append(y)

print(a)
print(sum(a))'''

#actual answer:
'''num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list): 
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The sum of the odd numbers added is: {}".format(list_sum))'''


'''manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]
shipment = []
weight = 0

for cargo, cargo_weight in manifest:
    if weight >= 100:
        break
    elif weight +cargo_weight > 100:
        continue
    else:
        shipment.append(cargo)
        weight+=cargo_weight
print(shipment)
print(weight)

manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))'''


#CONTINUE LOOP PRACTICE
'''my solution
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Paperbook Review: Totally Terrific"]


news_ticker = []
headlines_characters = {}

length_of_headlines = 0

for headline in headlines:
    headlines_characters[headline] = len(headline)

print(headlines_characters)

for headline, characters in headlines_characters.items():
    #print(f'{headline},{characters}')
    if length_of_headlines >= 170:
        #print("breaking from loop now!")
        break
    elif characters + length_of_headlines > 170:
        #print(f'skipping {headline} now')
        continue
    else:
        #print(f'adding {headline} now')
        length_of_headlines += characters
        news_ticker.append(headline)

print(news_ticker)'''

#Actual solution:
'''headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""

for headline in headlines:
    news_ticker +=headline + "," + " "
    if len(news_ticker) > 140:
        news_ticker = news_ticker[:100]
        break

print(news_ticker)'''

#check_prime = [5,7,11,26, 39, 51, 53, 57, 79, 85, 121, 143, 144]
# my solution WHICH DOES NOT WORK!!
#for number in check_prime:
#    if number == 3 or number == 5 or number == 7:
#        print(f'{number} is prime')
#    elif (number % 2) == 0 or (number % 3) == 0 or (number % 5) == 0 or (number % 7) == 0 or (number % (number**0.5)) == 0:
#        print(f'{number} is not prime')
#    else:
#        print(f'{number} is prime')
#actual solution
'''for number in check_prime:
    for num in range(2,number):
        if number%num == 0:
            print(f'{number} is NOT a prime number, because {num} is a factor of {number}')
            break
        elif num == number - 1:
            print(f'{number} is a prime number')'''

#zip function
'''headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Paperbook Review: Totally Terrific"]

characters = []

for headline in headlines:
    characters.append(len(headline))

print(characters)

x = list(zip(headlines,characters))
print(x)'''

#enumerate function and practising earlier quiz question again about headlines and newstickers
'''x = "hello, time, car, cake, park, house, lawn, mother, cow, games, car, well, carriage"
words = x.split()
wordslist = list(enumerate(words))
#print(wordslist)
newstick=""

for word in words:
    newstick += word + " "
    if len(newstick) >45:
        newstick = newstick[:45]
        break
print(newstick)'''


#testing out zipping
'''letters = ['a', 'b', 'c']
nums = [1, 2, 3]
words = ["hello", "hi", "welcome"]

for letter, num, word in zip(letters, nums, words):
    print(f"{letter}: {num}, {word}")

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
points = []
# points = list(zip(labels, x_coord, y_coord, z_coord))

for label, x, y, z in zip(labels, x_coord, y_coord, z_coord):
    points.append(f"{label}: {x}, {y}, {z}")

for point in points:
    print(point)

#unzipping tuples:
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

names, heights = zip(*cast)

print(names)
print(heights)'''

#transpose with zip
'''data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

#first,second,third = zip(*data)
#data_transpose = first,second,third
data_transpose = tuple(zip(*data))
print(data_transpose)'''

#cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
#heights = [72, 68, 72, 66, 76]

#for i, character in enumerate(cast):
#    cast[i] = character + " " + str(heights[i])

#print(cast)

'''X = ("london, tokyo, paris, berlin, chennai, amsterdam, copenhagen, washing, toronto, auckland, sydney")
cities = X.split()
capitalized_cities = [city.title() for city in cities]
squares = [x**2 for x in range(9) if x % 2 == 0]
squared = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
print(capitalized_cities,"\n", squares,"\n", squared)'''

#COMPREHENSIONS PRACTICE
'''cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]

firstnames = [name[0].lower().split() for name in cast]
firstnames_ = [name.split()[0].lower() for name in cast]
first_names = []
#for name in cast:
#    #name = name.lower()
#    name = name.split()
#    first_names.append(name[0].lower())
print(first_names)
print(firstnames)
print(firstnames_)'''

#QUIZ QUESTIONS - OSCAR WINNERS

'''nominated = {1931: ['Norman Taurog', 'Wesley Ruggles', 'Clarence Brown', 'Lewis Milestone', 'Josef Von Sternberg'], 1932: ['Frank Borzage', 'King Vidor', 'Josef Von Sternberg'], 1933: ['Frank Lloyd', 'Frank Capra', 'George Cukor'], 1934: ['Frank Capra', 'Victor Schertzinger', 'W. S. Van Dyke'], 1935: ['John Ford', 'Michael Curtiz', 'Henry Hathaway', 'Frank Lloyd'], 1936: ['Frank Capra', 'William Wyler', 'Robert Z. Leonard', 'Gregory La Cava', 'W. S. Van Dyke'], 1937: ['Leo McCarey', 'Sidney Franklin', 'William Dieterle', 'Gregory La Cava', 'William Wellman'], 1938: ['Frank Capra', 'Michael Curtiz', 'Norman Taurog', 'King Vidor', 'Michael Curtiz'], 1939: ['Sam Wood', 'Frank Capra', 'John Ford', 'William Wyler', 'Victor Fleming'], 1940: ['John Ford', 'Sam Wood', 'William Wyler', 'George Cukor', 'Alfred Hitchcock'], 1941: ['John Ford', 'Orson Welles', 'Alexander Hall', 'William Wyler', 'Howard Hawks'], 1942: ['Sam Wood', 'Mervyn LeRoy', 'John Farrow', 'Michael Curtiz', 'William Wyler'], 1943: ['Michael Curtiz', 'Ernst Lubitsch', 'Clarence Brown', 'George Stevens', 'Henry King'], 1944: ['Leo McCarey', 'Billy Wilder', 'Otto Preminger', 'Alfred Hitchcock', 'Henry King'], 1945: ['Billy Wilder', 'Leo McCarey', 'Clarence Brown', 'Jean Renoir', 'Alfred Hitchcock'], 1946: ['David Lean', 'Frank Capra', 'Robert Siodmak', 'Clarence Brown', 'William Wyler'], 1947: ['Elia Kazan', 'Henry Koster', 'Edward Dmytryk', 'George Cukor', 'David Lean'], 1948: ['John Huston', 'Laurence Olivier', 'Jean Negulesco', 'Fred Zinnemann', 'Anatole Litvak'], 1949: ['Joseph L. Mankiewicz', 'Robert Rossen', 'William A. Wellman', 'Carol Reed', 'William Wyler'], 1950: ['Joseph L. Mankiewicz', 'John Huston', 'George Cukor', 'Billy Wilder', 'Carol Reed'], 1951: ['George Stevens', 'John Huston', 'Vincente Minnelli', 'William Wyler', 'Elia Kazan'], 1952: ['John Ford', 'Joseph L. Mankiewicz', 'Cecil B. DeMille', 'Fred Zinnemann', 'John Huston'], 1953: ['Fred Zinnemann', 'Charles Walters', 'William Wyler', 'George Stevens', 'Billy Wilder'], 1954: ['Elia Kazan', 'George Seaton', 'William Wellman', 'Alfred Hitchcock', 'Billy Wilder'], 1955: ['Delbert Mann', 'John Sturges', 'Elia Kazan', 'Joshua Logan', 'David Lean'], 1956: ['George Stevens', 'Michael Anderson', 'William Wyler', 'Walter Lang', 'King Vidor'], 1957: ['David Lean', 'Mark Robson', 'Joshua Logan', 'Sidney Lumet', 'Billy Wilder'], 1958: ['Richard Brooks', 'Stanley Kramer', 'Robert Wise', 'Mark Robson', 'Vincente Minnelli'], 1959: ['George Stevens', 'Fred Zinnemann', 'Jack Clayton', 'Billy Wilder', 'William Wyler'], 1960: ['Billy Wilder', 'Jules Dassin', 'Alfred Hitchcock', 'Jack Cardiff', 'Fred Zinnemann'], 1961: ['J. Lee Thompson', 'Robert Rossen', 'Stanley Kramer', 'Federico Fellini', 'Robert Wise', 'Jerome Robbins'], 1962: ['David Lean', 'Frank Perry', 'Pietro Germi', 'Arthur Penn', 'Robert Mulligan'], 1963: ['Elia Kazan', 'Otto Preminger', 'Federico Fellini', 'Martin Ritt', 'Tony Richardson'], 1964: ['George Cukor', 'Peter Glenville', 'Stanley Kubrick', 'Robert Stevenson', 'Michael Cacoyannis'], 1965: ['William Wyler', 'John Schlesinger', 'David Lean', 'Hiroshi Teshigahara', 'Robert Wise'], 1966: ['Fred Zinnemann', 'Michelangelo Antonioni', 'Claude Lelouch', 'Richard Brooks', 'Mike Nichols'], 1967: ['Arthur Penn', 'Stanley Kramer', 'Richard Brooks', 'Norman Jewison', 'Mike Nichols'], 1968: ['Carol Reed', 'Gillo Pontecorvo', 'Anthony Harvey', 'Franco Zeffirelli', 'Stanley Kubrick'], 1969: ['John Schlesinger', 'Arthur Penn', 'George Roy Hill', 'Sydney Pollack', 'Costa-Gavras'], 1970: ['Franklin J. Schaffner', 'Federico Fellini', 'Arthur Hiller', 'Robert Altman', 'Ken Russell'], 1971: ['Stanley Kubrick', 'Norman Jewison', 'Peter Bogdanovich', 'John Schlesinger', 'William Friedkin'], 1972: ['Bob Fosse', 'John Boorman', 'Jan Troell', 'Francis Ford Coppola', 'Joseph L. Mankiewicz'], 1973: ['George Roy Hill', 'George Lucas', 'Ingmar Bergman', 'William Friedkin', 'Bernardo Bertolucci'], 1974: ['Francis Ford Coppola', 'Roman Polanski', 'Francois Truffaut', 'Bob Fosse', 'John Cassavetes'], 1975: ['Federico Fellini', 'Stanley Kubrick', 'Sidney Lumet', 'Robert Altman', 'Milos Forman'], 1976: ['Alan J. Pakula', 'Ingmar Bergman', 'Sidney Lumet', 'Lina Wertmuller', 'John G. Avildsen'], 1977: ['Steven Spielberg', 'Fred Zinnemann', 'George Lucas', 'Herbert Ross', 'Woody Allen'], 1978: ['Hal Ashby', 'Warren Beatty', 'Buck Henry', 'Woody Allen', 'Alan Parker', 'Michael Cimino'], 1979: ['Bob Fosse', 'Francis Coppola', 'Peter Yates', 'Edouard Molinaro', 'Robert Benton'], 1980: ['David Lynch', 'Martin Scorsese', 'Richard Rush', 'Roman Polanski', 'Robert Redford'], 1981: ['Louis Malle', 'Hugh Hudson', 'Mark Rydell', 'Steven Spielberg', 'Warren Beatty'], 1982: ['Wolfgang Petersen', 'Steven Spielberg', 'Sydney Pollack', 'Sidney Lumet', 'Richard Attenborough'], 1983: ['Peter Yates', 'Ingmar Bergman', 'Mike Nichols', 'Bruce Beresford', 'James L. Brooks'], 1984: ['Woody Allen', 'Roland Joffe', 'David Lean', 'Robert Benton', 'Milos Forman'], 1985: ['Hector Babenco', 'John Huston', 'Akira Kurosawa', 'Peter Weir', 'Sydney Pollack'], 1986: ['David Lynch', 'Woody Allen', 'Roland Joffe', 'James Ivory', 'Oliver Stone'], 1987: ['Bernardo Bertolucci', 'Adrian Lyne', 'John Boorman', 'Norman Jewison', 'Lasse Hallstrom'], 1988: ['Barry Levinson', 'Charles Crichton', 'Martin Scorsese', 'Alan Parker', 'Mike Nichols'], 1989: ['Woody Allen', 'Peter Weir', 'Kenneth Branagh', 'Jim Sheridan', 'Oliver Stone'], 1990: ['Francis Ford Coppola', 'Martin Scorsese', 'Stephen Frears', 'Barbet Schroeder', 'Kevin Costner'], 1991: ['John Singleton', 'Barry Levinson', 'Oliver Stone', 'Ridley Scott', 'Jonathan Demme'], 1992: ['Clint Eastwood', 'Neil Jordan', 'James Ivory', 'Robert Altman', 'Martin Brest'], 1993: ['Jim Sheridan', 'Jane Campion', 'James Ivory', 'Robert Altman', 'Steven Spielberg'], 1994: ['Woody Allen', 'Quentin Tarantino', 'Robert Redford', 'Krzysztof Kieslowski', 'Robert Zemeckis'], 1995: ['Chris Noonan', 'Tim Robbins', 'Mike Figgis', 'Michael Radford', 'Mel Gibson'], 1996: ['Anthony Minghella', 'Joel Coen', 'Milos Forman', 'Mike Leigh', 'Scott Hicks'], 1997: ['Peter Cattaneo', 'Gus Van Sant', 'Curtis Hanson', 'Atom Egoyan', 'James Cameron'], 1998: ['Roberto Benigni', 'John Madden', 'Terrence Malick', 'Peter Weir', 'Steven Spielberg'], 1999: ['Spike Jonze', 'Lasse Hallstrom', 'Michael Mann', 'M. Night Shyamalan', 'Sam Mendes'], 2000: ['Stephen Daldry', 'Ang Lee', 'Steven Soderbergh', 'Ridley Scott', 'Steven Soderbergh'], 2001: ['Ridley Scott', 'Robert Altman', 'Peter Jackson', 'David Lynch', 'Ron Howard'], 2002: ['Rob Marshall', 'Martin Scorsese', 'Stephen Daldry', 'Pedro Almodovar', 'Roman Polanski'], 2003: ['Fernando Meirelles', 'Sofia Coppola', 'Peter Weir', 'Clint Eastwood', 'Peter Jackson'], 2004: ['Martin Scorsese', 'Taylor Hackford', 'Alexander Payne', 'Mike Leigh', 'Clint Eastwood'], 2005: ['Ang Lee', 'Bennett Miller', 'Paul Haggis', 'George Clooney', 'Steven Spielberg'], 2006: ['Alejandro Gonzaalez Inarritu', 'Clint Eastwood', 'Stephen Frears', 'Paul Greengrass', 'Martin Scorsese'], 2007: ['Julian Schnabel', 'Jason Reitman', 'Tony Gilroy', 'Paul Thomas Anderson', 'Joel Coen', 'Ethan Coen'], 2008: ['David Fincher', 'Ron Howard', 'Gus Van Sant', 'Stephen Daldry', 'Danny Boyle'], 2009: ['James Cameron', 'Quentin Tarantino', 'Lee Daniels', 'Jason Reitman', 'Kathryn Bigelow'], 2010: ['Darren Aronofsky', 'David O. Russell', 'David Fincher', 'Ethan Coen', 'Joel Coen', 'Tom Hooper']}
winners = {1931: ['Norman Taurog'], 1932: ['Frank Borzage'], 1933: ['Frank Lloyd'], 1934: ['Frank Capra'], 1935: ['John Ford'], 1936: ['Frank Capra'], 1937: ['Leo McCarey'], 1938: ['Frank Capra'], 1939: ['Victor Fleming'], 1940: ['John Ford'], 1941: ['John Ford'], 1942: ['William Wyler'], 1943: ['Michael Curtiz'], 1944: ['Leo McCarey'], 1945: ['Billy Wilder'], 1946: ['William Wyler'], 1947: ['Elia Kazan'], 1948: ['John Huston'], 1949: ['Joseph L. Mankiewicz'], 1950: ['Joseph L. Mankiewicz'], 1951: ['George Stevens'], 1952: ['John Ford'], 1953: ['Fred Zinnemann'], 1954: ['Elia Kazan'], 1955: ['Delbert Mann'], 1956: ['George Stevens'], 1957: ['David Lean'], 1958: ['Vincente Minnelli'], 1959: ['William Wyler'], 1960: ['Billy Wilder'], 1961: ['Jerome Robbins', 'Robert Wise'], 1962: ['David Lean'], 1963: ['Tony Richardson'], 1964: ['George Cukor'], 1965: ['Robert Wise'], 1966: ['Fred Zinnemann'], 1967: ['Mike Nichols'], 1968: ['Carol Reed'], 1969: ['John Schlesinger'], 1970: ['Franklin J. Schaffner'], 1971: ['William Friedkin'], 1972: ['Bob Fosse'], 1973: ['George Roy Hill'], 1974: ['Francis Ford Coppola'], 1975: ['Milos Forman'], 1976: ['John G. Avildsen'], 1977: ['Woody Allen'], 1978: ['Michael Cimino'], 1979: ['Robert Benton'], 1980: ['Robert Redford'], 1981: ['Warren Beatty'], 1982: ['Richard Attenborough'], 1983: ['James L. Brooks'], 1984: ['Milos Forman'], 1985: ['Sydney Pollack'], 1986: ['Oliver Stone'], 1987: ['Bernardo Bertolucci'], 1988: ['Barry Levinson'], 1989: ['Oliver Stone'], 1990: ['Kevin Costner'], 1991: ['Jonathan Demme'], 1992: ['Clint Eastwood'], 1993: ['Steven Spielberg'], 1994: ['Robert Zemeckis'], 1995: ['Mel Gibson'], 1996: ['Anthony Minghella'], 1997: ['James Cameron'], 1998: ['Steven Spielberg'], 1999: ['Sam Mendes'], 2000: ['Steven Soderbergh'], 2001: ['Ron Howard'], 2002: ['Roman Polanski'], 2003: ['Peter Jackson'], 2004: ['Clint Eastwood'], 2005: ['Ang Lee'], 2006: ['Martin Scorsese'], 2007: ['Ethan Coen', 'Joel Coen'], 2008: ['Danny Boyle'], 2009: ['Kathryn Bigelow'], 2010: ['Tom Hooper']}
nominees = []
count = 0
for year,Nominees in nominated.items():
    nominees.append(Nominees)
print(nominees)
nominees = tuple(zip(*nominees))
#print(nominees)
print(nominees[1])
#print(nominees.count(nominees[2]))'''

    #print (nominee)
    #print(nominee[0])
    #print (nominee[count])
    #print(nominee[1:len(nominee)])

'''fruits = (('apple', 'strawberry', 'apple', 'orange', 'apple', 'apple', 'strawberry', 'apple', 'orange', 'apple'))

print(fruits)
print(fruits[0])
print(fruits.count(fruits[0]))

for fruit in fruits:
    print(fruit)'''


cast_dictionary = {'Barney': 72, 'Robin': 68, 'Ted': 71, "Lily": 66, "Marshall": 76}
cast_list = [("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76)]
castlist=[]

# define names and heights here
'''names,heights = zip(*cast_list)

print(names)

for name, height in cast_dictionary.items():
    both = [name,height]
    castlist.append(both)
print(castlist)

names,height = zip(*castlist)
print(names)

#answer from stackoverflow for how to make dictionary into a list
for key, value in dict.iteritems():
    temp = [key,value]
    dictlist.append(temp)'''

#OSCAR WINNERS QUIZ QUESTION2
'''winners = {1931: ['Norman Taurog'], 1932: ['Frank Borzage'], 1933: ['Frank Lloyd'], 1934: ['Frank Capra'],
           1935: ['John Ford'], 1936: ['Frank Capra'], 1937: ['Leo McCarey'], 1938: ['Frank Capra'],
           1939: ['Victor Fleming'], 1940: ['John Ford'], 1941: ['John Ford'], 1942: ['William Wyler'],
           1943: ['Michael Curtiz'], 1944: ['Leo McCarey'], 1945: ['Billy Wilder'], 1946: ['William Wyler'],
           1947: ['Elia Kazan'], 1948: ['John Huston'], 1949: ['Joseph L. Mankiewicz'], 1950: ['Joseph L. Mankiewicz'],
           1951: ['George Stevens'], 1952: ['John Ford'], 1953: ['Fred Zinnemann'], 1954: ['Elia Kazan'],
           1955: ['Delbert Mann'], 1956: ['George Stevens'], 1957: ['David Lean'], 1958: ['Vincente Minnelli'],
           1959: ['William Wyler'], 1960: ['Billy Wilder'], 1961: ['Jerome Robbins', 'Robert Wise'],
           1962: ['David Lean'], 1963: ['Tony Richardson'], 1964: ['George Cukor'], 1965: ['Robert Wise'],
           1966: ['Fred Zinnemann'], 1967: ['Mike Nichols'], 1968: ['Carol Reed'], 1969: ['John Schlesinger'],
           1970: ['Franklin J. Schaffner'], 1971: ['William Friedkin'], 1972: ['Bob Fosse'], 1973: ['George Roy Hill'],
           1974: ['Francis Ford Coppola'], 1975: ['Milos Forman'], 1976: ['John G. Avildsen'], 1977: ['Woody Allen'],
           1978: ['Michael Cimino'], 1979: ['Robert Benton'], 1980: ['Robert Redford'], 1981: ['Warren Beatty'],
           1982: ['Richard Attenborough'], 1983: ['James L. Brooks'], 1984: ['Milos Forman'], 1985: ['Sydney Pollack'],
           1986: ['Oliver Stone'], 1987: ['Bernardo Bertolucci'], 1988: ['Barry Levinson'], 1989: ['Oliver Stone'],
           1990: ['Kevin Costner'], 1991: ['Jonathan Demme'], 1992: ['Clint Eastwood'], 1993: ['Steven Spielberg'],
           1994: ['Robert Zemeckis'], 1995: ['Mel Gibson'], 1996: ['Anthony Minghella'], 1997: ['James Cameron'],
           1998: ['Steven Spielberg'], 1999: ['Sam Mendes'], 2000: ['Steven Soderbergh'], 2001: ['Ron Howard'],
           2002: ['Roman Polanski'], 2003: ['Peter Jackson'], 2004: ['Clint Eastwood'], 2005: ['Ang Lee'],
           2006: ['Martin Scorsese'], 2007: ['Ethan Coen', 'Joel Coen'], 2008: ['Danny Boyle'],
           2009: ['Kathryn Bigelow'], 2010: ['Tom Hooper']}
winner_year = []
count = 0

for year, winner in winners.items():
    both = [year, winner]
    winner_year.append(both)

# print(winner_year)

year, winnernames = zip(*winner_year)
# print(winnernames)

# print(winnernames.count(winnernames[3]))
win_directors = []
win_directors1 = []

for winner in winnernames:
    # print(winner,winnernames.count(winnernames[count]))
    win_director = winner, winnernames.count(winnernames[count])
    #print(win_director)
    count += 1
    win_directors.append(win_director)

print(win_directors)
#win_directors = set(win_directors)
#print(win_directors)'''



'''x = [(["house"],5), (["jump"],1), (["cow"],3), (["jump"],1)]

x = sorted(x)
print(x)
y = []

for word,number in x:
    z = number,word
    y.append(z)

print(y)

y = sorted(y)
print(y)
y = set(y)
print(y)'''

#OSCAR WINNERS QUIZ QUESTION 2 attempt 2
winners = {1931: ['Norman Taurog'], 1932: ['Frank Borzage'], 1933: ['Frank Lloyd'], 1934: ['Frank Capra'],
           1935: ['John Ford'], 1936: ['Frank Capra'], 1937: ['Leo McCarey'], 1938: ['Frank Capra'],
           1939: ['Victor Fleming'], 1940: ['John Ford'], 1941: ['John Ford'], 1942: ['William Wyler'],
           1943: ['Michael Curtiz'], 1944: ['Leo McCarey'], 1945: ['Billy Wilder'], 1946: ['William Wyler'],
           1947: ['Elia Kazan'], 1948: ['John Huston'], 1949: ['Joseph L. Mankiewicz'], 1950: ['Joseph L. Mankiewicz'],
           1951: ['George Stevens'], 1952: ['John Ford'], 1953: ['Fred Zinnemann'], 1954: ['Elia Kazan'],
           1955: ['Delbert Mann'], 1956: ['George Stevens'], 1957: ['David Lean'], 1958: ['Vincente Minnelli'],
           1959: ['William Wyler'], 1960: ['Billy Wilder'], 1961: ['Jerome Robbins', 'Robert Wise'],
           1962: ['David Lean'], 1963: ['Tony Richardson'], 1964: ['George Cukor'], 1965: ['Robert Wise'],
           1966: ['Fred Zinnemann'], 1967: ['Mike Nichols'], 1968: ['Carol Reed'], 1969: ['John Schlesinger'],
           1970: ['Franklin J. Schaffner'], 1971: ['William Friedkin'], 1972: ['Bob Fosse'], 1973: ['George Roy Hill'],
           1974: ['Francis Ford Coppola'], 1975: ['Milos Forman'], 1976: ['John G. Avildsen'], 1977: ['Woody Allen'],
           1978: ['Michael Cimino'], 1979: ['Robert Benton'], 1980: ['Robert Redford'], 1981: ['Warren Beatty'],
           1982: ['Richard Attenborough'], 1983: ['James L. Brooks'], 1984: ['Milos Forman'], 1985: ['Sydney Pollack'],
           1986: ['Oliver Stone'], 1987: ['Bernardo Bertolucci'], 1988: ['Barry Levinson'], 1989: ['Oliver Stone'],
           1990: ['Kevin Costner'], 1991: ['Jonathan Demme'], 1992: ['Clint Eastwood'], 1993: ['Steven Spielberg'],
           1994: ['Robert Zemeckis'], 1995: ['Mel Gibson'], 1996: ['Anthony Minghella'], 1997: ['James Cameron'],
           1998: ['Steven Spielberg'], 1999: ['Sam Mendes'], 2000: ['Steven Soderbergh'], 2001: ['Ron Howard'],
           2002: ['Roman Polanski'], 2003: ['Peter Jackson'], 2004: ['Clint Eastwood'], 2005: ['Ang Lee'],
           2006: ['Martin Scorsese'], 2007: ['Ethan Coen', 'Joel Coen'], 2008: ['Danny Boyle'],
           2009: ['Kathryn Bigelow'], 2010: ['Tom Hooper']}
#ACTUAL PROPER ANSWER

win_count_dict = {}
for year, winnerlist in winners.items():
    for winner in winnerlist:
        win_count_dict[winner] = win_count_dict.get(winner, 0) + 1
print(win_count_dict)
#highest_count = max(win_count_dict.values())

#most_win_director = [key for key, value in win_count_dict.items() if value == highest_count]
#print(most_win_director)

#BELOW IS MY LONG WINDED ANSWER
'''winner_year = []
count = 0

for year, winner in winners.items():
    both = [year, winner]
    winner_year.append(both)

# print(winner_year)

year, winnernames = zip(*winner_year)
# print(winnernames)

# print(winnernames.count(winnernames[3]))
win_directors = []
win_directors1 = []

for winner in winnernames:
    # print(winner,winnernames.count(winnernames[count]))
    win_director = winner, winnernames.count(winnernames[count])
    # print(win_director)
    count += 1
    win_directors.append(win_director)

for name, wins in win_directors:
    z = wins, name
    win_directors1.append(z)

win_directors1 = sorted(win_directors1)
# print(win_directors1)

final = []
for winner_time in win_directors1:
    if winner_time in final:
        continue
    else:
        final.append(winner_time)

# print(final)

most_win_director = []

for winner_time in final:
    if winner_time[0] == final[len(final)-1][0]:
        most_win_director.append(winner_time[1])

print(most_win_director)'''



