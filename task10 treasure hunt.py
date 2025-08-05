treasure = {    
    "clues": ["beach", "cave", "waterfall"],
    "locations" : {
        "beach" : {
            "items" : ["compass", "shovel"],
            "hint" : "dig here"
        },
        "cave" : {
            "items" : ["lantern","gold coin"],
            "hint" : "look behind the rocks"
        }
    },
    "crews" : ["first mate","navigator"]
}
treasure["crews"].append("cook")
treasure["locations"]["volcano"] = {
    "items" : ["diamond","lava boots"],
    "hint" : "wear protection"
}
treasure["clues"].append("volcano")
treasure["crews"].remove("navigator")
for place,objects in treasure["locations"].items():
    if "gold coin" in objects["items"]:
        print(f"the gold coin is in the {place}")
        objects["items"][0] = "item1"
        objects["items"][1] = "item2"
print(treasure["locations"]["cave"])