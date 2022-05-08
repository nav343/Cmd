import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

class Mods(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name='clear', description='Clears the given number of messages from the current channel', guild_ids=[951344945762013195])
    async def clear_msg(self, interaction: Interaction, number: int=SlashOption(name='number', description='Number of messages to be cleared', required=True, autocomplete=False, max_value=1000, min_value=1)):
        await interaction.channel.purge(limit=number)
        await interaction.response.send_message(f'Clearing {number} of messages.')
        await interaction.edit_original_message(content=f'Cleared {number} {"message" if number == 1 else "messages"} from {interaction.channel.mention}')

def setup(bot):
    bot.add_cog(Mods(bot))
