
from prettytable import PrettyTable

x = PrettyTable()

print(x)

x.field_names = ['id','name','year']

for i in range(0,3):
    a = input('enter id :')
    b = input('enter name :')
    c = input('enter year :')
    x.add_row([a,b,c])

print(x)