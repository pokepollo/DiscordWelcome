import discord

intents = discord.Intents.default()
intents.members = True 
client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):

    # Id del canal donde quieres enviar el mensaje de bienvenida
    canal = client.get_channel(ID DEL CANAL)

    # Mensaje de bienvenida
    mensaje_bienvenida = f'Bienvenido {member.mention} al servidor de Discord!'

    # Envía el mensaje al canal de bienvenida
    await canal.send(mensaje_bienvenida)
client.run('TOKEN')