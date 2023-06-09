import nextcord
from nextcord.ext import commands
from config import green

class Unlock(commands.Cog):
    def __init__(self, client): 
         self.client = client
    
    @nextcord.slash_command(name = 'unlock')
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def unlock(self, interaction:nextcord.Interaction):
        """Unlocks the channel for shayan"""
        embed = nextcord.Embed(title="Done!",description="Channel Opened",color = green)
        await interaction.response.send_message(embed=embed, delete_after=2)
        drole = nextcord.utils.get(interaction.guild.roles, name = 'Sasta Sherlock')
        await interaction.channel.set_permissions(drole, view_channel=True)
        
    @unlock.error
    async def unlock_error(self, ctx, error):
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
    client.add_cog(Unlock(client))