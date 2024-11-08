import discord
from discord.ext import commands, tasks
from urllib.request import urlopen
from PIL import Image
import io
import requests
import hashlib
import json
from datetime import datetime

bot = commands.Bot(command_prefix='!', description="ayuda bot")  # Comando
bot.remove_command("help")  # Borra el comando por defecto !help

# Ruta donde guardamos el hash de la imagen
HASH_FILE = 'image_hash.json'

TOKEN = '' #Crea un token de bot en discord.dev

# ID del canal donde se enviará el mensaje
CHANNEL_ID = 1302983930923974707  # Reemplaza con el ID del canal

# Función para cargar el hash guardado desde el archivo
def load_saved_hash():
    try:
        with open(HASH_FILE, 'r') as file:
            data = json.load(file)
            return data.get('hash', None)
    except FileNotFoundError:
        return None

# Función para guardar el hash actual en el archivo
def save_hash_to_file(hash_value):
    with open(HASH_FILE, 'w') as file:
        json.dump({'hash': hash_value}, file)

# Función para obtener la imagen y calcular su hash
def get_image_and_hash():
    # Obtener los datos desde la URL
    data = urlopen("https://www.habbo.es/gamedata/external_variables/bdc1f0fb26a966d366ce784882eb9bfb450dbe75").read().decode('utf-8')
    
    # Buscar la línea que contiene la URL del fondo
    for linea in data.split('\n'):
        if linea.startswith("landing.view.background_left.uri") or linea.startswith("landing.view.background_left.uri"):
            k, fondohabbo = linea.split("=")

            # Descargar la imagen desde la URL
            image_data = requests.get(fondohabbo).content

            # Calcular el hash de la imagen
            image_hash = hashlib.sha256(image_data).hexdigest()

            return image_data, image_hash, fondohabbo

    return None, None, None

# Tarea que se ejecuta cada 30 segundos
@tasks.loop(seconds=30)
async def check_for_image_change():
    print("Verificando si hay un nuevo fondo...")  # Mensaje en consola para indicar que el bot está verificando
    
    channel = bot.get_channel(CHANNEL_ID)  # Obtener el canal por ID
    if not channel:
        print(f"Canal con ID {CHANNEL_ID} no encontrado.")
        return

    # Obtener la imagen y su hash
    image_data, current_hash, image_url = get_image_and_hash()

    if image_data is None:
        print("No se pudo obtener la imagen.")
        return

    # Cargar el hash guardado previamente
    saved_hash = load_saved_hash()

    # Si el hash ha cambiado, enviamos la nueva imagen
    if current_hash != saved_hash:
        print("Se ha detectado un nuevo fondo!")  # Mensaje en consola indicando que se detectó un nuevo fondo

        # Convertir los datos de la imagen a un archivo en memoria
        with io.BytesIO(image_data) as image_binary:
            image_binary.seek(0)

            # Crear el embed para enviar
            embed = discord.Embed(
                title="Fondo de Habbo Hotel", 
                description="Aquí está el nuevo fondo de Habbo Hotel.", 
                timestamp=datetime.utcnow(),
                color=discord.Colour.random()
            )
            
            embed.set_image(url="attachment://fondo_HabboHotel.png")  # Incrustar la imagen en el embed
            embed.set_footer(text="BOT Programado Por Jose89fcb")

            # Enviar el embed con la imagen como archivo adjunto
            await channel.send(embed=embed, file=discord.File(fp=image_binary, filename="fondo_HabboHotel.png"))

        # Guardar el nuevo hash de la imagen
        save_hash_to_file(current_hash)

@bot.event
async def on_ready():
    print("BOT listo!")
    check_for_image_change.start()  # Iniciar la tarea periódica

bot.run(TOKEN)  # Asegúrate de poner tu token de bot aquí
