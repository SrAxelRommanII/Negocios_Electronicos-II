

inventario = 10


pronostico = [25, 30, 20, 35, 25]


demanda_real = [30, 25, 40, 30, 20]


produccion = pronostico.copy()

print(f"{'Día':<4} | {'Inv. Inicial':<12} | {'Producción':<10} | {'Disponible':<10} | {'Dem. Real':<10} | {'Atendida':<8} | {'Faltante':<8} | {'Inv. Final (Sobrante)':<22}")
print("-" * 100)

for dia in range(5):
    inv_inicial = inventario
    prod = produccion[dia]
    dem = demanda_real[dia]

    
    inventario_disponible = inv_inicial + prod

    
    if inventario_disponible >= dem:
        atendida = dem
        faltante = 0
        inventario = inventario_disponible - dem
    else:
        atendida = inventario_disponible
        faltante = dem - inventario_disponible
        inventario = 0  
        
    print(f"{dia+1:<4} | {inv_inicial:<12} | {prod:<10} | {inventario_disponible:<10} | {dem:<10} | {atendida:<8} | {faltante:<8} | {inventario:<22}")