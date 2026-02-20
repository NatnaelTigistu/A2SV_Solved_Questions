n = int(input())

for _ in range(n):
    number_of_cards = int(input())
    distributed_cards = 1
    card_tracker = 2
    alice_cards = 1
    bob_cards = 0
    alice_turn = False
    while number_of_cards > distributed_cards:

        if alice_turn:
            alice_cards += card_tracker 
            card_tracker += 1
            alice_cards += card_tracker 
            card_tracker += 1
            alice_turn = False
        else:
            bob_cards += card_tracker 
            card_tracker += 1
            bob_cards += card_tracker 
            card_tracker += 1
            alice_turn = True
        distributed_cards = (alice_cards + bob_cards)
    if not alice_turn:
        alice_cards -= (distributed_cards - number_of_cards)
    else:
        bob_cards -= (distributed_cards - number_of_cards)
    print(f"{alice_cards} {bob_cards}")