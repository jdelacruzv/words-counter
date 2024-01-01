thought = input('¿Cuéntame en que estás pensando?: ')

def words_counter():
	words = thought.split()
	counter = 0
	for word in words:
		counter += 1
	return counter

resul = words_counter()
print(f'Excelente, contaste tu pensamiento en {resul} palabras.')