import random


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
