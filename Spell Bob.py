for i in range(int(input())):
    cards = [m + n for m, n in zip(list(input()), list(input()))]
    print('yes' if (
            'b' in cards[0] and 'b' in cards[1] and 'o' in cards[2] or
            'b' in cards[0] and 'o' in cards[1] and 'b' in cards[2] or
            'o' in cards[0] and 'b' in cards[1] and 'b' in cards[2]) else 'no')
