num = int(input())
print(num)
print('%d'%(num/100),'nota(s) de R$ 100,00')
num%=100
print('%d'%(num/50),'nota(s) de R$ 50,00')
num%=50
print('%d'%(num/20),'nota(s) de R$ 20,00')
num%=20
print('%d'%(num/10),'nota(s) de R$ 10,00')
num%=10
print('%d'%(num/5),'nota(s) de R$ 5,00')
num%=5
print('%d'%(num/2),'nota(s) de R$ 2,00')
num%=2
print('%d'%(num/1),'nota(s) de R$ 1,00')


