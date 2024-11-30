import discord
from discord.ext import commands
from config import embed_color  # Zakładam, że embed_color to poprawnie zdefiniowany kolor w twoim pliku config
import random

class Dlugosc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Dlugosc - ForFun is online")

    # Komenda "dlugosc"
    @discord.app_commands.command(name="dlugosc", description="Pokazuje jak długiego masz członka")
    async def dlugosc(self, interaction: discord.Interaction):
        user_name = interaction.user.name
        baklazan = random.randint(1, 20)  # Domyślny zakres losowania

        # Specjalny przypadek dla użytkownika ".klopsik"
        if user_name == ".klopsik":
            baklazan = random.randint(-100, -20)  # Zmiana zakresu na wartości ujemne
            embed = discord.Embed(
                title="Twój bakłażan 🍆",
                description=f"Użytkownik {user_name} jest kobietą. Jego bakłażan wynosi {baklazan} cm.",
                color=embed_color
            )
        else:
            embed = discord.Embed(
                title="Twój bakłażan 🍆",
                description=f"Użytkownik {user_name} ma bakłażana wielkości {baklazan} cm.",
                color=embed_color
            )

        # Wysłanie embedowanej wiadomości
        await interaction.response.send_message(embed=embed)

# Funkcja setup do dodania cogu
async def setup(bot):
    await bot.add_cog(Dlugosc(bot))
