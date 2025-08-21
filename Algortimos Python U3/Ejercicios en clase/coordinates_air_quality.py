# Pida al usuario la ubicación de una persona, la cantidad de estaciones
# de calidad del aire y luego pida la ubicacion y lectura del sensor
# de todas las estaciones. Al terminar, imprima cuál es la lectura de 
# calidad del aire en la estación más cercana.

cords = input("Ingrese las coordenadas X, Y (separadas solo por una coma) de la ubicación de la persona: ")

for i in range(0,len(cords)):
    if cords[i] == ",":
        break

coma_pos = i

ub_persona_x = float(cords[0:coma_pos])
ub_persona_y = float(cords[coma_pos+1:])

cant_est = int(input("Ingrese la cantidad de estaciones: "))

dist_min = 50000

for e in range(cant_est):
    ub_est_x = float(input(""))
    ub_est_y = float(input(""))
    sensor = input("")
    dist = ((ub_est_y - ub_est_x)**2 + (ub_est_y - ub_persona_y)**2)**0.5
    if dist < dist_min:
        dist_min = dist    
        sensor_sel = sensor

print("La calidad del aire aqui es: ", sensor_sel)

