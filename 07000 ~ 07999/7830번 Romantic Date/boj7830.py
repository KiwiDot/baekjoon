# 백준 7830번 Romantic Date
import sys
put = sys.stdin.readline

T = int(put())
card = ['2D', '2C', '2H', '2S', '3D', '3C', '3H', '3S', '4D', '4C', '4H', '4S', '5D',
        '5C', '5H', '5S', '6D', '6C', '6H', '6S', '7D', '7C', '7H', '7S', '8D', '8C',
        '8H', '8S', '9D', '9C', '9H', '9S', 'TD', 'TC', 'TH', 'TS', 'JD', 'JC', 'JH',
        'JS', 'QD', 'QC', 'QH', 'QS', 'KD', 'KC', 'KH', 'KS', 'AD', 'AC', 'AH', 'AS']

# 카드 점수 계산
num = {'A': 140, '2': 20, '3': 30, '4': 40, '5': 50, '6': 60, '7': 70,
       '8': 80, '9': 90, 'T': 100, 'J': 110, 'Q': 120, 'K': 130}
suit = {'D': 0, 'C': 1, 'H': 2, 'S': 3}

while T:
    T -= 1
    player1 = put().split()
    player2 = set(card) - set(player1)      # 여자 친구가 들고 있는 손패
    score = 0

    for i in player1:
        idx = card.index(i)
        cnt = player2 & set(card[:idx])     # cnt는 주인공의 카드 보다 점수가 낮은 카드들

        if cnt:
            # 주인공 카드 점수의 바로 아래 카드를 제거하는 것이 가장 좋다
            score += 1
            maximum = max(cnt, key=lambda x: num[x[0]] + suit[x[1]])
            player2.discard(maximum)

    print(score)