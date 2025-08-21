# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 08:59:19 2024

@author: Julian David
"""

"""2. En una tienda de libros se ofrecen descuentos según la cantidad de libros que
 se compren. Si el cliente compra menos de 5 libros, no hay descuento. Si compra entre 5 y 10 
 libros, se aplica un descuento del 10%. Si compra más de 10 libros, se aplica un descuento
 del 20%. El programa debe determinar el valor total a pagar, dado el precio unitario de un
 libro y la cantidad de libros a comprar.
"""

valor_libro=13000

num_libros=int(input("Cuantos libros va a comprar?"))

precio_pagar=0


if (num_libros>5 and num_libros<10):
    precio_pagar=(num_libros*valor_libro)-(num_libros*valor_libro)*0.1 #descuento del 10
elif(num_libros>10):
    precio_pagar=(num_libros*valor_libro)-(num_libros*valor_libro)*0.2 #descuento del 20
else:
    precio_pagar=(num_libros*valor_libro)

print(f'El valor a pagar es de {precio_pagar}')
    
    
