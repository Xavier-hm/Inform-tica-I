# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 15:36:57 2024

@author: Julian David
"""
"""En una tienda de libros se ofrecen descuentos según la cantidad de libros que se compren.
 Si el cliente compra menos de 5 libros, no hay descuento. Si compra entre 5 y 10 libros,
 se aplica un descuento del 10%. Si compra más de 10 libros, se aplica un descuento del 20%. 
 El programa debe determinar el valor total a pagar, dado el precio unitario de un libro y la
 cantidad de libros a comprar."""
 
 
#Ingreso de datos de la compra 
input_ok=0


p_book=input("¿Cual es el precio del libro?")
p_book=float(p_book)

n_books=input("¿Cuantos unidades se van a comprar?")
n_books=int(n_books)


#Calcular precio de la compra
precio_final=(p_book*n_books)

if n_books>10:
    precio_final= precio_final-(p_book*n_books*0.2)
elif n_books>5:
        precio_final= precio_final-(p_book*n_books*0.1)

        
print("El valor a pagar es de ",precio_final)

 