# edad = int(input('¿Qué edad tienes? '))
# if 65 > edad >= 18:
#     print('Eres mayor de edad')
# elif edad < 0:
#     print('No has nacido')
# elif 65 < edad <= 90:
#     print('Estas viejo')
# elif edad > 91:
#     print('Uff, que viejo!')
# else:
#     print('Eres menor de edad')












# def validarPassword(password): #Acoplar funciones para hacer más fácil revisar, arreglar
#     if len(password) < 6:
#         print('Su contraseña debe contener al menos 6 caracteres')
#     elif password == '123456':
#         print('Este password es muy sencillo. Elija otro')
#     elif password == '654321':
#         print('Este password es muy sencillo. Elija otro')
#     elif ("'" in password) or ("*" in password) or ("-" in password):
#         print("No puede usar especial dentro de su password")
#     else:
#         print('Contraseña correcta')
# #Le pido la nueva contraseña la usuario
# password = input('Ingrese una contraseña: ')
# #Valido la contraseña con la función "validarPassword"
# validarPassword(password)











# import getpass

# def validarPassword(password): #Acoplar funciones para hacer más fácil revisar, arreglar
#     #Validamos que sea de largo al menos sea 6
#     if len(password) < 6:
#         print('Su contraseña debe contener al menos 6 caracteres')
#         return False
#     elif password == '12345678':
#         print('Este password es muy sencillo. Elija otro')
#         return False
#     elif password == '87654321':
#         print('Este password es muy sencillo. Elija otro')
#         return False
#     elif ("'" in password) or ("*" in password) or ("-" in password):
#         print("No puede usar especial dentro de su password")
#         return False
#     else:
#         print('Contraseña correcta')
#         return True