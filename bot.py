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
    cmd = message.content
    if cmd[0] == "!":
        cmd = cmd[1:]

        # Classement saison en cours /lboard
        if cmd in lboards:
            if 'team' in cmd:
                r = maxroll_scrap.get_teams(cmd)
            else:
                r = maxroll_scrap.get_single_class(cmd)
            await message.channel.send(r)

        # Liste des commandes
        if cmd == "help":
            r = f"**Usage :**\n"
            r = r + f"```" + "!classement --saison --soft" + "```"
            r = r + f"*classements* : {str(lboards)}\n"
            r = r + f"\n **Option** *--saison* : s1 à s{str(maxroll_scrap.get_current_season())}. Facultatif, saison en cours par défaut."
            r = r + f"\n **Option** *--soft* : retourne les classements softcore. Facultatif, classements hardcore par défaut.\n"
            r = r + f"\n Exemples :"
            r = r + f"```!dh```"
            r = r + f"```!team-4```"
            r = r + f"```!crusader --s13```"

            await message.channel.send(r)

# Exécution du bot
client.run(token)