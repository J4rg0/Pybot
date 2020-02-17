# bot.py
import discord
import os
import quotes
import phrases
import theImages
import rolls
import getToken

token = getToken.goToken()
client = discord.Client()

@client.event

async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!roll'):
        string = message.content
        words = string.split()
        words.remove('!roll')
        quote = rolls.addRoll(words)
        await message.channel.send(quote)

    if message.content.startswith('!plot'):
        string = message.content
        words = string.split()
        rolls.graphIt(words)
        await message.channel.send(file=discord.File('E:\Tools\Pybot\\rollchart.png'))

    # if message.content.startswith('!pie'):
    #     string = message.content
    #     words = string.split()
    #     rolls.piePlot(words)
    #     await message.channel.send(file=discord.File('E:\Tools\Best-Boi-Bot Python\\piechart.png'))

    if message.content.startswith('!mean'):
        string = message.content
        words = string.split()
        result = rolls.mean(words)
        await message.channel.send(result)


    if message.content.startswith('$best'):
        await message.channel.send('To crush the orks, see the Tau driven before you, and hear the lamentations of the Daemonettes.')
        await message.channel.send(file=discord.File('E:\Tools\Pybot\media\cb.jpg'))

    if message.content.startswith('!nurgle'):
        image = theImages.nurgleImage()
        await message.channel.send(file=discord.File(image))
        quote = quotes.nurgle()
        await message.channel.send(quote)


    if message.content.startswith('!tzeentch'):
        quote = quotes.tzeentch()
        await message.channel.send(quote)

    if message.content.startswith('!necron'):
        image = theImages.necronImage()
        await message.channel.send(file=discord.File(image))
        thePhrase = phrases.necronPhrase()
        await message.channel.send(thePhrase)

    if message.content.startswith('!cron'):
        image = theImages.cronImage()
        await message.channel.send(file=discord.File(image))

    if message.content.startswith('!poo'):
        image = theImages.nurgleImage()
        await message.channel.send(file=discord.File(image))
        thePhrase = phrases.nurglePhrase()
        await message.channel.send(thePhrase)

    if message.content.startswith('!gk'):
        image = theImages.gkImage()
        await message.channel.send(file=discord.File(image))
        thePhrase = phrases.greyPhrase()
        await message.channel.send(thePhrase)

    if message.content.startswith('!commands'):
        await message.channel.send('My useable commands so far are: !gk, !poo, !nurgle, !necron, !cron, !tzeentch, $best')

    if message.content.startswith('!jerry'):
        quote = phrases.jerryPhrase()
        await message.channel.send(quote)

    if message.content.startswith('!dump'):
        string = message.content
        words = string.split()
        picture = theImages.pooImage(words)
        await message.channel.send(picture)

    if 'nigger' in message.content:
        await message.delete()
        sentence = phrases.insult()
        await message.channel.send(sentence)


client.run(token)
