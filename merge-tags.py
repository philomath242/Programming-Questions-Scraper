import csv

probs = {}

with open("result.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:

        # make a dictionary with number as key
        # value will be dictionary with tags

        # if does not exist in probs make new
        if int(row["number"]) not in probs:
            probs[int(row["number"])] = {
                "title": row["title"],
                "link": row["link"],
                "acceptance": row["acceptance"],
                "difficulty": row["difficulty"],
                "tags": [row["tag"]],
            }
        # if exist then just add tag
        else:
            probs[int(row["number"])]["tags"].append(row["tag"])
            # print(probs[int(row["number"])])


with open("new.csv", "w") as res:
    writer = csv.DictWriter(
        res, fieldnames=["number", "title", "link", "acceptance", "difficulty", "tags"]
    )

    writer.writeheader()

    for prob in probs:
        writer.writerow(
            {
                "number": prob,
                "title": probs[prob]["title"],
                "link": probs[prob]["link"],
                "acceptance": probs[prob]["acceptance"],
                "difficulty": probs[prob]["difficulty"],
                "tags": ", ".join(probs[prob]["tags"]),
            }
        )
