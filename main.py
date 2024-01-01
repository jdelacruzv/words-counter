# Counts the number of elements in a list.
def words_counter(final_list):
	counter = len(final_list)
	return print(f'Excelente, contaste tu pensamiento en {counter} palabras.')


# Splits the line of a text file into a list of words.
def split_row_list(file_handler):
	new_list = []
	for line in file_handler:
		words_list = line.split()
		new_list += words_list
	return new_list


def main():
	option = input('Ingrese la letra T=texto | A=Archivo: ').lower()
	if option == 't':
		text = input('¿Cuéntame en que estás pensando?, ingreso el texto: ')
		words = text.split()
		words_counter(words)
	else:
		file = input('¿Cuéntame en que estás pensando?, ingreso el archivo: ')
		try:
			file_handler = open(file)
			result = split_row_list(file_handler)
			words_counter(result)
		except:
			print('No se puede abrir el archivo:', file)
			exit()


main()