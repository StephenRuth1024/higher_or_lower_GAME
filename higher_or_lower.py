'''
Breaking the game down





3. we need to check if their guess is correct or incorrect

4. if incorrect, game over

5. correct, repeat step 2-4



'''




















'''
Solved

1. we need data: a person and their amount of instagram followers. This has been supplied with a list of dictionaries.

2. present a choice to the user. 2 people (from the data), 1 pick. the user has to pick which person they think has more followers

'''




'''


Teasing out problem 2

2. strip out all 'name': value from the dictionaries and put them in a list called name_pairs.
 Use that list to present a choice to the user. 2 people (from the list), 1 pick. 
 Remove each pick from the data to prevent duplicates. the user has to pick the person they think has more followers



choice = int(input(f"Which celebrity has more followers? Type 1 for {person1} or 2 for {person2}"))
check()





'''




'''


Teasing out problem 3


3. we need to check if their guess is correct or incorrect

check() function

This is actually quite tricky because we have the names, but we need to retrieve their instagram viewer count for each and then compare -
We can create 2 variable, instagram1 and instagram2, and pass them into a function to get the values.


and then we can do the if, elif, else: logic






def find_followers_by_name(name):
    for person in data:
        if person["name"] == name:
            return person.get("follower_count")


followers1 = find_followers_by_name(person1)
followers2 = find_followers_by_name(person2)
    


winner = []
if followers1 > followers2:
    winner.append(person1)
elif followers 2 > followers1:
    winner.append(followers2)

if choice == 1 and winner[0] == follwers1:
    print("You guessed correctly!)
else:
    print("Wrong!)
        







'''
























import random
from game_data import data



name_pairs = []
count = 0




def check(choice, person1, person2, followers1, followers2, count):
    if choice == 1 and followers1 > followers2:
            count += 1
            print(f"Correct! {person1}: {followers1} and {person2}: {followers2}")
            print()
            game(count)
    elif choice == 2 and followers2 > followers1:
            count += 1
            print(f"Correct! {person1}: {followers1} and {person2}: {followers2}")
            print()
            game(count)
    else:
        print(f"Wrong! {person1}: {followers1} and {person2}: {followers2}")
        print(f"Your score was {count}!")



def find_followers_by_name(name):
    for person in data:
        if person["name"] == name:
            return person.get("follower_count")


   

def game(count=0):
    for person in data:
        if "name" in person:
            name_pairs.append(("name", person["name"]))



    person1 = random.choice(name_pairs)
    name_pairs.remove(person1)
    person1 = person1[1]
  

    person2 = random.choice(name_pairs)
    name_pairs.remove(person2)
    person2 = person2[1]
  

    choice = int(input(f"\nWho has more followers on Instagram? Type 1 for {person1} or 2 for {person2}\n"))
    followers1 = find_followers_by_name(person1)
    followers2 = find_followers_by_name(person2)
    
    check(choice, person1, person2, followers1, followers2, count)
    
    
    
    

    

game()







'''person1 = choice(data)["name"]
data.remove(person1)

person2 = choice(data)["name"]
data.remove(person2)

choice = int(input(f"Which celebrity has more followers? Type 1 for {person1} or 2 for {person2}"))'''
