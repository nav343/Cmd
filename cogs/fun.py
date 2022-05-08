import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @nextcord.slash_command(name="avatar", description="Get the Avatar/Pfp of a member")
    async def ava(self, interaction: Interaction, member : nextcord.Member=SlashOption(name="member", description="name of the member", required=False)):
        if member != None:
            emb = nextcord.Embed(title=f'{member.name}\'s Profile Picture !!!', color=nextcord.Color.blue())
            emb.set_image(url = member.display_avatar)
            await interaction.response.send_message(embed=emb)
        elif member == None:
            my_emb = nextcord.Embed(title='Your Profile Picture !!!', color=nextcord.Color.blue())
            my_emb.set_image(url = interaction.user.display_avatar)
            await interaction.response.send_message(embed=my_emb)

    @commands.command()
    async def cat(self, ctx, color=None):
        if color == None:
            error_emb = nextcord.Embed(title='❌ Color is a required argument that is missing !!!.', color=nextcord.Color.red())
            await ctx.send(embed=error_emb)
        else:
            cat_emb = nextcord.Embed(title='Cats...... 😻', color=nextcord.Color.blue())
            cat_emb.set_image(url=f'https://cataas.com/cat/{color}')
            await ctx.send(embed=cat_emb)

def setup(bot):
    bot.add_cog(Fun(bot))
