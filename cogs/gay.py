import discord
from discord.ext import commands
from config import embed_color  
import random

class Forfun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog - ForFun is online")

    # Gay test        
    @discord.app_commands.command(name="gay", description="Pokazuje w ilu procentach jesteś gejem")
    async def gay(self, interaction: discord.Interaction):
        user_name = interaction.user.name
        if user_name == "mrxarom":
            gay = random.randint(0, 5)
        elif user_name == "bez_nazwy1942":
            gay = random.randint(0, 10)
        elif user_name == ".klopsik1":
            gay = random.randint(90,100)
        elif user_name == "pawix25":
            gay = random.randint(100,1000000)
        else: 
            gay = random.randint(0, 100)
        print(f"Uzytkownik {user_name} uzyl komendy gay")  # Debugging line
        if user_name == ".klopsik1":
            embed = discord.Embed(
            title="Test na geja🌈",
            description=(f"Użytkownik {user_name} jest pedałem w {gay}%"),
            color=embed_color
        )
        elif user_name == "pawix25":
            embed = discord.Embed(
            title="Test na geja🌈",
            description=(f"Idź na siłownie. Jesteś gejem w {gay}%"),
            color=embed_color
        )
        else:
            embed = discord.Embed(
                title="Test na geja🌈",
                description=(f"Użytkownik {user_name} jest gejem w {gay}%"),
                color=embed_color
            )
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Forfun(bot))