n = int(input())
cards = input()
all_cards = []
for i in range(0, len(cards), 2):
    all_cards.append(cards[i:i+2])

str_digit = 'TJQKAcshd'
score = [0] * n
for i in range(n):
    if 'T' in all_cards[i]:
        score[i] += 100
    if 'J' in all_cards[i]:
        score[i] += 110
    if 'Q' in all_cards[i]:
        score[i] += 120
    if 'K' in all_cards[i]:
        score[i] += 130
    if 'A' in all_cards[i]:
        score[i] += 140
    if 'c' in all_cards[i]:
        score[i] += 1
    if 's' in all_cards[i]:
        score[i] += 2
    if 'h' in all_cards[i]:
        score[i] += 3
    if 'd' in all_cards[i]:
        score[i] += 4
    if all_cards[i][0] not in str_digit:
        score[i] += int(all_cards[i][0]) * 10
for prohod in range(1, len(score)):
    for i in range(0, len(score) - prohod):
        if score[i] > score[i+1]:
            score[i], score[i+1] = score[i+1], score[i]
            all_cards[i], all_cards[i+1] = all_cards[i+1], all_cards[i]

cards = ''
for i in range(len(all_cards)):
    cards += all_cards[i]
print(cards)
