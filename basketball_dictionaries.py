
##class constructor
class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"] 
        self.age = player_dict["age"] 
        self.position = player_dict["position"] 
        self.team = player_dict["team"] 
    
    #way to override init and write what you want in this format
    def __repr__(self):
        return "Player: {}, {} y/o, pos: {}, team: {}".format(self.name, self.age, self.position, self.team)    

#example dictionary to get information from
kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}

jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
    
# Create your Player instances here! or player objects

print(kevin["name"])
player_kevin = Player(kevin)
print(player_kevin)
print(player_kevin.age)

player_jason = Player(jason)
print(player_jason)

player_kyrie = Player(kyrie)
print(player_kyrie)


##Challenge 3...using for loop

players = [
    {
    "name": "Kevin Durant", 
	"age":34, 
	"position": "small forward", 
	"team": "Brooklyn Nets"
    },
    {
	"name": "Jason Tatum", 
	"age":24, 
	"position": "small forward", 
	"team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
	"age":32, "position": "Point Guard", 
	"team": "Brooklyn Nets"
    },
    {
	"name": "Damian Lillard", 
	"age":33, "position": "Point Guard", 
	"team": "Portland Trailblazers"
    },
    {
	"name": "Joel Embiid", 
	"age":32, "position": "Power Foward", 
	"team": "Philidelphia 76ers"
    },
    {
    "name": "", 
	"age":16, 
	"position": "P", 
	"team": "en"
    }
]

#for loop over the list of dictionaries
#we iterate through the list...use dict info to
#create new player instance

new_team = []
for player_dict in players:
    player = Player(player_dict)
    new_team.append(player)

print(new_team)




