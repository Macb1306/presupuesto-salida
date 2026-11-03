from calculos import calcular_total, calcular_saldo
from calculos import evaluar_saldo

assert calcular_total([1200, 3500, 1800]) == 6500
assert calcular_total([]) == 0
assert calcular_saldo(8000, 6500) == 1500
assert calcular_saldo(8000, 8500) == -500
assert evaluar_saldo(0) == "Dentro del presupuesto"
assert evaluar_saldo(-500) == "Presupuesto excedido"

print("6 pruebas correctas")
