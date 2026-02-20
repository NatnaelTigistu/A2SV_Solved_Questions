n = int(input())

for _ in range(n):
    number_of_cards = int(input())
    distributed_cards = 1
    card_tracker = 2
    alice_white_cards = 1
    alice_black_cards = 0
    bob_white_cards = 0
    bob_black_cards = 0
    alice_turn = False

    while number_of_cards > distributed_cards:

        if alice_turn:
            alice_black_cards += card_tracker // 2
            alice_white_cards += (card_tracker + 1) // 2
            card_tracker += 1
            alice_black_cards += card_tracker // 2
            alice_white_cards += (card_tracker + 1) // 2
            card_tracker += 1
            alice_turn = False
        else:
            bob_black_cards += card_tracker // 2
            bob_white_cards += (card_tracker + 1) // 2
            card_tracker += 1
            bob_black_cards += card_tracker // 2
            bob_white_cards += (card_tracker + 1) // 2
            card_tracker += 1
            alice_turn = True

        distributed_cards = alice_black_cards + alice_white_cards + bob_black_cards + bob_white_cards

    if distributed_cards > number_of_cards:
        extra = distributed_cards - number_of_cards
        if not alice_turn:
            reduce_black = extra // 2
            reduce_white = extra - reduce_black
            alice_black_cards -= reduce_black
            alice_white_cards -= reduce_white
        else:
            reduce_black = extra // 2
            reduce_white = extra - reduce_black
            bob_black_cards -= reduce_black
            bob_white_cards -= reduce_white

    print(f"{alice_white_cards} {alice_black_cards} {bob_black_cards} {bob_white_cards}")
