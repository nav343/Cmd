import nextcord
import json
import requests
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
    async def cat(self, ctx):
        url = 'https://cataas.com/cat?json=true'
        res = requests.get(url)
        data = json.loads(res.text)
        imgurl = data['url']
        img_url = f'https://cataas.com{imgurl}'
        emb = nextcord.Embed(title='Cats....... 😻',color=nextcord.Color.blue())
        emb.set_image(url=img_url)
        await ctx.send(embed=emb)

    @commands.command()
    async def dog(self, ctx):
        msg = await ctx.send('Searching for a dog........')
        dog_url = 'https://random.dog/woof.json'
        dog_res = requests.get(dog_url)
        dog_data = json.loads(dog_res.text)
        dogimg = dog_data['url']
        dog_emb = nextcord.Embed(title='Dogs...... 🐶',color=nextcord.Color.blue())
        dog_emb.set_image(url=dogimg)
        print(dogimg)
        await msg.edit(content='', embed=dog_emb)

    @nextcord.slash_command(name='fox', description='Get a random fox', guild_ids=[951344945762013195])
    async def fox(self, ctx: Interaction):
        await ctx.response.send_message('Searching for a fox........')
        fox_url = 'https://randomfox.ca/floof/'
        fox_res = requests.get(fox_url)
        fox_data = json.loads(fox_res.text)
        foximg = fox_data['image']
        fox_emb = nextcord.Embed(title='Fox...... 🦊',color=nextcord.Color.blue())
        fox_emb.set_image(url=foximg)
        print(foximg)
        await ctx.edit_original_message(content='', embed=fox_emb)

    @nextcord.slash_command(name='word', guild_ids=[951344945762013195])
    async def word(ctx: Interaction): ...

    @word.subcommand(name='meaning', description='Get the meaning of a word')
    async def meaning(self, ctx: Interaction, word = SlashOption(name='word', description='What word do you want to search ?', required=True)):
        await ctx.response.send_message(f'Searching for {word}......')
        req = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
        req_data = json.loads(req.text)
        wrd = req_data['word']
        phonetic = req_data['phonetic']

        word_emb = nextcord.Embed(title=f'Meaning of {word} !!!', color=nextcord.Color.blue())
        word_emb.add_field(name='**Word**', value=wrd)
        word_emb.add_field(name='**Phonetic**', value=phonetic)
        await ctx.edit_original_message(embed=word_emb)

    @nextcord.slash_command(name='slap', description='Slaps a member of your server', guild_ids=[951344945762013195])
    async def slap_mem(self, ctx: Interaction, member: nextcord.Member = SlashOption(name='member', description='Name of the member that you want slap', required=True)):
        slap_emb = nextcord.Embed(title=f'{ctx.user.name} slapped {member.name}', description='', color=nextcord.Color.blue())
        await ctx.response.send_message(embed=slap_emb)

def setup(bot):
    bot.add_cog(Fun(bot))
