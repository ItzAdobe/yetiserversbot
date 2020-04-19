import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

#Bot Started And Custom Play and Status
@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.idle, activity=discord.Game('Helping Yeti Servers'))
	print('Bot Custom Play is Working')
	print('Bot and Now Online')
#---------------------------------------------------

#My End Logs
@client.event
async def on_member_join(ctx):
    print(f'{member} has Joined Yeti Servers')
	
@client.event
async def on_member_remove(member):
    print(f'{member} has left/banned Yeti Servers')
#---------------------------------------------------

#error For No Command Found
@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send('Invalid Command Used')
#---------------------------------------------------

	
#ping Command
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
#---------------------------------------------------	
	
#clear Command
@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)
	
	
@clear.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Please Give An Amount Of Messages To Delete')
	
#---------------------------------------------------




client.run('NzAxMzEzOTExMzAyOTE0MDk4.Xpvrhw.uPZWbq1B8BkAUkmBA9tNxBhUtiE')
