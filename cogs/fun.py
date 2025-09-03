import random
import discord
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.hangman_games = {}  # {channel_id: {"word": str, "guessed": set, "tries": int}}

        # Représentation ASCII du pendu
        self.hangman_stages = [
            "😀\n-----",
            "😀\n | \n-----",
            "😀\n/| \n-----",
            "😀\n/|\\ \n-----",
            "😀\n/|\\ \n / \n-----",
            "😀\n/|\\ \n/ \\ \n💀 DERNIÈRE CHANCE !",
            "💀\n/|\\\n/ \\ \nGAME OVER"
        ]

    # ----------------------------
    # 🎲 Commandes Fun / Jeux
    # ----------------------------
    @commands.hybrid_command(name="dice", description="Lance un dé à 6 faces 🎲")
    async def dice(self, ctx):
        result = random.randint(1, 6)
        await ctx.reply(f"🎲 Tu as obtenu **{result}** !")

    @commands.hybrid_command(name="roll", description="Lance un dé avec X faces 🎲")
    async def roll(self, ctx, faces: int = 20):
        result = random.randint(1, faces)
        await ctx.reply(f"🎲 Dé {faces} → **{result}**")

    @commands.hybrid_command(name="8ball", description="Pose une question à la boule magique 🔮")
    async def eight_ball(self, ctx, *, question: str):
        responses = [
            "Oui ✅", "Non ❌", "Peut-être 🤔", "Jamais 😈",
            "Repose plus tard ⏳", "Absolument 🔥", "J'en doute 😬"
        ]
        await ctx.reply(f"🔮 Question : **{question}**\nRéponse : {random.choice(responses)}")

    @commands.hybrid_command(name="coinflip", description="Pile ou face 🪙")
    async def coinflip(self, ctx):
        choice = random.choice(["Pile 🪙", "Face 🪙"])
        await ctx.reply(f"Résultat : **{choice}**")

    @commands.hybrid_command(name="meme", description="Envoie un meme aléatoire 😂")
    async def meme(self, ctx):
        memes = [
            "https://i.imgflip.com/30b1gx.jpg",
            "https://i.imgflip.com/1bij.jpg",
            "https://i.imgflip.com/26am.jpg",
            "https://i.imgflip.com/4/1otk96.jpg"
        ]
        await ctx.send(random.choice(memes))

    @commands.hybrid_command(name="gif", description="Envoie un gif aléatoire 🔥")
    async def gif(self, ctx):
        gifs = [
            "https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif",
            "https://media.giphy.com/media/26Fxy3Iz1ari8oytO/giphy.gif",
            "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif"
        ]
        await ctx.send(random.choice(gifs))

    @commands.hybrid_command(name="cat", description="Photo de chat mignon 🐱")
    async def cat(self, ctx):
        cats = [
            "https://cataas.com/cat",
            "https://placekitten.com/400/400",
            "https://cdn2.thecatapi.com/images/MTY3ODIyMQ.jpg"
        ]
        await ctx.send(random.choice(cats))

    @commands.hybrid_command(name="dog", description="Photo de chien mignon 🐶")
    async def dog(self, ctx):
        dogs = [
            "https://placedog.net/400/400",
            "https://cdn2.thedogapi.com/images/BJa4kxc4X.jpg",
            "https://cdn2.thedogapi.com/images/HJ7Pzg5EQ.jpg"
        ]
        await ctx.send(random.choice(dogs))

    @commands.hybrid_command(name="joke", description="Raconte une blague 🤣")
    async def joke(self, ctx):
        jokes = [
            "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent dans le bateau.",
            "Quel est le comble pour un électricien ? De ne pas être au courant ⚡",
            "Pourquoi les squelettes ne se battent-ils jamais entre eux ? Parce qu’ils n’ont pas les tripes."
        ]
        await ctx.send(random.choice(jokes))

    @commands.hybrid_command(name="rps", description="Pierre-papier-ciseaux ✊✋✌️")
    async def rps(self, ctx, choix: str):
        options = ["pierre", "papier", "ciseaux"]
        bot_choice = random.choice(options)
        choix = choix.lower()

        if choix not in options:
            return await ctx.send("❌ Choisis entre `pierre`, `papier`, ou `ciseaux`.")

        result = ""
        if choix == bot_choice:
            result = "Égalité 😐"
        elif (choix == "pierre" and bot_choice == "ciseaux") or \
             (choix == "papier" and bot_choice == "pierre") or \
             (choix == "ciseaux" and bot_choice == "papier"):
            result = "Tu as gagné 🎉"
        else:
            result = "J’ai gagné 😎"

        await ctx.send(f"✊✋✌️ Tu as choisi **{choix}** | J’ai choisi **{bot_choice}** → {result}")

    @commands.hybrid_command(name="rate", description="Note quelque chose 📊")
    async def rate(self, ctx, *, thing: str):
        percent = random.randint(0, 100)
        await ctx.send(f"📊 Je donne **{percent}%** à **{thing}** !")

    @commands.hybrid_command(name="reverse", description="Renvoie ton texte à l’envers 🔄")
    async def reverse(self, ctx, *, text: str):
        await ctx.send(text[::-1])

    @commands.hybrid_command(name="mock", description="Écrit ton texte en mode mOcKiNg 🐸")
    async def mock(self, ctx, *, text: str):
        mocked = ''.join(random.choice([c.upper(), c.lower()]) for c in text)
        await ctx.send(mocked)

    @commands.hybrid_command(name="say", description="Le bot répète ton message 🗣️")
    async def say(self, ctx, *, message: str):
        await ctx.send(message)

    @commands.hybrid_command(name="love", description="Calcule l’amour entre 2 personnes ❤️")
    async def love(self, ctx, member1: discord.Member, member2: discord.Member):
        percent = random.randint(0, 100)
        if percent < 30:
            emoji = "💔"
        elif percent < 70:
            emoji = "💞"
        else:
            emoji = "💖🔥"
        await ctx.send(f"{member1.mention} ❤️ {member2.mention} → **{percent}%** {emoji}")

    @commands.hybrid_command(name="ship", description="Crée un ship name entre 2 membres 💘")
    async def ship(self, ctx, member1: discord.Member, member2: discord.Member):
        name1 = member1.display_name
        name2 = member2.display_name
        half1 = name1[:len(name1)//2]
        half2 = name2[len(name2)//2:]
        ship_name = half1 + half2
        percent = random.randint(20, 100)
        await ctx.send(f"💘 Nouveau couple : **{member1.mention} + {member2.mention} = {ship_name}** ({percent}% d’amour)")

    # ----------------------------
    # 🤺 Commandes interactives
    # ----------------------------
    @commands.hybrid_command(name="hug", description="Fais un câlin à quelqu’un 🤗")
    async def hug(self, ctx, member: discord.Member):
        gifs = [
            "https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif",
            "https://media.giphy.com/media/od5H3PmEG5EVq/giphy.gif",
            "https://media.giphy.com/media/143vPc6b08locw/giphy.gif"
        ]
        await ctx.send(f"🤗 {ctx.author.mention} fait un câlin à {member.mention} !\n{random.choice(gifs)}")

    @commands.hybrid_command(name="kiss", description="Embrasse quelqu’un 😘")
    async def kiss(self, ctx, member: discord.Member):
        gifs = [
            "https://media.giphy.com/media/G3va31oEEnIkM/giphy.gif",
            "https://media.giphy.com/media/KH1CTZtw1iP3W/giphy.gif",
            "https://media.giphy.com/media/12VXIxKaIEarL2/giphy.gif"
        ]
        await ctx.send(f"😘 {ctx.author.mention} embrasse {member.mention} !\n{random.choice(gifs)}")

    @commands.hybrid_command(name="slap", description="Mets une claque à quelqu’un 👋")
    async def slap(self, ctx, member: discord.Member):
        gifs = [
            "https://media.giphy.com/media/Gf3AUz3eBNbTW/giphy.gif",
            "https://media.giphy.com/media/jLeyZWgtwgr2U/giphy.gif",
            "https://media.giphy.com/media/Zau0yrl17uzdK/giphy.gif"
        ]
        await ctx.send(f"👋 {ctx.author.mention} met une claque à {member.mention} !\n{random.choice(gifs)}")

    @commands.hybrid_command(name="fight", description="Défie quelqu’un en duel ⚔️")
    async def fight(self, ctx, member: discord.Member):
        gifs = [
            "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif",
            "https://media.giphy.com/media/l1J9EdzfOSgfyueLm/giphy.gif",
            "https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif"
        ]
        await ctx.send(f"⚔️ {ctx.author.mention} défie {member.mention} en duel !\n{random.choice(gifs)}")

    # ----------------------------
    # 🎮 Pendu multijoueurs
    # ----------------------------
    @commands.hybrid_command(name="pendu", description="Lance une partie multijoueur du pendu 🎮")
    async def pendu(self, ctx):
        if ctx.channel.id in self.hangman_games:
            return await ctx.send("⚠️ Une partie est déjà en cours dans ce salon !")

        words = ["python", "discord", "ordinateur", "programmation", "fromage", "voiture", "espace", "chatgpt"]
        word = random.choice(words)
        self.hangman_games[ctx.channel.id] = {"word": word, "guessed": set(), "tries": 0}

        display = " ".join("_" for _ in word)
        await ctx.send(
            f"🎮 Jeu du pendu lancé dans {ctx.channel.mention} !\nMot : {display}\nEssais restants : 6\n\n{self.hangman_stages[0]}")

    @commands.hybrid_command(name="guesspendu", description="Propose une lettre pour le pendu 🔤")
    async def guesspendu(self, ctx, letter: str):
        game = self.hangman_games.get(ctx.channel.id)

        if not game:
            return await ctx.send("❌ Il n’y a pas de partie en cours dans ce salon. Utilise `!pendu`.")

        word = game["word"]
        guessed = game["guessed"]
        tries = game["tries"]

        letter = letter.lower()
        if len(letter) != 1 or not letter.isalpha():
            return await ctx.send("❌ Merci de proposer **une seule lettre valide**.")

        if letter in guessed:
            return await ctx.send(f"⚠️ La lettre `{letter}` a déjà été proposée.")

        guessed.add(letter)

        if letter not in word:
            game["tries"] += 1
            tries = game["tries"]
            if tries >= 6:
                del self.hangman_games[ctx.channel.id]
                return await ctx.send(f"💀 Partie terminée ! Le mot était **{word}**.\n\n{self.hangman_stages[6]}")

        display = " ".join(l if l in guessed else "_" for l in word)

        if "_" not in display.replace(" ", ""):
            del self.hangman_games[ctx.channel.id]
            return await ctx.send(f"🎉 Bravo à tous ! Le mot était **{word}** ✅")

        await ctx.send(
            f"Mot : {display}\nEssais restants : {6 - game['tries']}\n\n{self.hangman_stages[game['tries']]}")


async def setup(bot):
    await bot.add_cog(Fun(bot))
