def matrixmult(A,B):
    """
    Calculate a product of two matrices.

    Parameters
    ----------
    A: list
        A list the elements of which are lists of the same length
    B: list
        A list the elements of which are lists of the same length

    Returns
    -------
    C: list
        The resulting matrix
    """

    nrowsa = len(A)
    ncolsb = len(B[0])

    nrowsb = len(B)
    ncolsa = len(A[0])

    ncolsinrowa = []

    for i in A:
        ncolsinrowa.append(len(i))
    if not all(i == ncolsinrowa[0] for i in ncolsinrowa):
        raise ValueError("Cannot multiply the two matrices A and B. Number of columns in A is not equal to the number of rows in B")
    
    ncolsinrowb = []

    for i in B:
        ncolsinrowb.append(len(i))
    if not all(i == ncolsinrowb[0] for i in ncolsinrowb):
        raise ValueError("Cannot multiply the two matrices A and B. Number of columns in A is not equal to the number of rows in B")

    C = [[0 for o in range(ncolsb)] for u in range(nrowsa)]
    if nrowsb != ncolsa:
        raise ValueError("Cannot multiply the two matrices A and B. Number of columns in A is not equal to the number of rows in B")

    #nrowsb = ncolsa

    for i in range(nrowsa):
        for j in range(ncolsb):
            for k in range(nrowsa):
                C[i][j] += A[i][k] * B[k][j]
    return C