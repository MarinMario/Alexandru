import discord
from discord.ext import commands
import json
import utils as utils
import random

env = json.load(open(".env.json"))
token = env["TOKEN"]

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="alex ", intents=intents)

server_vars_path = "server_vars.json"
quotes_path = "quotes.json"
replies_path = "replies.json"
media_path = "media.json"


@bot.event
async def on_ready():
    utils.init_folder("files")
    for guild in bot.guilds:
        server_folder = f"files/{guild.id}"
        print(f"\nServer Name: {guild.name} | Server ID: {guild.id}")
        utils.init_folder(server_folder)
        utils.init_file(f"{server_folder}/{server_vars_path}", "{}")
        utils.init_file(f"{server_folder}/{quotes_path}", "[]")
        utils.init_file(f"{server_folder}/{replies_path}", "{}")
        utils.init_file(f"{server_folder}/{media_path}", "{}")


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.has_permissions(manage_nicknames=True)
async def nume(ctx, member: discord.Member, *args):
    formatted_nickname = " ".join(args)
    await member.edit(nick=formatted_nickname)
    await ctx.send(f"gata acum {member.name} are numele {formatted_nickname}")


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def injura(ctx: commands.Context, member: discord.Member):
    await ctx.send(
        f"{member.mention} {utils.swear_sentence()} {utils.swear_sentence()} {utils.swear_sentence()}"
    )


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def complimenteaza(ctx: commands.Context, member: discord.Member):
    await ctx.send(
        f"{member.mention} {utils.compliment_sentence()} {utils.compliment_sentence()} {utils.compliment_sentence()}"
    )


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def spune(ctx, *args):
    message = " ".join(args)
    await ctx.send(message)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def memoreaza(ctx, *args):
    quote = " ".join(args)
    utils.add_element_to_array_file(ctx, quote, quotes_path)

    await ctx.send("gata am memorat")


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def uita(ctx, *args):
    quote = " ".join(args)
    quotes = utils.get_json_file_content(ctx, quotes_path)
    if quote in quotes:
        utils.remove_element_from_arr_file(ctx, quote, quotes_path)
        await ctx.send("gata am uitat")
    else:
        await ctx.send("nici macar n-am memorat asta")


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def vorbeste(ctx: commands.Context):
    quotes = utils.get_json_file_content(ctx, quotes_path)
    if len(quotes) == 0:
        await ctx.send("n-am memorat nimic")
        return

    random_quote = random.choice(quotes)

    await ctx.send(random_quote)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def memorie(ctx: commands.Context):
    quotes = utils.get_json_file_content(ctx, quotes_path)
    if len(quotes) == 0:
        await ctx.send("n-am memorat nimic")
        return

    str_quotes = "\n".join(quotes)
    await ctx.send(str_quotes)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def raspunde(ctx: commands.Context, *args):

    args_str = " ".join(args)
    if "#" not in args_str:
        await ctx.send(
            "ca sa imi adaugi un raspuns scrie `alex raspunde propozitie#raspuns`"
        )
        return

    args_split = args_str.split("#")
    reply_to = args_split[0]
    reply_with = args_split[1]
    if reply_to == "" or reply_with == "":
        await ctx.send(
            "ca sa imi adaugi un raspuns scrie `alex raspunde propozitie#raspuns`"
        )
        return

    utils.add_element_to_dict_file(ctx, replies_path, reply_to, reply_with)

    await ctx.send("gata asa raspund")


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def sterge_raspuns(ctx: commands.Context, *args):
    sentence = " ".join(args)
    worked = utils.remove_element_from_dict_file(ctx, replies_path, sentence)

    message = f"gata nu mai raspund la {sentence}" if worked else "nu merge"
    await ctx.send(message)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def raspunsuri(ctx: commands.Context):
    replies = utils.get_json_file_content(ctx, replies_path)
    str_replies = ""
    for key in replies:
        str_replies += key + ": " + replies[key] + "\n"

    if str_replies == "":
        str_replies = "nu am raspunsuri"

    await ctx.send(str_replies)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def salveaza_media(ctx: commands.Context, *args):
    name = " ".join(args)
    if not ctx.message.attachments:
        await ctx.send("n-ai pus fisier in mesaj")
        return

    attachment = ctx.message.attachments[0]
    utils.add_element_to_dict_file(ctx, media_path, name, attachment.url)

    await ctx.send("gata am salvat fisierul")


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def sterge_media(ctx: commands.Context, *args):
    name = " ".join(args)
    worked = utils.remove_element_from_dict_file(ctx, media_path, name)

    message = f"gata am sters fisierul {name}" if worked else "nu merge"
    await ctx.send(message)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def media(ctx: commands.Context, *args):
    name = " ".join(args)
    content = utils.get_json_file_content(ctx, media_path)

    if name not in content.keys():
        await ctx.send(f"nu am fisierul {name}")
        return

    await ctx.send(content[name])


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def fisiere_media(ctx: commands.Context):
    content = utils.get_json_file_content(ctx, media_path)
    file_names = "\n".join(content.keys())

    if len(file_names) == 0:
        await ctx.send("n-am fisiere")
        return

    await ctx.send(file_names)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def barbut(ctx: commands.Context):
    choices = [1, 2, 3, 4, 5, 6]
    dice1 = random.choice(choices)
    dice2 = random.choice(choices)

    await ctx.send(f"{ctx.author.mention} ai dat {dice1} {dice2}")


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def a(ctx: commands.context):
    x = random.randint(1, 100)
    message = "a" if x == 1 else x * "A"

    await ctx.send(message)


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def seteaza_welcome(ctx: commands.Context, *args):
    message = " ".join(args)
    utils.add_element_to_dict_file(
        ctx, server_vars_path, "welcome_channel", ctx.channel.id
    )
    utils.add_element_to_dict_file(ctx, server_vars_path, "welcome_message", message)
    await ctx.send("gata asta e canalul de welcome")


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def welcome(ctx: commands.Context):
    server_vars = utils.get_json_file_content(ctx, server_vars_path)
    if "welcome_message" not in server_vars:
        await ctx.send("n-am mesaj de welcome")
    await ctx.send(server_vars["welcome_message"])


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def ajutor(ctx: commands.Context):
    await ctx.send(
        ""
        + "\nComenzi pentru Membrii:"
        + "\n1. Ca sa injuri pe cineva scrie `alex injura @membru`"
        + "\n2. Ca sa complimentezi pe cineva scrie `alex complimenteaza @membru`"
        + "\n3. Ca sa spun ceva scrie `alex spune propozitie`"
        + "\n4. Ca sa spun o propozitie memorata scrie `alex vorbeste`"
        + "\n5. Ca sa dai ca zarul scrie `alex barbut`"
        + "\n6. Ca sa vezi ce am memorat scrie `alex memorie`"
        + "\n7. Ca sa vezi ce pot raspunde scrie `alex raspunsuri`"
        + "\n8. Ca sa postezi fisiere salvate scrie `alex media nume fisier`"
        + "\n9. Ca sa vezi ce fisiere au fost salvate scrie `alex fisiere_media`"
        + "\n10. Ca sa tip AAAAAAAAAAAA scrie `alex a`"
        + "\n11. Ca sa vezi mesajul de welcome scrie `alex welcome`"
        + "\n"
        + "\nComenzi pentru Admini:"
        + "\n1. Ca sa setezi nume la alte persoane scrie `alex nume @membru nume nou`"
        + "\n2. Ca sa memorez ceva scrie `alex memoreaza propozitie`"
        + "\n3. Ca sa uit ceva memorat scrie `alex uita propozitie`"
        + "\n4. Ca sa ma faci sa spun ceva cand vad un anumit cuvant scrie `alex raspunde propozitie#raspuns`"
        + "\n5. Ca sa nu mai raspund la un anumit cuvant scrie `alex sterge_raspuns cuvant`"
        + "\n6. Ca sa salvezi fisiere media scrie `alex salveaza_media nume fisier` si adauga atasamentul"
        + "\n7. Ca sa stergi fisiere salvate scrie `alex sterge_media nume fisier`"
        + "\n8. Ca sa setezi canalul de welcome scrie `alex seteaza_welcome mesaj de welcome` in ce canal vrei"
    )


@bot.event
async def on_member_remove(member: discord.Member):

    server_vars = utils.get_json_file_content(member, server_vars_path)

    if "welcome_channel" not in server_vars:
        print("welcome channel is not configured")
        return

    welcome_channel_id = server_vars["welcome_channel"]
    channel = discord.utils.get(member.guild.channels, id=welcome_channel_id)

    if not channel:
        print("configured welcome channel doesn't exist")
        return

    message = f"🔴 {member.mention} {utils.swear_sentence()} {utils.swear_sentence()} {utils.swear_sentence()}"

    await utils.safe_send(channel, message)
    # await channel.send(message)


@bot.event
async def on_member_join(member: discord.Member):

    server_vars = utils.get_json_file_content(member, server_vars_path)

    if "welcome_message" not in server_vars or "welcome_channel" not in server_vars:
        print("welcome channel is not configured")
        return

    welcome_channel_id = server_vars["welcome_channel"]
    channel = discord.utils.get(member.guild.channels, id=welcome_channel_id)

    if not channel:
        print("configured welcome channel doesn't exist")
        return

    welcome_message = server_vars["welcome_message"]
    message = f"🟢 {member.mention} " + welcome_message

    await utils.safe_send(channel, message)
    # await channel.send(message)


@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return

    lower_msg = message.content.lower()
    if "alex" not in lower_msg:
        return

    replies = utils.get_json_file_content(message, replies_path)

    for key in replies:
        if key.lower() in lower_msg:
            await utils.safe_send(message.channel, replies[key])
            # await message.channel.send(replies[key])

    await bot.process_commands(message)


@bot.event
async def on_command_error(ctx: commands.Context, error):
    if isinstance(error, commands.CommandNotFound):
        print("Command doesn't exist")
        # await utils.safe_send(ctx, "n-am comanda aia, scrie `alex ajutor`")
    if isinstance(error, commands.MissingRequiredArgument):
        await utils.safe_send(ctx, "nu asa se foloseste comanda")
    elif isinstance(error, commands.CommandOnCooldown):
        await utils.safe_send(
            ctx, f"nu spama frate. incearca iar in {error.retry_after:.2f} secunde"
        )
    elif isinstance(error, commands.MissingPermissions):
        await utils.safe_send(ctx, "tu n-ai voie")
    elif isinstance(error, commands.BotMissingPermissions):
        await utils.safe_send(ctx, "n-am permisiuni sa rulez asta")
    else:
        print("some other error")
        # await utils.safe_send(ctx, "nush dc da nu merge")

    print(f"Error: {error}")


bot.run(token)
