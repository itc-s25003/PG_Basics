import csv

li = [
        ["Top Gun", "Risky Business", "Minority Report"],
        ["Titanic", "The Revenant", "Inception"],
        ["Training Day", "Man on Fire", "Flight"]
    ]

with open("output.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    for item in li:
        w.writerow(item)
        
