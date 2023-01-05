# 백준 24912번 카드 색칠
import sys
put = sys.stdin.readline

N = int(put())
card = put().split()
card = ''.join(card)

card = card.replace("102", "132")
card = card.replace("201", "231")

card = card.replace("203", "213")
card = card.replace("302", "312")

card = card.replace("103", "123")
card = card.replace("301", "321")

card = card.replace("01", "31")
card = card.replace("10", "12")

card = card.replace("00", "12")
card = card.replace("0", "1")

if '11' in card or '22' in card or '33' in card:
    card = ['-1']

print(' '.join(list(card)))