def ordenar_elemento_medio(A: list) -> list:
    medio = A[(len(A) // 2) - 1] if len(A) % 2 == 0 else A[len(A) // 2]

    menores = []
    otros = []

    for elemento in A:
        if elemento < medio:
            menores.append(elemento)
        elif elemento != medio:
            otros.append(elemento)
    mitad = len(menores) // 2
    menoresAntes = menores[:mitad]
    menoresDespues = menores[mitad:]

    elementosAntes = len(A)//2 - 1 if len(A) % 2 == 0 else len(A)//2
    izq = menoresAntes + otros[:elementosAntes - len(menoresAntes)]
    der = menoresDespues + otros[elementosAntes - len(menoresAntes):]
    return izq + [medio] + der

if __name__ == "__main__":
    A = [9, 3, 8, 5, 4, 7, 2, 1]
    resultado = ordenar_elemento_medio(A)
    print(resultado)