# Agro UD

El sistema Agro UD opera el sensor de humedad en la tierra (sen0114) y el conversor de señales analogas a digitales (ADC) de la linea asd1x15 que opera con la libreria de adafruit para python [ASD1x15](https://github.com/adafruit/Adafruit_ADS1X15).
Ademas de esto a partir de la lectura del voltaje se hace una conversion para que la salida sea un porcentaje de humedad, y se encia a la plataforma Thing Speak

## Explicacion a detalle
A continuacion se muestra el montaje a detalle con una imagen.
<img src="https://i0.wp.com/henrysbench.capnfatz.com/wp-content/uploads/2015/09/Arduino-ADS1115-Simple-Tutorial-Hook-Up.png" />

El scrip trabaja el lenguaje python 2.7, el cual es iniciado por Thing Speak cada determindo tiempo y trasportado a la nube.
Para trabajar el sensor se requiere instalar la libreria asd1x15 que permitira hacer lectura del sensor.
La lectura del sensor es complementada por una ecuacion que convierte el voltaje recibido en un porcentaje de huedad

## Autores

Miguel Angle Vega Alonso
Edvard Frederick Bareño
Andres Felipe Gomez 
Wilmer Ricardo Pachon Lopez
