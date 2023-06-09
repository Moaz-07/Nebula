from nextcord import SlashOption,Interaction
from nextcord.ext import commands
import nextcord
from config import green
import random
from Assets.eight_ball import ball_replies

class Ball(commands.Cog):
    def __init__(self, client): 
         self.client = client

    @nextcord.slash_command(name = "8ball")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ball(self, interaction: nextcord.Interaction, question: str = SlashOption(description="Speak to the 8ball")):
        """Ask the magik 8ball a question"""
        rolk = random.choice(ball_replies)
        e = nextcord.Embed(description=(f"🎱 {rolk}"))
        await interaction.response.send_message(f"> {question}",embed=e)

    @ball.error
    async def ball_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        em = nextcord.Embed(title=f"Woah Slow it down buckaroo!",description=f"Try again in **{error.retry_after:.2f}s**", color=0xe74c3c)
        await ctx.send(embed=em)
      elif isinstance(error,commands.MissingRequiredArgument):
        er = nextcord.Embed(title="Missing Argument",description=f"Missing a required argument: {error.param}",color=0xe74c3c)
        await ctx.send(embed=er)
      else:
        emb = nextcord.Embed(title=f"Something went wrong!",description=f"Tell Moaz about this error if possible", color=0xe74c3c)
        await ctx.send(embed=emb)
        
def setup(client):
    client.add_cog(Ball(client))
