
class Player:
    all_players=[]
    def __init__(self,player_dic):
        self.name=player_dic['name']
        self.age=player_dic['age']
        self.position=player_dic['position']
        self.team=player_dic['team']



    def add_player(self, player_dic):
        for player in player_dic:
            all_players.append(player)

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
    

player_kevin=Player(kevin)
print(player_kevin.position)
player_jason=Player(jason)
player_kyrie=Player(kyrie)
kevin.add_player("kevin")
print(all_players)



