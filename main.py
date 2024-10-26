import discord
import random
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
    elif message.content.startswith('$Recomendacion'):
        await message.channel.send((f'{random.choice(facts_list)}'))
    else:
        await message.channel.send(message.content)
facts_list = ["Ahorra energia para luchar contra el cambio climático.","Pon en práctica las 3 ‘R’ de la sostenibilidad", "Una dieta baja en carbono supone consumir de manera más inteligente y luchar contra el cambio climático.", "Otra de las acciones para luchar contra el cambio climático que puedes hacer es escoger una energía verde y promover la generación de energías renovables como la solar, eólica, hidráulica." ]
client.run("")
