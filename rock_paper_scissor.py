import random
#Rock beats scissors
#Scissors beats paper
#Paper beats rock
game = True
player = None
choices = ["rock", "paper", "scissors"]
outcomes = {
    "rock": {
        "rock": "tie",
        "paper": "loss",
        "scissor": "win"
    },
    "paper": {
        "rock": "win",
        "paper": "tie",
        "scissor": "loss"
    },
    "scissors": {
        "rock": "loss",
        "paper": "win",
        "scissor": "tie"
    }
}

while player not in choices:
    player = input("rock, paper, scissors? " ).lower()
computer = random.choice(choices)
print(f"player: {player}")
print(f"computer: {computer}")
print(outcomes.get(player).get(computer))


        
    
