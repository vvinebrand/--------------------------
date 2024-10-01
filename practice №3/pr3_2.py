import random

def card_dealing(num_players, cards, deck):
    random.shuffle(deck)
    player_hands = [[] for _ in range(num_players)]

    for _ in range(cards):
        for player_index in range(num_players):
            player_hands[player_index].append(deck.pop(0))

    return player_hands

# колода
suits = ['черви', 'руби', 'буби', 'пики']
ranks = ['туз', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король']
deck = [f"{rank} {suit}" for suit in suits for rank in ranks]

num_players = int(input('введите количество игроков: '))
cards_per_player = int(input('\nвведите количество карт для одного игрока: '))
player_hands = card_dealing(num_players, cards_per_player, deck)

print()
for player_index, hand in enumerate(player_hands):
    print(f"игрок {player_index + 1}: {', '.join(hand)}")

print(f"\nкарты в колоде: {', '.join(deck)}")