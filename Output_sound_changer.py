#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Output:
# Al ejecutar:
# 1. Se revisará qué dispositivo está por defecto.
# 2. Se colocará el dispositivo siguiente al que estaba por defecto.
# 3. Se notificará qué dispositivo se puso por defecto.

import os

# Variables
headphones = "analog-output-headphones"
speaker = "analog-output-lineout"

def dispositivo_por_defecto():
    stream = os.popen("pactl list sinks |grep -E 'Puerto Activo'") # Cambiar <Puerto Activo> por <active port> en caso de que el sistema esté en inglés.
    output = stream.read().strip()
    return output

def run():
    dipositivo_actual = dispositivo_por_defecto()
    #print(output)
    if headphones in dipositivo_actual:
        os.system("pactl set-sink-port 0 "+speaker)
    else:
        os.system("pactl set-sink-port 0 "+headphones)

    # Confirmar qué dispositivo está por defecto
    nuevo_dispositivo = dispositivo_por_defecto()
    if headphones in nuevo_dispositivo:
        nuevo_dispositivo = "Audífonos"
    elif speaker in nuevo_dispositivo:
        nuevo_dispositivo = "Bocinas"

    notificacion = "Dispositivo "+nuevo_dispositivo+" puesto por defecto."
    print(notificacion)
    os.system("notify-send '"+notificacion+"'")


if __name__ == "__main__":
    run()
