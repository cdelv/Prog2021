vendidos = ["Espresso", "Espresso", "Latte","Cappuccino", "Mocha", "Espresso", "Latte"]


def contar_vendidos(lista, item="Espresso"):
       n = lista.count(item)
       print("{} {}s vendidos.".format(n, item))

contar_vendidos(vendidos)