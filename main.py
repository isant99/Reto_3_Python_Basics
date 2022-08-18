#Billetes:
Billete5e, Billete10e, Billete20e, Billete50e, Billete100e, Billete200e, Billete500e = 5, 10, 20, 50, 100, 200, 500
billetes = [Billete500e, Billete200e, Billete100e, Billete50e, Billete20e, Billete10e, Billete5e]

#Monedas:
Moneda50cent, Moneda1e, Moneda2e = 0.5, 1, 2
monedas = [Moneda2e, Moneda1e, Moneda50cent]

precio_total = 0
menu = ['Patatas fritas', 'Patatas bravas', 'Aros de cebolla', 'Palitos de queso', 'Pizza Margarita',\
        'Pizza 4 quesos', 'Empanadillas', 'Bocadillo de pimientos', 'Bocadillo de tomate y queso']
precios = [12, 13, 12.5, 13.5, 36, 36.5, 15, 24, 24.5]
menudict = dict(zip(menu,precios))

print('Bienvenido al restaurante de comida rapida mas caro del mundo.', '\n', 'Aqui tiene la carta:')
for key, value in menudict.items():
        print(key, '------', value, '€')

order = []
order.append(input('¿Que desea? (Respete mayusculas y minusculas) '))
while True:
        more = input('¿Algo mas? Pulse 0 para no, 1 para si ')
        try:
                more = int(more)
                if more == 1:
                        order.append(input('¿Que mas desea? '))
                elif more == 0:
                        break
                else:
                        print('No le he entendido')
        except ValueError:
                print('No le he entendido')

for i in order:
        if i in menudict.keys():
                precio_total = precio_total + menudict[i]
        else:
                print('Lo siento, no tenemos', i)

print('El precio de su pedido es:', precio_total, '€')

pago = []
veces = []
for j in billetes:
        bill = int(precio_total//j)
        if bill != 0:
                pago.append(j)
                veces.append(bill)
                precio_total = precio_total - bill*j
for k in monedas:
        mon = int(precio_total//k)
        if mon != 0:
                pago.append(k)
                veces.append(mon)
                precio_total = precio_total - mon*k

print('Tiene que entregar:')
for l in range(len(pago)):
        print(pago[l], '€ x' ,veces[l])



