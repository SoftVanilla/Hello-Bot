from discord.ext import commands

import random

# 개발자 페이지에서 봇에 대한 토큰 문자열을 가져온 뒤, TOKEN에 대입하자
TOKEN = "봇 페이지에서 받은 토큰 문자열"

client = commands.Bot(command_prefix='/')


@client.event
async def on_ready():
    print(f'{client.user} online!')


@client.command(name='주사위')
async def roll(ctx, number: int):
    await ctx.send(f'주사위를 굴려 {random.randint(1,number)}이(가) 나왔습니다. (1-{number})')


@roll.error
async def roll_error(ctx, error):
    await ctx.send(f"2 이상의 정수를 넣어주세요!\nex) /주사위 6")


client.run(TOKEN)
