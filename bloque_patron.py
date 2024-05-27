def find_best_combinations(blocks, target,tol_greater,tol_smaller, start=0, path=[], best_path_greater=[], best_path_smaller=[], best_diff_greater=float('inf'), best_diff_smaller=float('inf')):
    # Calcular la suma actual del camino
    current_sum = sum(path)
    # Calcular la diferencia actual con el objetivo
    current_diff = abs(target - current_sum)
    
    # Si la diferencia actual es mejor (menor), actualizar el mejor camino y la mejor diferencia
    if current_sum >= target:
        if current_diff < best_diff_greater:
            best_path_greater = path
            best_diff_greater = current_diff
    else:
        if current_diff < best_diff_smaller:
            best_path_smaller = path
            best_diff_smaller = current_diff
    # Si la diferencia cumple la tolerancia para no hacer mas calculos de mas
    if best_diff_greater<tol_greater and best_diff_smaller<tol_smaller:
         return best_path_greater, best_path_smaller, best_diff_greater, best_diff_smaller
    # Si la suma actual es mayor o igual al objetivo, no continuar la búsqueda desde aquí
    if current_sum >= target:
        return best_path_greater, best_path_smaller, best_diff_greater, best_diff_smaller
    
    # Recorrer los bloques desde el índice de inicio
    for i in range(start, len(blocks)):
        # Llamar recursivamente con el bloque actual añadido al camino
        best_path_greater, best_path_smaller, best_diff_greater, best_diff_smaller = find_best_combinations(blocks, target,tol_greater,tol_smaller, i + 1, path + [blocks[i]], best_path_greater, best_path_smaller, best_diff_greater, best_diff_smaller)
    
    return best_path_greater, best_path_smaller, best_diff_greater, best_diff_smaller

# Definir los tamaños de los bloques
blocks = [0.1,0.101,0.1002,0.1003,0.1004,0.1005,0.1006,0.1007,0.1008,0.1009,0.05,0.101,0.102,0.103,0.104,0.105,0.106,0.107,0.108,0.109,0.11,0.111,0.112,0.113,0.114,0.115,0.116,0.118,0.119,0.12,0.121,0.122,0.123,0.124,0.125,
          0.126,0.127,0.128,0.129,0.130,0.131,0.132,0.133,0.134,0.135,0.136,0.137,0.138,0.139,0.140,0.141,0.142,0.143,0.144,0.145,0.146,0.147,0.148,0.149,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,
          0.85,0.90,0.95,1,2,3,4]
#blocks = [25.4 * x for x in blocks]

# Definir el tamaño objetivo
target_size = 10.53
target_size = target_size/25.4

# Tolerancia de busqueda
tol_greater = 0.002
tol_smaller = 0.002
# Encontrar las mejores combinaciones
tol_greater = tol_greater/25.4
tol_smaller = tol_smaller/25.4
best_path_greater, best_path_smaller, best_diff_greater, best_diff_smaller = find_best_combinations(blocks, target_size,tol_greater,tol_smaller)

# Sumar los valores de las mejores combinaciones
best_sum_greater = sum(best_path_greater)
best_sum_smaller = sum(best_path_smaller)

best_path_greater =  [round(x,5) for x in best_path_greater]
best_path_smaller = [round(x,5) for x in best_path_smaller]

# Mostrar el resultado
print("Mejor combinación mayor al objetivo:", best_path_greater)
print("Suma de la mejor combinación mayor al objetivo:", 25.4*best_sum_greater)
print("Diferencia con el objetivo:", 25.4*best_diff_greater)

print("\nMejor combinación menor al objetivo:", best_path_smaller)
print("Suma de la mejor combinación menor al objetivo:", 25.4*best_sum_smaller)
print("Diferencia con el objetivo:", 25.4*best_diff_smaller)

