import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hola!")
    if message.content.startswith('$Recomendacion1'):
        await message.channel.send("Ahorra energia para luchar contra el cambio climático")
    if message.content.startswith('$Recomendacion2'):
        await message.channel.send("Pon en práctica las 3 ‘R’ de la sostenibilidad")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)
client.run("")
