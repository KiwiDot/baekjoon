# 백준 5342번 Billing
import sys
put = sys.stdin.readline

item = {"Paper": 57.99, "Printer": 120.50, "Planners": 31.25,
        "Binders": 22.50, "Calendar": 10.95, "Notebooks":11.20, "Ink": 66.95}
cost = 0

while True:
    text = put().strip()
    if text == "EOI":
        break

    cost += item[text]

print("${:.2f}".format(cost))