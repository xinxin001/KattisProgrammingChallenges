from sys import stdin


n = int(stdin.readline())
cards = [int(x) for x in stdin.readline().split()]
final_deck = []

for i in range(n):
    if len(final_deck) != 0 and (cards[i] + final_deck[-1])%2 == 0:
        final_deck.pop()
    else:
        final_deck.append(cards[i])

print(len(final_deck))