import sys

sys.argv = list(input().split())
sum = 0
for arg in sys.argv[:]:
   try:
       sum += int(arg)
   except:
       pass

sys.exit(str(sum))
