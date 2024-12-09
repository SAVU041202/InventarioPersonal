def calcular_aguinaldo_proporcional(dias_trabajados, salario_diario):
    """
    Calcula el aguinaldo proporcional.
    
    :param dias_trabajados: Número de días trabajados durante el año.
    :param salario_diario: Salario diario del trabajador.
    :return: Aguinaldo proporcional.
    """
    # Días de aguinaldo completos por ley (puedes ajustar este valor según tu país)
    dias_de_aguinaldo_por_año = 15

    # Calcula el aguinaldo proporcional
    aguinaldo_proporcional = (dias_trabajados / 365) * (dias_de_aguinaldo_por_año * salario_diario)

    return round(aguinaldo_proporcional, 2)


# Ejemplo de uso
try:
    dias_trabajados = int(input("Ingrese el número de días trabajados: "))
    salario_diario = float(input("Ingrese el salario diario: "))

    if dias_trabajados < 0 or dias_trabajados > 365:
        print("El número de días trabajados debe estar entre 0 y 365.")
    elif salario_diario <= 0:
        print("El salario diario debe ser un número positivo.")
    else:
        aguinaldo = calcular_aguinaldo_proporcional(dias_trabajados, salario_diario)
        print(f"El aguinaldo proporcional es: ${aguinaldo}")
except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")
