import random
import os
import json
import discord
from discord.ext import commands
import asyncio


def swear_sentence():
    start = ["ba", "sa-mi bag pula in", "futu-te in"]

    mid0 = [
        "retardatule",
        "handicapatule",
        "prostule",
        "muist imputit",
        "jegos infect",
        "pula bleaga",
        "muistu pulii",
        "retardat infect",
        "jegos cu sperma la gura",
        "sloboz de cal",
        "cacat de om",
    ]

    mid1 = [
        "fata ta de retardat libidinos",
        "nasu ala stramb de handicapat",
        "ochii tai blegi",
        "nasu ala de raton imputit",
        "fata aia de bulangiu fara viata",
        "ma-ta aia stramba fara dinti",
        "ma-ta aia stramba",
        "familia ma-tii",
        "toata rasa ta de retardati",
        "moaca aia de prost care sugi pula",
        "gaozu tau infect",
        "mutra ta de prost",
        "mutra aia de retardat",
        "gatu ma-tii pana ii iese sperma pe ochi",
        "gaozu ma-tii",
        "gura ta pana iti cad dintii",
    ]

    mid2 = [
        "gatu ala de gazela",
        "gura aia scarboasa",
        "nasu ala stramb",
        "gaozu ala infect",
        "mutra aia de balena",
        "gura de retardat",
        "mormantu ma-tii",
        "gatu ala de sobolan",
        "ochii aia beliti",
    ]

    mid = [mid0, mid1, mid2]

    end = [
        "fute-m-as pe rasa ma-tii",
        "sa-ti bag toata pula pe gat",
        "te fut in gura iti dau muie si mi-o si sugi",
        "baga-ti-as pula pe nas",
        "handicapat infect",
        "sa-mi bag pula in rasa ma-tii",
        "retardat handicapat",
        "manca-mi-ai coaiele",
        "baga-te-as in mormant",
        "sa ma fut in gatu ma-tii",
        "sa-mi bag pula in ce ai mai sfant",
        "sa iti iau toata rasa in pula",
        "sa iti trag chilotii pe ochi",
        "baga-mi-as pula in gatu tau de orfan",
        "manca-mi-ai toata pula libidinosule",
        "fute-m-as pe toata familia ta",
    ]

    result = random.choice([0, 1, 2])
    result_start = start[result]
    result_mid = random.choice(mid[result])
    result_end = random.choice(end)
    x = f"{result_start} {result_mid} {result_end}"

    return x


def compliment_sentence():

    start = ["ba frate", "sa mor io", "te"]

    mid0 = [
        "esti cel mai smeker om de pe pamantu asta",
        "esti bazat rau sa moara mama",
        "sa-mi bag pula coaie te iubesc",
        "esti atat de smeker",
        "sunt erect dupa tine",
        "m-ai facut fleasca",
    ]

    mid1 = [
        "de nu esti cel mai smeker om",
        "coaie esti atat de bazat sa-mi bag pula",
        "de nu te respect",
        "esti un om fara egal coaie",
    ]

    mid2 = [
        "respect profund coaie",
        "respect din suflet",
        "iubesc sa mor io",
    ]

    mid = [mid0, mid1, mid2]

    # end = [
    #     "sa"
    # ]

    result = random.choice([0, 1, 2])
    result_start = start[result]
    result_mid = random.choice(mid[result])
    # result_end = random.choice(end)
    x = f"{result_start} {result_mid}"

    return x


def init_file(file_path: str, content: str):
    print(f"initalizing file: ", file_path)

    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(content)
            print(f"{file_path} created successfully.")
    else:
        print(f"{file_path} already exists.")


def init_folder(folder_path: str):
    print(f"initalizing folder: ", folder_path)
    current_path = os.getcwd()
    os.makedirs(current_path + "/" + folder_path, exist_ok=True)


def add_element_to_array_file(ctx: commands.Context, elem: str, file_path: str):
    full_path = f"files/{ctx.guild.id}/{file_path}"
    file_content = json.load(open(full_path))
    file_content.append(elem)

    with open(full_path, "w") as file:
        json.dump(file_content, file, indent=4)


def remove_element_from_arr_file(ctx: commands.Context, elem: str, file_path: str):
    full_path = f"files/{ctx.guild.id}/{file_path}"
    file_content = json.load(open(full_path))
    file_content.remove(elem)

    with open(full_path, "w") as file:
        json.dump(file_content, file, indent=4)


def save_dict_to_file(_dict: dict, file_path: str):
    with open(file_path, "w") as file:
        json.dump(_dict, file, indent=4)


def add_element_to_dict_file(
    ctx: commands.Context, file_path: str, name: str, content: str
):
    full_path = f"files/{ctx.guild.id}/{file_path}"
    file_content = json.load(open(full_path))
    file_content[name] = content
    save_dict_to_file(file_content, full_path)


def remove_element_from_dict_file(ctx: commands.Context, file_path: str, name: str):
    full_path = f"files/{ctx.guild.id}/{file_path}"
    file_content = json.load(open(full_path))
    if name in file_content.keys():
        del file_content[name]
        save_dict_to_file(file_content, full_path)
        return True

    return False


def get_json_file_content(ctx: commands.Context, file_path: str):
    full_path = f"files/{ctx.guild.id}/{file_path}"
    return json.load(open(full_path))


async def safe_send(ctx, content: str):
    try:
        await ctx.send(content)
    except discord.HTTPException as e:
        if e.status == 429:
            retry_after = int(e.response.headers.get("Retry-After", 5))
            print("Cooldown: ", retry_after)
            await asyncio.sleep(retry_after)
            await ctx.send(content)
