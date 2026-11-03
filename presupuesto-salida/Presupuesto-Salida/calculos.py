def calcular_total(gastos):
    return sum(gastos)


def calcular_saldo(presupuesto, total):
    return presupuesto - total

def evaluar_saldo(saldo):
    if saldo >= 0:
        return "Dentro del presupuesto"
    return "Presupuesto excedido"