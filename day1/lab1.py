# Information about user
name = input("What's your name? ")
brothers = int(input("How many sisters do you have? "))
sisters = int(input("How many brothers do you have? "))
city_from = input("What city are you from? ")

# Use some of the operations we learned
name_length = len(name) 
siblings = brothers + sisters
perc_brothers = round(brothers / siblings * 100)
perc_sisters = round(sisters / siblings * 100)
city_lower = city_from.lower()
city_vowels = city_lower.count('a') + city_lower.count('e') + city_lower.count('i') + city_lower.count('o') + city_lower.count('u')
percentage_vowels = round(float(city_vowels) / len(city_from) * 100)

# Write a short paragraph
print('Hello, my name is ' + name)
print('My name is ' + str(name_length) + ' letters long')
print('I have ' + str(siblings) + ' siblings (' + str(perc_sisters) + ' % sisters and ' + str(perc_brothers) + ' % brothers)')
print("I'm from " + city_from)
print("My city's name contains " + str(city_vowels) + ' vowels')
print("That's " + str(percentage_vowels) + ' % vowels')