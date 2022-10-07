import csv


probs = {}

with open("InterviewBitQuestions.csv", "r") as f:
    dictreader = csv.DictReader(f)
    for line in dictreader:
        # if line["avg_time"] in ["easy", "medium", "hard"]:
        #     print(line)
        if line["Title"] not in probs:
            probs[line["Title"]] = {
                "Tag": line["Tag"],
                "Difficulty": line["Difficulty"],
                "Average Time": line["Average Time"],
                "Link": line["Link"],
                "Companies": [line["Company"]],
            }
        else:
            if line["Company"] != "":
                probs[line["Title"]]["Companies"].append(line["Company"])
    f.close()


with open("final" + ".csv", "w", newline="") as output:
    dwriter = csv.DictWriter(
        output, ["Title", "Tag", "Difficulty", "Average Time", "Link", "Companies"]
    )
    dwriter.writeheader()
    for prob in probs:
        dwriter.writerow(
            {
                "Title": prob,
                "Tag": probs[prob]["Tag"],
                "Difficulty": probs[prob]["Difficulty"],
                "Average Time": probs[prob]["Average Time"],
                "Link": probs[prob]["Link"],
                "Companies": ", ".join(probs[prob]["Companies"]),
            }
        )

    output.close()
