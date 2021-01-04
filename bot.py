import discord
import random
import pyautogui
import time
import webbrowser
from discord.ext import commands

client = commands.Bot(command_prefix='?')

# -----------------------------------------------------------------------------------------------------------------------
# testing
'''
@client.command(pass_context=True)
@commands.has_role(".")
async def photo(ctx, amount=1):
    await ctx.send(file=discord.File('Ok.png'))
'''


# To bot is online :)
@client.event
async def on_ready():
    print("I'm Alive.")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Menidify"))


# -----------------------------------------------------------------------------------------------------------------------


# Roles
Join = "Member"


@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name=Join)
    await member.add_roles(role)
    print(f"{member} was given {role}")


# -----------------------------------------------------------------------------------------------------------------------
# Roles
@client.command(pass_context=True)
@commands.has_role(".")
async def mute(ctx, member: discord.Member):
    role = discord.utils.find(lambda r: r.name == 'Trash', ctx.guild.roles)
    if role in member.roles:
        await ctx.send("{} is already muted".format(member))
    else:
        await member.add_roles(role)
        await ctx.send("{} is now muted".format(member))


@client.command(pass_context=True)
@commands.has_role(".")
async def unmute(ctx, member: discord.Member):
    role = discord.utils.find(lambda r: r.name == 'Trash', ctx.guild.roles)
    if role in member.roles:
        await member.remove_roles(role)
        await ctx.send("{} mute removed".format(member))
    else:
        await ctx.send("{} is not muted".format(member))


# DELETE
@client.command(pass_context=True)
@commands.has_role(".")
async def delete(ctx, amount=1):
    await ctx.channel.purge(limit=int(amount))


@client.command()
@commands.has_role(".")
async def Nuclear(ctx, amount=500000):
    await ctx.channel.purge(limit=amount)


# BAN / KICK / UNBAN
@client.command(pass_context=True)
@commands.has_role(".")
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} Was Kicked From The Server')


@client.command(pass_context=True)
@commands.has_role(".")
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')


@client.command(pass_context=True)
@commands.has_role(".")
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user


# Games.:D
@client.command(aliases=['8ball', 'test'])
async def mage(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I see it, Yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try later.',
                 'ASk again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


# Takes screenshots from sites and the post it on chat
@client.command(pass_context=True)
@commands.has_role(".")
async def screenshot(ctx, url):
    await ctx.send('Here is your screenshot you pervert:')
    webbrowser.open(url , new=2)
    time.sleep(5)
    pyautogui.screenshot(f'C:\DiscordBot\site.png')
    await ctx.send(file=discord.File(f'site.png'))


client.run('NzMyMDA2ODM5NjgzNjQ1NTAx.XwvFHw.2F38XvuYoBDH6fuLOV4lUE3sKSo')
