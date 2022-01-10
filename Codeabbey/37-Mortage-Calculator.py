def mortgage_calculator():
    data = input().split()
    p = prestamo = int(data[0])
    i = intereses = (int(data[1]) / 100.0) / 12
    n = meses = int(data[2])

    pago_mensual = p*(i*(1+i)**n)/((1+i)**n-1)
    print(round(pago_mensual))
mortgage_calculator()