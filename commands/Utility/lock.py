import nextcord
from nextcord.ext import commands
from config import green
from nextcord import Interaction

class Unilock(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @nextcord.ui.button(label="Unlock", style=nextcord.ButtonStyle.red)
    async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        drole = nextcord.utils.get(interaction.guild.roles, name = 'Sasta Sherlock')
        await interaction.channel.set_permissions(drole, view_channel=True)
        await interaction.response.send_message("Channel unlocked, Shanny aka 🤡 can see you! Be careful out there.", ephemeral=True)
        self.value = True
        self.stop()

class Lock(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @nextcord.slash_command(name = 'lock')
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def lock(self, interaction:nextcord.Interaction):
        """Locks the channel for shayan"""
        drole = nextcord.utils.get(interaction.guild.roles, name = 'Sasta Sherlock')
        await interaction.channel.set_permissions(drole, view_channel=False)
        embed = nextcord.Embed(title="Channel locked",description="Do *m!unlock* to open the channel or press the button below!",color = green)
        view=Unilock()
        msg = await interaction.response.send_message(embed=embed,view=view)
        await view.wait()
        await msg.delete()
        
    @lock.error
    async def lock_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        em = nextcord.Embed(title=f"Woah Slow it down buckaroo!",description=f"Try again in **{error.retry_after:.2f}s**", color=0xe74c3c)
        await ctx.send(embed=em)
      elif isinstance(error, commands.MissingPermissions):
        em = nextcord.Embed(title=f"Missing Perms",description=f"Change this in the channel or server", color=0xe74c3c)
        await ctx.send(embed=em)
      else:
        emb = nextcord.Embed(title=f"Something went wrong!",description=f"Tell Moaz about this error if possible", color=0xe74c3c)
        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(Lock(client))
