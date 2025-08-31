import json

with open("score.json", "r") as f:
    data = json.load(f)
    print(data)

print(data["highscore"])
data["highscore"] = 10
with open("score.json", "w") as f:
    json.dump(data, f, indent=4)