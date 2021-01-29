database = [
    {"name":"Iron man", "human":True, "youtuber":False, "movie":True , "original":False, "inventor":True, "indian":False},

    {"name": "Einstein", "human": True, "youtuber": False, "movie": False, "original": True, "inventor": True,"indian": False},

    {"name": "Carry Minati", "human": True, "youtuber": True, "movie": False, "original": True, "inventor": False,"indian": True},

    {"name": "PewDiePie", "human": True, "youtuber": True, "movie": False, "original": True, "inventor": False,"indian": False},

    {"name": "Nemo", "human": False, "youtuber": False, "movie": True, "original": False, "inventor": False,"indian": False},

    {"name": "Narendra Modi", "human": True, "youtuber": False, "movie": False, "original": True, "inventor": False,"indian": True},

    {"name": "Mukesh Ambani", "human": True, "youtuber": False, "movie": False, "original": True, "inventor": True,"indian": True},
]

def take_chance(answer, property):
    if answer == "y":
        ans = True
    else:
        ans = False

    to_remove=[]
    for d in database:
        if d[property] != ans:
            to_remove.append(d)

    for i in to_remove:
        database.remove(i)

    if len(database) == 1:
        print("your character is "+database[0]["name"])
        quit()


ans = input("is your character human(y,n)")
take_chance(ans, "human")


ans = input("Is your character Youtuber(y,n)")
take_chance(ans, "youtuber")

ans = input("Is your character in a movie(y,n)")
take_chance(ans,"movie")

ans = input("Is your character original(y,n)")
take_chance(ans,"original")

ans = input("Is your character Inventor(y,n)")
take_chance(ans,"inventor")

ans = input("Is your character Indian(y,n)")
take_chance(ans,"indian")


