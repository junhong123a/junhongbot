import discord
import asyncio



client = discord.Client()
game = discord.Game("준홍아 도움")               

@client.event
async def on_ready():
    print('Bot Online')
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):             
    if message.author.bot:                 
        return None                        
    if message.content == "준홍아 안녕":         
        embed = discord.Embed(title="안녕하세요!", description="준홍봇입니다. 준홍봇의 개발자는 준홍!good good#8922 이며, 이 봇은 베타입니다.", color=0x85CFFF)
        embed.set_footer(text="준홍봇 응답시스템")
        await message.channel.send(embed=embed)
        await message.channel.send("준홍봇의 개발자 준홍은 봇 도우미로 활동하고 있습니다. 도움이 필요하신분은 준홍!good good#8922로 DM  주시기 바랍니다.")
        
    if message.content  ==  '준홍아 핑':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="준홍봇 핑 체크", value=f'준홍봇의 핑은\n{round(client.latency * 1000)}ms입니다!', inline=True)
                embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
                print(f'ping is {round(client.latency * 1000)}ms')

client.run("NTAzNTAyMTU3OTI1MDU2NTE0.XoA4-w.QD5VgisG0H4OAdKb15-pzr5D29Q")
