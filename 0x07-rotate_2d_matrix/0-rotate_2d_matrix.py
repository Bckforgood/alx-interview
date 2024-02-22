#!/usr/bin/python3


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise
    """
    n = len(matrix)
    # Transpose de la matrice
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Inversion des colonnes pour la rotation de 90 degrés
    for row in matrix:
        row.reverse()
