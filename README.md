# Fondo Habbo Hotel Bot

Este es un bot de Discord diseñado para monitorear el fondo del sitio web de **Habbo Hotel** y enviar una notificación con la nueva imagen cuando haya un cambio en el fondo. El bot monitorea constantemente el fondo de la página y, si detecta que la imagen ha cambiado, la envía automáticamente a un canal de Discord.

## Características

- **Monitoreo de fondo**: Revisa el fondo de Habbo Hotel cada 30 segundos.
- **Detección de cambios**: Si el fondo cambia, el bot envía automáticamente la nueva imagen al canal de Discord.
- **Evita el spam**: Solo envía la imagen cuando detecta un cambio real en el fondo.
- **Configuración sencilla**: Solo necesitas configurar el token de tu bot y el ID del canal de Discord donde deseas recibir las imágenes.

## Requisitos

Antes de ejecutar el bot, asegúrate de tener lo siguiente:

- **Python 3.7.0 o superior**: Puedes descargar Python desde [aquí](https://www.python.org/downloads/release/python-370/).
  
- **Librerías necesarias**: Puedes instalar todas las dependencias necesarias utilizando el archivo `requirements.txt`. Las principales librerías son:

  - `discord.py`: Librería para interactuar con la API de Discord.
  - `requests`: Librería para realizar solicitudes HTTP (usada para descargar la imagen).
  - `Pillow`: Librería para manejar y procesar imágenes.

  Las librerías se instalan automáticamente desde el archivo `requirements.txt`.

## Instalación

### Paso 1: Clona este repositorio

Clona este repositorio en tu máquina local con el siguiente comando:

```bash
git clone https://github.com/jose89fcb/Fondo-habbo-hotel-python-automatico.git
cd Fondo-habbo-hotel-python-automatico
