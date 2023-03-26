import discord
import asyncio
import datetime
import colorama
from colorama import Fore, Style

intents = discord.Intents.default()
intents.members = True 
client = discord.Client(intents=intents)

@client.event
async def on_ready():

    print(Fore.GREEN + '==============================================')
    print('¡El bot de bienvenida está en línea!')
    print('Conectado como:', Fore.YELLOW + client.user.name, '#' + client.user.discriminator)
    print('ID del bot:', Fore.YELLOW + str(client.user.id))
    print('Hora de inicio del BOT:', Fore.CYAN + datetime.datetime.now().strftime('%H:%M:%S'))
    print(Fore.GREEN + '==============================================')
    print(Style.RESET_ALL)

@client.event
async def on_member_join(member):
    # Define el canal donde quieres enviar el mensaje de bienvenida
    canal = client.get_channel(ID DE CANAL)

    # Carga la imagen que deseas enviar
    with open('IMAGE.png', 'rb') as f:
        imagen = discord.File(f)

    # Define el mensaje de bienvenida en formato embed
    embed = discord.Embed(title=f'¡Bienvenido {member.name}!', description='Esperamos que te sientas como en casa.', color=0x00ff00)
    embed.set_thumbnail(url=member.avatar.url)
    embed.add_field(name='Normas del servidor', value='Por favor, asegúrate de leer las normas del servidor antes de comenzar a participar.')
    embed.set_footer(text='¡Que tengas un excelente día!')

    # Asignar un rango al nuevo miembro
    role = discord.utils.get(member.guild.roles, name="NOMBRE DE ROL")
    await member.add_roles(role)

    await canal.send(file=imagen, embed=embed)

@client.event
async def on_member_remove(member):
    # Define el canal donde quieres enviar el mensaje de despedida
    canal = client.get_channel(ID DE CANAL)

    # Carga la imagen que deseas enviar
    with open('IMAGE.png', 'rb') as f:
        imagen = discord.File(f)

    # Define el mensaje de despedida en formato embed
    embed = discord.Embed(title=f'¡{member.name} ha abandonado el servidor!', description='¡Esperamos verte pronto de nuevo!', color=0xff0000)
    embed.set_thumbnail(url=member.avatar.url)

    await canal.send(file=imagen, embed=embed)

client.run('BOT TOKEN')
