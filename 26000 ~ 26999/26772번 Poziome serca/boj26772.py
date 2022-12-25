# 백준 26772번 Poziome serca
import sys
put = sys.stdin.readline

serca = """ @@@   @@@ 
@   @ @   @
@    @    @
@         @
 @       @ 
  @     @  
   @   @   
    @ @    
     @     """

serca = [i for i in serca.split('\n')]

N = int(put())

for i in serca:
    print((i + ' ') * N)