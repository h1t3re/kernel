def generateur_recurrent_d_espace(unité_de_dimension, coordonné, dimension):
    for x in unité_de_dimension:
        if len(coordonné)+1 < dimension:
            for y in generateur_recurrent_d_espace(unité_de_dimension, coordonné + str(x), dimension):
                yield y
        elif len(coordonné)+1 == dimension:
            yield coordonné + str(x)

def generateur_recurrent_d_espace_infini():
	i = 0
	while True:
		i = i + 1
		for x in generateur_recurrent_d_espace([x for x in range(1, i)],  "", i):
			yield x