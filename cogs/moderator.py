import discord
from discord.ext import commands
from datetime import timedelta

class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.warns = {}  # dictionnaire pour stocker les avertissements {user_id: [list des warns]}

    # CLEAR
    @commands.hybrid_command(name="clear", description="Supprime un nombre de messages 📋")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = 5):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"✅ {amount} messages supprimés.", delete_after=5)

    # KICK
    @commands.hybrid_command(name="kick", description="Expulse un membre du serveur 👢")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason: str = "Aucune raison donnée"):
        await member.kick(reason=reason)
        await ctx.send(f"👢 {member.mention} a été expulsé pour : {reason}")

    # BAN
    @commands.hybrid_command(name="ban", description="Bannit un membre du serveur 🔨")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason: str = "Aucune raison donnée"):
        await member.ban(reason=reason)
        await ctx.send(f"🔨 {member.mention} a été banni pour : {reason}")

    # MUTE
    @commands.hybrid_command(name="mute", description="Réduit un membre au silence ⏳")
    @commands.has_permissions(moderate_members=True)
    async def mute(self, ctx, member: discord.Member, duration: int = 10, *, reason: str = "Aucune raison donnée"):
        """Mute avec un timeout (par défaut 10 minutes)."""
        time = timedelta(minutes=duration)
        await member.timeout(time, reason=reason)
        await ctx.send(f"⏳ {member.mention} a été mute pendant {duration} minutes. Raison : {reason}")

    # UNMUTE
    @commands.hybrid_command(name="unmute", description="Rend la parole à un membre 🔊")
    @commands.has_permissions(moderate_members=True)
    async def unmute(self, ctx, member: discord.Member):
        await member.timeout(None)  # enlève le timeout
        await ctx.send(f"🔊 {member.mention} a été unmute.")

    # WARN
    @commands.hybrid_command(name="warn", description="Donne un avertissement ⚠️")
    @commands.has_permissions(moderate_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason: str = "Aucune raison donnée"):
        if member.id not in self.warns:
            self.warns[member.id] = []
        self.warns[member.id].append(reason)
        await ctx.send(f"⚠️ {member.mention} a reçu un avertissement : {reason}")

    # LISTE DES WARNS
    @commands.hybrid_command(name="warnings", description="Affiche les avertissements d’un membre 📋")
    async def warnings(self, ctx, member: discord.Member):
        if member.id not in self.warns or len(self.warns[member.id]) == 0:
            await ctx.send(f"✅ {member.mention} n’a aucun avertissement.")
        else:
            warns = "\n".join([f"{i+1}. {r}" for i, r in enumerate(self.warns[member.id])])
            await ctx.send(f"📋 Avertissements pour {member.mention} :\n{warns}")



async def setup(bot):
    await bot.add_cog(Moderator(bot))
