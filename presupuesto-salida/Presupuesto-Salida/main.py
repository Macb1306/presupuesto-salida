from datos import gastos, presupuesto
from calculos import calcular_total, calcular_saldo

total = calcular_total(gastos)
saldo = calcular_saldo(presupuesto, total)

print(f"Total de gastos: {total} pesos")
print(f"Saldo disponible: {saldo} pesos")