print('-'*43)
print('*** Calculadora de años, semanas y dias ***')
print('-'*43)
dias = int(input('Ingrese los dias: '))

#Calculos
anos = int(dias / 365)
resto =  dias % 365
semana = int(resto / 7)
resto = resto % 7

print('Los ' + str(dias) + ' días' + ' son: ' + str(anos) + ' años, ' + str(semana) + ' semanas y ' + str(resto) + ' dias.')
