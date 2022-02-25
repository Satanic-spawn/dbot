import discord
import os
import sys
import prices
import pred
import pred2

client = discord.Client()
TOKEN = 'NzAzNTg4NzM1MjQ1MjIxOTM5.XqQyEg.YsjygcuyNn1FVp-WdSysHRArp88'
lish = 'BTTC','ETH'


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hi'):
        await message.channel.send('Hello')

    if message.content.startswith('$mylist'):
        lisht = message.content.replace("$mylist","")
        lishtn = lisht.split(",")
        lishtn.extend(lish)
        await message.channel.send(lishtn)

    if message.content.startswith('$price '):
        nm = message.content.replace("$price ","")
        nml = nm.split(" ")
        prc = prices.price_yf(nml[0], nml[1], nml[2])
        await message.channel.send(file=discord.File('dbot/dbimages/fig1.png'))
        #await message.channel.send(prc)

    if message.content.startswith('$predprice '):
        nm = message.content.replace("$predprice ","")
        nml = nm.split(" ")
        name = nml[0]+"-INR"
        prc = str(pred2.predd2(nml[0], "INR"))
        await message.channel.send("Model accuracy graph for "+nml[0]+": ")
        await message.channel.send(prc)


client.run(TOKEN)
