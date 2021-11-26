#author : vmakar0v
import discord
from discord.ext import commands
import requests
import json


BOT = commands.Bot(command_prefix = '/') # ucan replace the command prefix with what ever u want 
#u cant also change the commands
@BOT.command()
async def corona(ctx):
    #----- GET Request from corona API
    
    req = requests.get("https://coronavirus-19-api.herokuapp.com/countries/morocco")
    json_object = req.json()

    Country = json_object["country"]
    todayCs = json_object["todayCases"]
    Death = json_object["deaths"]
    ppl = json_object["cases"]
    chads = json_object['recovered']
    ac = json_object['active']
    TD = json_object['todayDeaths']
    cr = json_object['critical']
    #------- EMBED

    embed = discord.Embed(
        title = 'CORONA',
        colour = discord.Colour.red(), 
        )
    embed.set_footer(text='RUN!Covid is coming.')
    embed.set_author(name='Mountassir', icon_url='https://www.kofiannanfoundation.org/app/uploads/2020/03/aad20d67-2871_lores.jpg')
    embed.add_field(name = 'Country', value=Country, inline= False)
    embed.add_field(name = 'Cases', value=ppl, inline= False)
    embed.add_field(name = 'Deaths', value=Death, inline= False)
    embed.add_field(name = 'Today Cases', value=todayCs, inline= False)
    embed.add_field(name = 'Critical', value=cr, inline= False)
    embed.add_field(name = 'Active', value=ac, inline= False)
    embed.add_field(name = 'Recovered', value=chads, inline= False)
    embed.add_field(name = 'Today Deaths', value=TD, inline= False)

    await ctx.send(embed=embed)

#------------------------------- STAY HOME , STAY SAFE -------------------------------#
