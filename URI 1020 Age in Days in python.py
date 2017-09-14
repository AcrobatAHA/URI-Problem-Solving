N = int(input())
year=N//365
N%=365
mon=N//30
N%=30
day =N
print(year,"ano(s)")
print(mon,"mes(es)")
print(day,"dia(s)")
