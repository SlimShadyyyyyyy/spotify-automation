import random

import bot.config

import giphy_client
from giphy_client.rest import ApiException

import discord
from discord.ext import commands


class Giphy(commands.Cog):
    """The Giphy class is a Discord bot cog that uses the Giphy API to search for and display GIFs in a Discord server."""

    def __init__(self, bot):
        self.bot = bot
        self.giphy_client = giphy_client.DefaultApi()
        self.limit = 25
        self.rating = 'g'

    @commands.group(name='gif', invoke_without_command=True)
    async def giphy(self, ctx, *, q):
        try:
            giphy_api_response = self.giphy_client.gifs_search_get(
                api_key=bot.config.giphy_api_key(),
                q=q,
                limit=self.limit,
                rating=self.rating
            )

            giphy_giffs = list(giphy_api_response.data)
            giff = random.choice(giphy_giffs)

            embed = discord.Embed(title=q)
            embed.set_image(url=f'https://media.giphy.com/media/{giff.id}/giphy.gif')

            await ctx.channel.send(embed=embed)

        except ApiException as e:
            print('Exception for the API', e)
        
    @giphy.command()
    async def trending(self, ctx):
        try:
            giphy_api_response = self.giphy_client.gifs_trending_get(
                api_key=bot.config.giphy_api_key(),
                limit=self.limit,
            )
            
            giphy_giffs = list(giphy_api_response.data)
            giff = random.choice(giphy_giffs)

            embed = discord.Embed(title='Trending GIF')
            embed.set_image(url=f'https://media.giphy.com/media/{giff.id}/giphy.gif')

            await ctx.channel.send(embed=embed)

        except ApiException as e:
            print('Exception for the API', e)
    
    @giphy.command()
    async def random(self, ctx):
        try:
            giphy_api_response = self.giphy_client.gifs_random_get(
                api_key=bot.config.giphy_api_key(),
                rating=self.rating
            )

            random_giff = giphy_api_response.data

            embed = discord.Embed(title='Trending GIF')
            embed.set_image(url=f'https://media.giphy.com/media/{random_giff.id}/giphy.gif')

            await ctx.channel.send(embed=embed)

        except ApiException as e:
            print('Exception for the API', e)
    
    @giphy.command()
    async def translate(self, ctx, *, s):
        try:
            giphy_api_response = self.giphy_client.gifs_translate_get(
                api_key=bot.config.giphy_api_key(),
                s=s
            )

            translated_giff = giphy_api_response.data
            
            embed = discord.Embed(title='Translated GIF')
            embed.set_image(url=f'https://media.giphy.com/media/{translated_giff.id}/giphy.gif')

            await ctx.channel.send(embed=embed)

        except ApiException as e:
            print('Exception for the API', e)


def setup(bot):
    """ Setup Giphy Module"""
    bot.add_cog(Giphy(bot))
        
