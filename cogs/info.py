import nextcord
from nextcord import Interaction
from nextcord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, ctx):
        if self.bot.user in ctx.mentions:
            await ctx.channel.send('My prefix is `$>` !!!')

    @commands.command()
    async def help(self, ctx, sub_command=None):
        if sub_command == None:
            emb = nextcord.Embed(title='Cmd Help Desk', color=nextcord.Color.blue(), description='My prefix is `$>` (pinging me also works).\nType out `$>[command]` to get a detailed info about that particular linux command.')
            emb.add_field(name='Available Modules/Commands', value='''
** 💻 Linux Commands**
`cd` => Change Directory,
`pwd` => Present Working Directory,
`ip` => Internet Protocol,
`ls` => List Dir content,
`find` => locate files based on user's criteria,
`w` => Show a list of currently logged-in users,
`grep` => Search a file for a pattern of chars,
`cp` => Copy files and folders,
`mv` => Move files and folders,
`rm` => Remove files and folders,
`mkdir` => Make directories,
`ping` => Send ICMP ECHO_REQUEST to network hosts.

** 🎉 Fun**
`avatar/ava <member>` => Send the pfp of a person in the server. (Coming soon.....),
`dog` => Sends a random dog image from a public api (Coming soon.......),
`cat` => Sends a random cat image from a public api (Coming soon.......),
`slap <member>` => Slaps a member of your server.

** 🔨 Mods (Admin powers only)**
`kick <member>` => Kick a member,
`ban <member>` => Ban a member,
`clear <number>` => Delete a certain number of messages.

**🎵 Music**
Not yet implemented. !!!

Plz note that most of the commands given here are not complete......
\n''')
            emb.add_field(name='Support', value=':pray: Support the project by starring the official repo on github. \n https://github.com/nav343/Cmd', inline=False)
            emb.add_field(name='Add to your Server ?', value='Add me to your server by typing `$>invite` :smiling_face_with_3_hearts:', inline=False)
            await ctx.reply(embed=emb)
        else:
            await ctx.send(f'The value of sub command is {sub_command}')

    @nextcord.slash_command(name='help', description='Get all the available commands', guild_ids=[951344945762013195])
    async def help_sls(self, ctx: Interaction):
        emb = nextcord.Embed(title='Cmd Help Desk', color=nextcord.Color.blue(), description='My prefix is `$>` (pinging me also works).\nType out `$>[command]` to get a detailed info about that particular linux command.')
        emb.add_field(name='Available Modules/Commands', value='''
** 💻 Linux Commands**
`cd` => Change Directory,
`pwd` => Present Working Directory,
`ip` => Internet Protocol,
`ls` => List Dir content,
`find` => locate files based on user's criteria,
`w` => Show a list of currently logged-in users,
`grep` => Search a file for a pattern of chars,
`cp` => Copy files and folders,
`mv` => Move files and folders,
`rm` => Remove files and folders,
`mkdir` => Make directories,
`ping` => Send ICMP ECHO_REQUEST to network hosts.

** 🎉 Fun**
`avatar/ava <member>` => Send the pfp of a person in the server. (Coming soon.....),
`dog` => Sends a random dog image from a public api (Coming soon.......),
`cat` => Sends a random cat image from a public api (Coming soon.......),
`slap <member>` => Slaps a member of your server.

** 🔨 Mods (Admin powers only)**
`kick <member>` => Kick a member,
`ban <member>` => Ban a member,
`clear <number>` => Delete a certain number of messages.

**🎵 Music**
Not yet implemented. !!!

Plz note that most of the commands given here are not complete......
\n''')
        emb.add_field(name='Support', value=':pray: Support the project by starring the official repo on github. \n https://github.com/nav343/Cmd', inline=False)
        emb.add_field(name='Add to your Server ?', value='Add me to your server by typing `$>invite` :smiling_face_with_3_hearts:', inline=False)
        await ctx.response.send_message(embed=emb)


    @commands.command()
    async def invite(self, ctx):
        invite_emb = nextcord.Embed(color=nextcord.Color.blue())
        invite_emb.description = '[Add me to your server 😄 !!!](https://discord.com/api/oauth2/authorize?client_id=964833799567446040&permissions=8&scope=bot%20applications.commands)'
        await ctx.send(embed=invite_emb)

    
    @commands.command()
    async def support(self, ctx):
        await ctx.send(':pray: Support the project by starring the official github repo : https://github.com/nav343/Cmd')

def setup(bot):
    bot.add_cog(Info(bot))
