#Funciones de diccionarios
persona = {
    'nombres' : 'Saira Yamileth',
    'apellidos' : 'Pérez González'
}

print(persona.get ('nombres'))
print(persona['apellidos'])

claves = ('nota1', 'nota2', 'nota3')
notas = dict.fromkeys(claves)
print(notas.get('nota4'))

print(persona.items())
print(persona.values())
print(persona.keys())

#Borrar el apellido del diccionario personas
persona.pop('apellidos')
print(persona)
persona.popitem()
print(persona)

#Agregar un nuevo elemento o actualizarlo si existe
persona.setdefault('edad' , 20)
print(persona)

persona.setdefault(nombre = 'Virginia Sofia')
print(persona)

print("Total de elementos {0} ".format(len(persona)))

del persona ['edad']