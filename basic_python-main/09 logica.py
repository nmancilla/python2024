# #Operadores booleanos
# '''
# Operación     Significado
# <             estrictamente menor que
# <=            menor o igual que
# >             estrictamente mayor que
# >=            mayor o igual que
# ==            igual que
# !=            diferente que
# is            igualdad a nivel de identidad (Son el mismo objeto)
# is not        desigualdad a nivel de identidad (no son el mismo objeto)
# '''
# proposicion = not ((10 > 2 + 2) and (5 < 3 or 6 > 1))
# #                       true           false   true
# #                       true            true
# #                               true
# #                               False
# print(proposicion)







#   Resultado     Resultado     A and B     A or B    A ^ B (XOR) (“algunos pero no todos”)
#   Prueba A      Prueba B
#   ----------+--------------+-----------+---------+---------
#   True          True          True        True      False
#   True          False         False       True      True
#   False         True          False       True      True
#   False         False         False       False      False







# x = not ( (3 > 7) and ( 4 > 1 + 1) or (5 < 10 - 3)) #
# #   not      F    and  (     T      or      T  )
# #   not      F    and              T
# #   not             F
# #           T
# #   x = true







'''
Juan tiene 27 años
No tiene Hijos
Salió al colegio a los 17 años
Estudio por 6 años en la Universidad
Lleva 3 años pololeando o de noviazgo
Tiene 4 años de Experiencia Laboral
'''

# Variables
nombre = "Juan"
edad = 27 # años
n_hijos = 0
graduacion_colegio = 17 # años 
duracion_uni = 6 # años
duracion_pololeo = 3 # años
exp_laboral = 4 # años

# ¿Juan es mayor de edad?
print(edad >= 18)

#¿Juan se graduó del colegio antes de los 18 años? 
print(graduacion_colegio < 18)

#¿Juan no tiene 4 años de experiencia laboral?
print(exp_laboral != 4)

#¿Juan tiene hijos?
print(n_hijos > 0)

#¿Juan no tiene hijos?
print(n_hijos == 0)


#¿Al graduarse de la Universidad ya había cumplido 22?
edad_grad_uni = graduacion_colegio + duracion_uni
print(edad_grad_uni >= 22)

#¿Juan comenzó a pololear a los 25?
edad_inicio_pololeo = edad - duracion_pololeo
print(edad_inicio_pololeo == 25)

#¿Juan lleva más tiempo trabajando o estudiando?
print(exp_laboral > duracion_uni)

# ¿el nombre es Juan? 
me_llamo_juan = nombre == "Juan"
print(me_llamo_juan)
print(type(me_llamo_juan))

#¿Juan es mayor de edad y está pololeando?
print(edad > 18 and duracion_pololeo > 0)


#carrera de al menos 6 años o si tiene más de 5 años de experiencia 
print(duracion_uni >= 6 or exp_laboral > 5)


#si es que cumple un requisito: ser menor a 28 o tener menos de 3 años de experiencia laboral.
menor_28 = edad < 28 
exp_menor_3 = exp_laboral < 3
print(menor_28) #True
print(exp_menor_3) #False
print(menor_28 ^ exp_menor_3)
