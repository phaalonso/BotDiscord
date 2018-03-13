import discord
import random
import Secreto
import builds

TOKEN = Secreto.seu_token()  # linkagem do token

client = discord.Client()
RhinoT = builds.Rhino(True)
RhinoF = builds.Rhino(False)


@client.event
async def on_ready():
    print('Bot ONLINE - Olá Mundo!')
    print(client.user.name)
    print(client.user.id)
    print('-----------------------')
    await client.change_presence(game=discord.Game(name='Online'))


@client.event
async def on_message(message):  # Resposta ao usuário
    if message.content.lower().startswith("!test"):
        await client.send_message(message.channel, "Ola Mundo, estou vivo!")

    elif message.content == "cookie":  # Resposta ao usuário atráves de emoticon
        await client.send_message(message.channel, ":cookie:")

    elif message.content.lower().startswith("!moeda"):  # Cara ou coroa 50,50%
        choice = random.randint(1, 2)
        if choice == 1:
            await client.add_reaction(message, '😀')
        elif choice == 2:
            await client.add_reaction(message, '👑')

    elif str(message.content).startswith('!build'):
        segunda=str(message.content).split()[1]
        '''if segunda == 'Teste':
            await client.send_message(message.channel,'OI')
            print('daijwi')'''

        builds = [('Rhino', 'link1','descri1'), ('Loki', 'link2','descri2'), ('Banshee', 'link3','descri3'), ('Vauban', 'link4','descri4')]
        for i in builds:
          if i[0]==segunda:
                await client.send_message(message.channel,i[1] )
                await client.send_message(message.channel, i[2])


'''
    elif message.content == "!build Rhino":
        await client.send_message(message.channel, RhinoT)
        await client.send_message(message.channel, RhinoF)
'''

client.run(TOKEN)

# print(TesteA)
