# Agro UD

El sistema Agro UD esta pensado para optimizar la trata de cultivos urbanos y de esta manera mejorar la calidad del aire en la ciudad 

## Requisitos para ejecutar

Los elementos que se utilizaron en el desarrollo del proyecto, estan basados en plataformas open source, con esto encontramos sensores de humedad del suelo(sen0114), humedad del aire(dht11), temperatura ambiente(dht11) y sensor de luz uv(GUVA analog uv) y por supuesto la plataforma principal desde donde son enlazados dichos sensores que es Raspberry pi 3, sin embargo cualquier version de la misma, es capaz de soportar la implementacion desarrollada en el transcurso de la jornada, python es el lenguaje usado, debido a su versatilidad y facilidad de implementacion

### Prerequisitos

Por supuesto es necesario tener el sistema operativo de raspberry montado sobre la misma, ademas de ello una conexion estable con internet y por supuesto python para poder ejecutar los correspondientes scripts de cada sensor

### Desarrollo del proyecto

Durante el proceso se empieza enlazando con la unidad de raspberry todos los sensores que se querian tratar, una vez logrado ello, se procede a enviar los datos a la plataforma de IoT con el fin de poder tener accesos a ellos en cualquier momento, ademas que la plataforma ofrece algunas herramientas adicionales para analisis de datos, una vez realizado este enlace de forma 
correcta, se desarrollo un bot que permitiera acceder desde el movil a los datos tomados en tiempo real

###Visualizacion
Para la visualizacion de los datos tomados podemos acceder a los canales publicos establecidos https://thingspeak.com/channels/454552 correspondiente a los datos tomados de la humedad del suelo 
https://thingspeak.com/channels/484072 correspondiente a los datos tomados de el resto desensores como lo son la humedad del aire, temperatura del aire y ademas la luz uv incidente en el ambiente.


## Autores

Miguel Angle Vega Alonso
Edvard Frederick Bareño
Andres Felipe Gomez 
Wilmer Ricardo Pachon Lopez



## Agradecimientos

Grupo de investigacion GIIRA
Carlos Montenegro
Paolo alonso Gaona

