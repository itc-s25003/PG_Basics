import csv

li = [
        ["トップガン", "卒業白書", "マイノリティ・レポート"],
        ["タイタニック", "レヴェナント", "インセプション"],
        ["トレーニング デイ", "マイ・ボディーガード", "フライト"]
    ]

with open("output2.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    for item in li:
        w.writerow(item)
