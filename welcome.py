import discord

intents = discord.Intents.default()
intents.members = True 
client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
    # Define el canal donde quieres enviar el mensaje de bienvenida
    canal = client.get_channel(ID DE CANAL)

    # Carga la imagen que deseas enviar
    with open('FOTO.png', 'rb') as f:
        imagen = discord.File(f)

    # Crea el mensaje de bienvenida con la imagen adjunta
    mensaje_bienvenida = f'¡Bienvenido {member.mention} al servidor de Discord! :tada: :confetti_ball:\n\n'
    mensaje_bienvenida += 'Esperamos que te sientas como en casa, no dudes en presentarte en el canal correspondiente y comenzar a conocer gente nueva.\n\n'
    mensaje_bienvenida += 'Recuerda revisar las normas del servidor antes de comenzar a participar.\n\n'
    mensaje_bienvenida += '¡Que tengas un excelente día!'

    await canal.send(mensaje_bienvenida, file=imagen)

client.run('TOKEN')
