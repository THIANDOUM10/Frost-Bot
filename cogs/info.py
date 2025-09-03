import discord
from discord.ext import commands
import datetime

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.datetime.utcnow()

    @commands.hybrid_command(name="ping", description="Renvoie la latence du bot 🏓")
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.send(f"🏓 Pong ! Latence : **{latency} ms**")

    @commands.hybrid_command(name="uptime", description="Depuis combien de temps Frost Bot est en ligne ⏳")
    async def uptime(self, ctx):
        now = datetime.datetime.utcnow()
        delta = now - self.start_time
        days, seconds = delta.days, delta.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        await ctx.send(f"⏳ Frost Bot est en ligne depuis **{days}j {hours}h {minutes}m {seconds}s**")

    @commands.hybrid_command(name="botinfo", description="Infos sur Frost Bot 🤖")
    async def botinfo(self, ctx):
        embed = discord.Embed(
            title="❄️ Frost Bot",
            description="Un bot Discord créé par **KINGFROST** pour profiter pleinement de Discord 🚀",
            color=discord.Color.blue()
        )
        embed.add_field(name="👑 Créateur", value="**KINGFROST**", inline=True)
        embed.add_field(name="🤖 Nom du bot", value="Frost Bot", inline=True)
        embed.add_field(name="📡 Latence", value=f"{round(self.bot.latency * 1000)} ms", inline=True)
        embed.add_field(name="⏳ Uptime", value="Utilise `!uptime` pour voir depuis combien de temps je tourne", inline=False)
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)
        embed.set_footer(text=f"Demandé par {ctx.author}", icon_url=ctx.author.display_avatar.url)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Info(bot))
