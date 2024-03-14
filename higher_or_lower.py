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







