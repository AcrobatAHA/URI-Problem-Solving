N = int(input())
hour = N//3600
N = N%3600
minu = N // 60
N %=60
sec=N
print("%d:%d:%d"%(hour,minu,sec))
