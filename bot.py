import discord
import maxroll_scrap

# TODO : Valorisation du token du bot à adapter en fonction de l'hébergement
token = open(".env", "r")
token = token.read()

# Instanciation liste des leaderboards surveillés
lboards = ['barbarian', 'monk','dh', 'wd', 'wizard','crusader', 'team-2', 'team-3', 'team-4']

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
    if message.content == "!dh":
        r = maxroll_scrap.get_single_lb()
        await message.channel.send(r)

# Exécution du bot
client.run(token)