import asyncio
import datetime

from managers.database import add_warn, remove_warn, get_warnings

import discord
from discord.ext import commands


class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def warn(self, ctx, member: discord.Member, reason: str = None):
        total = await add_warn(
            user_id=member.id,
            guild_id=ctx.guild.id,
            reason=reason
        )

        embed = discord.Embed(color=discord.Color.blurple())
        embed.set_author(name=f'Warning for - {member}')
        embed.set_thumbnail(url=member.avatar)

        embed.add_field(
            name='Reason:',
            value=reason,
            inline=False
        )
        embed.add_field(
            name='Total Amount:',
            value=total,
            inline=False
        )

        embed.set_footer(
            text=f'Requested By - {ctx.author}',
            icon_url=ctx.author.display_avatar
        )
        
        warning_log_channel = ctx.guild.get_channel(1107408673808064553)

        await warning_log_channel.send(embed=embed)

        try:
            await member.send(f"You were warned by **{ctx.author}** in **{ctx.guild.name}**!\nReason: {reason}")
        except discord.HTTPException:
            await ctx.send(f'{member.mention}, you were warned by **{ctx.author}**!\nReason: {reason}', delete_after=1.5)

        if total > 3:
            mute_role = discord.utils.get(ctx.guild.roles, name='muted')
            if mute_role and mute_role not in member.roles:
                await member.add_roles(mute_role)
                try:
                    await member.send('You have been muted for 30 minutes.')
                finally:
                    await ctx.send(f'{member.mention} has been muted for 30 minutes.', delete_after=2)

            await asyncio.sleep(30 * 60) # mutes for 30 minutes
            await member.remove_roles(mute_role)

    @commands.command()
    async def removewarn(self, ctx, member: discord.Member, reason: str = None):
        pass

    @commands.command()
    async def warns(self, ctx, member: discord.Member):
        warns = await get_warnings(user_id=member.id, guild_id=ctx.guild.id)
        if warns:
            embed = discord.Embed(title=f'{member} Warnings', color=discord.Color.red())
            for warn in warns:
                embed.add_field(
                    name=f':warning: Warning {warn[0]}',
                    value=f'**Reason:** {warn[2]}\n**Date Issued:** {datetime.datetime.fromtimestamp(warn[3]).strftime("%d-%m-%Y %H:%M")}',
                    inline=True
                )
            await ctx.send(embed=embed)
