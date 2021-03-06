a = int(input('Nhap a:'))
b = int(input('Nhap b:'))
UCLN = 1
if(a>b):
  for i in range (2,a):
    if (a%i==0 and b%i==0):
      print('UCLN : ',i)
      UCLN=i
else:
  for i in range (2,b):
    if (a%i==0 and b%i==0):
      print('UCLN : ',i)
      UCLN=i

print(f'BCNN {a} va {b} la ',(a*b)/UCLN)
