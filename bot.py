import discord
import maxroll_scrap
import re

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
    print(f"Message reçu : '{message.content}'")
    cmd = message.content
    # Si le message posté ne commence pas par un '!' c'est pas une commande
    if cmd[0] == "!":
        cmd = cmd[1:]

        ### Commandes classements BriTs
        # vérif présence d'options
        if " " in cmd:
            cmd = cmd.split(" ")
            # contrôle de validité du radical de la commande
            if cmd[0] in lboards:
                # identification des options
                for arg in cmd:
                    if arg == "--soft":
                        mode = arg
                    # si saisie multiple d'option num saison, seule la première est lue 
                    if re.search("^--\d\d$", arg) and not 'season' in locals():
                        season = re.sub('-', '', arg)
                # valorisation des appels scrap en fonction des options trouvées

        # Si un seul param, alors uniquement type ladder (sinon cmd invalide sans feedback user)
        else:
            if cmd in lboards:
                if 'team' in cmd:
                    r = maxroll_scrap.get_teams(cmd,'','')
                else:
                    r = maxroll_scrap.get_single_class(cmd,'','')
        
        # Liste des commandes
        if cmd == "help":
            r = f"**Usage : classements BriTs**\n"
            r = r + f"```" + "!classement --saison --soft" + "```"
            r = r + f"__Classements__ : {str(lboards)}\n"
            r = r + f"\n **Option** *--numéro de saison* : 1 à {str(maxroll_scrap.get_current_season())}. Facultatif, saison en cours par défaut."
            r = r + f"\n **Option** *--soft* : retourne les classements softcore. Facultatif, classements hardcore par défaut.\n"
            r = r + f"Exemples :"
            r = r + f"```!dh```"
            r = r + f"```!team-4```"
            r = r + f"```!crusader --13```"
            r = r + "\n**Usage : classements par BattleTag**\n<*Coming soon*>"
    if r : await message.channel.send(r)

# Exécution du bot
client.run(token)