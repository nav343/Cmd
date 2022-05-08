import nextcord
from nextcord.ext import commands

class Linux(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def cd(self, ctx, path='~/Documents/nice/dir'):
        cd_embed = nextcord.Embed(title='Cd', color=nextcord.Color.blue())
        cd_embed.add_field(name='**Introduction**', value='In Linux and other Unix-like operating systems, the cd ("change directory") command is used to change the current working directory. When working on the Linux terminal, it is one of the most basic and frequently used commands. The user\'s current working directory is the folder (directory) in which he or she is now working. You\'re operating in a directory every time you interact with your command prompt. \n \n `cd` is a shell built-in whose behavior varies slightly depending on the shell. It determines the essential information for its execution by looking at the shell environment variables. We\'ll look at the built-in version of cd in Bash.')
        cd_embed.add_field(name='Syntax', value='`cd [OPTIONS] {path}`', inline=False)
        cd_embed.add_field(name='**Available OPTIONS**', value='Only two options are available to the command, both of which are rarely used. \n `-l`, follow symbolic links. by default, cd behaves as if the -l option is specified. \n `−p,` symbolic links should not be followed. to put it another way, if you choose this option and try to go to a symlink that refers to a directory, the cd will change to that directory. \n when used without any arguments, cd will transport you to your home directory in its most basic form.', inline=False)
        cd_embed.add_field(name="**Example**", value=f'`cd {path}`', inline=False)
        await ctx.send(embed=cd_embed)

    @commands.command()
    async def find(self, ctx):
        find_emb = nextcord.Embed(title='Find', color=nextcord.Color.blue())
        find_emb.add_field(name='**Introduction**', value='The `find` command helps us to find a particular file within a directory. It is used to find the list of files for the various conditions like permission, user ownership, modification, date/time, size, and more. \n The `find` utility comes by default with most of the Linux distros, so we don\'t need to install any additional package. It is one of the most essential and used commands of the Linux systems.')
        find_emb.add_field(name='**Syntax**', value='`find {location} {comparison-criteria} {search-term}`', inline=False)
        find_emb.add_field(name='**Symbols**', value='The following are the symbols used to specify the directory. \n **(.)** : For current directory name \n **(/)** : For the root directory', inline=False)
        find_emb.add_field(name='**Example**', value='Input\n`$ find . -name "*.py"` \nOutput\n`<All the files ending in .py extension inside the pwd>`', inline=False)
        find_emb.set_footer(text='💡 The \'.\' means that we want to find things inside the present working dir. The `-name` flag means that we want to search a file name with the name given inside ""')
        await ctx.send(embed=find_emb)

    @commands.command()
    async def ip(self, ctx):
        ip_emb = nextcord.Embed(title='Ip', color=nextcord.Color.blue())
        ip_emb.add_field(name='**Introduction**', value='`ip` command is a collection of utilities for controlling TCP/IP networking and traffic control in linux.\n **Syntax**\nThe basic syntax is as follow/n `ip a / ip addr`')
        ip_emb.add_field(name='**Options**', value='The IP command supports the following command-line options: \n-V: It is used to display the version of the IP command.\n-h, -human, -human-readable: It is used to display the statistics in the form of human-readable values.\n-b, -batch <FILENAME>: It is used to read and invoke commands from the given file or input. The failure may cause the termination of IP utility. The \'-force\' option will not let the IP terminated on errors in batch mode. If there were any errors during execution, the return code would be non zero.\b-s, -stats, -statistics: It is used to display more information such as statistics or time values.\n-d, -details: It is used to display the detailed output.\n-l, -loops <COUNT>: It is used to specify a maximum number of loops.\n-f, -family <FAMILY>: It is used to determine the protocol family. These protocol family identifiers may be inet, inet6, bridge, ipx, dnet, mpls, or link. And More', inline=False)
        await ctx.send(embed=ip_emb)

    @commands.command()
    async def pwd(self, ctx, path='~/.config/discord/'):
        pwd_embed = nextcord.Embed(title='Pwd', color=nextcord.Color.blue())
        pwd_embed.add_field(name='**Introduction**', value='The `pwd` command is used to print the current working directory. It\'s one of Linux\'s most fundamental and commonly used commands. When the command is ran, it prints out the full path of the current working directory. Most current shells, such as bash and zsh, provide pwd as a built-in shell command.\n Type `pwd` to check your current/present working directory.', inline=False)
        pwd_embed.add_field(name='**Example**', value=f'**Input**: `$ pwd`\n**Output**: `$ {path}`', inline=False)
        await ctx.send(embed=pwd_embed)
    

def setup(bot):
    bot.add_cog(Linux(bot))