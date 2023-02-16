def scalar_vector_product(scalar, vector) :
    return([scalar * vector for vector in vector])

print(scalar_vector_product(5, [1, 2, 3, 4]))