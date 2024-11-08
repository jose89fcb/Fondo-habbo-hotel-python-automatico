# Habbo Hotel Fondo Bot

Este bot de Discord está diseñado para monitorear el fondo de la página de Habbo Hotel y enviarlo automáticamente a un canal de Discord cada vez que se detecte un cambio en la imagen del fondo.

## Características

- **Monitoreo constante**: El bot revisa la imagen del fondo de Habbo Hotel cada 30 segundos para detectar si ha cambiado.
- **Detección de cambios**: Si el fondo cambia, el bot envía un mensaje con la nueva imagen a un canal de Discord específico.
- **Evita spam**: El bot solo envía la imagen cuando detecta un cambio real en la imagen del fondo, evitando enviar la misma imagen repetidamente.
- **Configuración fácil**: Solo necesitas configurar el canal de Discord donde se enviará la imagen y proporcionar un token para el bot.

## ¿Cómo funciona?

1. El bot descarga los datos de la página de Habbo Hotel para obtener la URL del fondo.
2. Calcula el hash de la imagen actual.
3. Compara el hash de la nueva imagen con el que tiene guardado en su archivo local.
4. Si el hash es diferente (es decir, si la imagen cambió), el bot envía la nueva imagen a un canal de Discord y guarda el nuevo hash.
5. Si no hay cambios en la imagen, el bot no enviará nada, evitando así el spam.

## Requisitos

- Python 3.7 o superior
- Librerías: `discord.py`, `requests`, `Pillow`, `hashlib`
