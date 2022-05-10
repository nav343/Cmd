import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

class Mods(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # The clear command (Slash Command)
    @nextcord.slash_command(name='clear', description='Clears the given number of messages from the current channel')
    async def clear_msg(self, interaction: Interaction, number: int=SlashOption(name='number', description='Number of messages to be cleared', required=True, autocomplete=False, max_value=1000, min_value=1)):
        await interaction.channel.purge(limit=number)
        await interaction.response.send_message(f'Clearing {number} of messages.')
        await interaction.edit_original_message(content=f'Cleared {number} {"message" if number == 1 else "messages"} from {interaction.channel.mention}')

    @nextcord.slash_command(name='ban', description='Ban a member of your server', guild_ids=[951344945762013195, 912182674418982982])
    @commands.has_permissions(ban_members=True)
    async def ban_mem(self, ctx: Interaction, member: nextcord.Member=SlashOption(name='name', description='Name of the member that you want ban.', required=True), reason=SlashOption(name='reason', description='Reason for banning the member', required=False, default=None)):
        emb = nextcord.Embed(title=f'{ctx.user.name} banned {member.name}.', color=nextcord.Color.blue())
        emb.add_field(name='Reason', value=reason)
        try:
            await member.ban(reason=reason)
            await ctx.response.send_message(embed=emb)
        except Exception:
            err_emb = nextcord.Embed(title='Missing Permissions', description='You are missing Admin Permissions. Only members with Admin power can ban other members.', color=nextcord.Color.red())
            await ctx.response.send_message(embed=err_emb)

    @nextcord.slash_command(name='kick', description='Kick a member of your server', guild_ids=[951344945762013195, 912182674418982982])
    @commands.has_permissions(kick_members=True)
    async def kick_mem(self, ctx: Interaction, member: nextcord.Member=SlashOption(name='name', description='Name of the member that you want kick.', required=True), reason=SlashOption(name='reason', description='Reason for Kicking the member', required=False, default=None)):
        emb = nextcord.Embed(title=f'{ctx.user.name} kicked {member.name}.', color=nextcord.Color.blue())
        emb.add_field(name='Reason', value=reason)
        try:
            await member.kick(reason=reason)
            await ctx.response.send_message(embed=emb)
        except Exception:
            err_emb = nextcord.Embed(title='Missing Permissions', description='You are missing Admin Permissions. Only members with Admin power can kick other members.', color=nextcord.Color.red())
            await ctx.response.send_message(embed=err_emb)

def setup(bot):
    bot.add_cog(Mods(bot))
