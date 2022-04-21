import json
import gkeepapi

from types import SimpleNamespace
from pprint import pprint

readyShopList = []


def getWeekDays():
    weekDays = [
        {
            "name": "Monday",
            "recipe": "rec-v003-20-04-2022"
        },
        {
            "name": "Tuesday",
            "recipe": "rec-v003-20-04-2022"
        },
        {
            "name": "Wednesday",
            "recipe": "rec-v003-20-04-2022"
        }
    ]
    return weekDays
    

def getShopList(weekDays):
    shopList = {}

    for day in weekDays:

        recipe = json.load(open(f"recipies/{day.get('recipe')}.json"), object_hook=lambda d: SimpleNamespace(**d))
        recipeIngredients = recipe.main.ingredients

        for ingredient in recipeIngredients:
            if ingredient.category not in shopList:
                shopList[ingredient.category] = {}
                shopList[ingredient.category][ingredient.name] = ingredient.quantity
            else:
                if ingredient.name not in shopList.get(ingredient.category):
                    shopList[ingredient.category][ingredient.name] = ingredient.quantity
                else:
                    shopList[ingredient.category][ingredient.name] += ingredient.quantity

    return shopList


def formatShopList(d):
    for k, v in d.items():
        if isinstance(v, dict):
            readyShopList.append([f"> {k.upper()}:", False])
            formatShopList(v)
        else:
            readyShopList.append([f"{v}x - {k}", False])


def sendToKeep(readyShopList):
    keep = gkeepapi.Keep()
    login = keep.login('ekoalraku@gmail.com', 'xqowtwpkfsyhycar')
    note = keep.createList("Lista Zakupów")

    for item in readyShopList:
        print(item[0])
        if '>' in item[0]:
            topItem = note.add(f"{item[0]}")
            continue
        subItem = note.add(f"{item[0]}")
        topItem.indent(subItem)

    keep.sync()


def main():
    weekDays = getWeekDays()
    shopList = getShopList(weekDays)
    
    formatShopList(shopList)
    sendToKeep(readyShopList)

main()