import discord
from discord.ext import commands
import random

# Configuración del bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Listas de tips y retos
facts_list = [
    "Ahorra energía para luchar contra el cambio climático.",
    "Pon en práctica las 3 ‘R’ de la sostenibilidad",
    "Una dieta baja en carbono supone consumir de manera más inteligente y luchar contra el cambio climático.",
    "Escoge una energía verde y promueve la generación de energías renovables como la solar, eólica, hidráulica.",
    "Separa la basura en los diferentes contenedores para ayudar a la Economía Circular.",
    "Apaga las luces cuando no las necesites para ayudar a combatir el Cambio Climático.",
    "Movilidad Sostenible: Utiliza transporte público o bicicleta antes que el coche siempre que sea posible.",
]

eco_retos = [
    "🧴 Reduce el uso de plásticos desechables: intenta llevar tu propia botella reutilizable esta semana.",
    "💡 Ahorra energía: apaga las luces y desconecta los dispositivos cuando no los estés usando.",
    "🌱 Planta algo: ya sea una semilla en una maceta o en tu jardín, ¡cada planta cuenta!",
    "♻️ Haz una limpieza ecológica: separa tu basura y recicla todo lo que puedas.",
    "🚶 Usa transporte sostenible: intenta caminar, ir en bicicleta o usar transporte público para tus desplazamientos.",
    "🍃 Compra local: apoya los mercados locales y reduce tu huella de carbono evitando productos importados.",
    "👕 Ahorra agua: acorta el tiempo de tus duchas esta semana para reducir el consumo de agua.",
    "📱 Reduce tu tiempo en pantallas: ahorrarás energía y ayudarás al planeta.",
    "🛒 Lleva tu propia bolsa de tela cuando vayas de compras y evita usar bolsas plásticas.",
    "🍎 Come una comida sin carne: intenta al menos un día vegetariano para reducir tu impacto ambiental.",
]

# Evento de mensajes
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower().startswith("hola"):
        await message.channel.send("Hola, soy EcoBot y estoy aquí para ayudarte a cuidar nuestro planeta.")
    elif message.content.lower().startswith("!ecotip"):
        await message.channel.send(random.choice(facts_list))
    elif message.content.lower().startswith("!ecoreto"):
        await message.channel.send(random.choice(eco_retos))
    
    # Permite que otros comandos procesen los mensajes
    await bot.process_commands(message)

# Comando de la calculadora de huella de carbono
@bot.command()
async def eco_calculadora(ctx):
    await ctx.send("🌍 ¡Hola! Vamos a calcular tu huella de carbono con unas preguntas rápidas.")

    # Pregunta 1: Transporte
    await ctx.send("🚗 ¿Cuántos kilómetros viajas en coche cada semana? (Escribe solo el número)")
    try:
        transporte_km = await bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30.0)
        km_semanales = int(transporte_km.content)
    except ValueError:
        await ctx.send("Por favor, ingresa un número válido para los kilómetros.")
        return
    except TimeoutError:
        await ctx.send("Tiempo de espera agotado. Intenta de nuevo con `!eco_calculadora`.")
        return

    # Pregunta 2: Electricidad
    await ctx.send("💡 ¿Cuántos kWh de electricidad consumes al mes? (Escribe solo el número)")
    try:
        electricidad_kwh = await bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30.0)
        kwh_mensuales = int(electricidad_kwh.content)
    except ValueError:
        await ctx.send("Por favor, ingresa un número válido para el consumo eléctrico.")
        return
    except TimeoutError:
        await ctx.send("Tiempo de espera agotado. Intenta de nuevo con `!eco_calculadora`.")
        return

    # Pregunta 3: Carne
    await ctx.send("🥩 ¿Cuántas veces a la semana comes carne? (Escribe solo el número)")
    try:
        carne_semanal = await bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30.0)
        carne_veces = int(carne_semanal.content)
    except ValueError:
        await ctx.send("Por favor, ingresa un número válido para la cantidad de carne.")
        return
    except TimeoutError:
        await ctx.send("Tiempo de espera agotado. Intenta de nuevo con `!eco_calculadora`.")
        return

    # Cálculo simple de huella de carbono (estimación)
    transporte_huella = km_semanales * 0.21  # kg CO2 por km de coche
    electricidad_huella = kwh_mensuales * 0.475  # kg CO2 por kWh promedio
    carne_huella = carne_veces * 5.7  # kg CO2 por porción de carne promedio

    # Suma total
    huella_total = transporte_huella + electricidad_huella + carne_huella

    # Respuesta final
    await ctx.send(
        f"🌱 Tu huella de carbono estimada es de aproximadamente {huella_total:.2f} kg de CO2 al mes.\n"
        "Recuerda que reducir el uso de transporte, ahorrar electricidad, y consumir menos carne puede ayudar a disminuir esta cifra. ¡Cada acción cuenta! 💪🌍"
    )

# Evento de inicio del bot
@bot.event
async def on_ready():
    print(f"{bot.user} está listo para ayudar al planeta 🌎")

bot.run("")
