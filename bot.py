import discord
import maxroll_scrap

# TODO : Valorisation du token du bot à adapter en fonction de l'hébergement
token = open(".env", "r")
token = token.read()

# TODO : Personnalisation du client en mode objet
client = discord.Client()

# Feedback bot en ligne
@client.event
async def on_ready():
    print(">> Bot prêt à l'écoute <<")

# Fonction d'écoute de mot clef
@client.event
async def on_message(message):
    print(f"Commande reçue : '{message.content}'")
    if message.content == "!test":
        r = maxroll_scrap.test(message.content)
        await message.channel.send(r)

# Exécution du bot
client.run(token)