# 백준 26264번 빅데이터? 정보보호!
import sys
put = sys.stdin.readline

N = int(put())
text = put().strip()
bigdata = text.count("bigdata")
security = N - bigdata

if bigdata > security:
    print("bigdata?")
elif bigdata < security:
    print("security!")
else:
    print("bigdata? security!")