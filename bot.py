import discord


# 개발자 페이지에서 봇에 대한 토큰 문자열을 가져온 뒤, TOKEN에 대입하자
TOKEN = "봇 페이지에서 받은 토큰 문자열"

client = discord.Client()


# 봇이 접속하면 아래의 함수를 실행하게 된다
@client.event
async def on_ready():
    print(f'{client.user} online!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send("그렇군요!")


# 봇을 실행하자
client.run(TOKEN)
