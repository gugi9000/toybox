class Player:
    def __init__(self,name):
        self.name = name

dealer = Player("%")
player1 = Player("a")
player2 = Player("b")
player3 = Player("c")
player4 = Player("d")
player5 = Player("e")
player6 = Player("f")
        
player_list = [dealer, player1, player2, player3, player4, player5, player6]
player_no = 1

for player in player_list:
    input_name = input(f"Player {player_no} what is your name? ")
    player = Player(name=input_name)
    print(player.name)
    player_no += 1
