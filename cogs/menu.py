import discord
from discord.ext import commands

class Menu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="menu", description="Affiche toutes les commandes disponibles 📜")
    async def menu(self, ctx):
        embed = discord.Embed(
            title="📌 Menu des commandes",
            description="Sélectionne une catégorie pour voir toutes les commandes disponibles.",
            color=discord.Color.blurple()
        )
        embed.set_footer(text=f"Demandé par {ctx.author}", icon_url=ctx.author.display_avatar.url)

        # Liste des catégories
        options = [
            discord.SelectOption(label="🎮 Fun / Jeux", description="Toutes les commandes amusantes", value="fun"),
            discord.SelectOption(label="🤺 Interactions", description="Commandes pour interagir avec d'autres membres", value="inter"),
            discord.SelectOption(label="🛠️ Modération", description="Commandes pour modérer le serveur", value="mod"),
            discord.SelectOption(label="ℹ️ Infos / Utilitaires", description="Commandes informatives ou utilitaires", value="info"),
        ]

        select = discord.ui.Select(placeholder="Choisis une catégorie…", options=options)

        async def select_callback(interaction: discord.Interaction):
            if select.values[0] == "fun":
                cmds = [
                    "`!dice` 🎲", "`!roll <faces>` 🎲", "`!coinflip` 🪙", "`!8ball <question>` 🔮",
                    "`!meme` 😂", "`!gif` 🔥", "`!cat` 🐱", "`!dog` 🐶",
                    "`!joke` 🤣", "`!rps <pierre/papier/ciseaux>` ✊✋✌️", "`!rate <quelque chose>` 📊",
                    "`!reverse <texte>` 🔄", "`!mock <texte>` 🐸", "`!say <texte>` 🗣️",
                    "`!love <user1> <user2>` ❤️", "`!ship <user1> <user2>` 💘",
                    "`!pendu` 🎮", "`!guesspendu <lettre>` 🔤"
                ]
                embed = discord.Embed(title="🎮 Fun / Jeux", description="\n".join(cmds), color=discord.Color.green())

            elif select.values[0] == "inter":
                cmds = [
                    "`!hug <user>` 🤗", "`!kiss <user>` 😘", "`!slap <user>` 👋", "`!fight <user>` ⚔️"
                ]
                embed = discord.Embed(title="🤺 Interactions entre membres", description="\n".join(cmds), color=discord.Color.orange())

            elif select.values[0] == "mod":
                cmds = [
                    "`!kick <user>` 🚪", "`!ban <user>` 🔨", "`!clear <nombre>` 🧹",
                    "`!mute <user> [minutes]` ⏳", "`!unmute <user>` 🔊",
                    "`!warn <user> <raison>` ⚠️", "`!warnings <user>` 📋"
                ]
                embed = discord.Embed(title="🛠️ Modération", description="\n".join(cmds), color=discord.Color.red())

            elif select.values[0] == "info":
                cmds = [
                    "`!ping` 🏓", "`!botinfo` 📜"
                ]
                embed = discord.Embed(title="ℹ️ Infos / Utilitaires", description="\n".join(cmds), color=discord.Color.blurple())

            await interaction.response.edit_message(embed=embed, view=view)

        select.callback = select_callback

        view = discord.ui.View()
        view.add_item(select)
        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(Menu(bot))

