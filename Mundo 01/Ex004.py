#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela

var1 = input('Digite algo: ')
print('O tipo primitivo desse valor é: {}'.format(type(var1))) 
print('Só tem espaços? {}'.format(var1.isspace())) 
print('É alfabético? {}'.format(var1.isalpha())) 
print('É alfanumérico? {}'.format(var1.isalnum())) 
print('Está em maiúsculas? {}'.format(var1.isupper())) 
print('Está em minúsculas? {}'.format(var1.islower())) 
print('Está capitalizada? {}'.format(var1.istitle())) 

