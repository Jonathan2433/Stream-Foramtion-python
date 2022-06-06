import csv
import re

# ouverture du fichier
file = open("BordeauxWines.csv", "r", encoding="utf-8")
# lecture du fichier
reader = csv.reader(file)
# transformation de la data en liste
data = list(reader)


# inititation des variables
total = 0
price_count = 0
without_price_count = 0
price_sum = 0
expensive_wine = []
wine_more_100 = 0
wine_lower_50 = 0
wine_lower_25 = 0
wine_lower_10 = 0
wine_lower_5 = 0


for bottle in data[1:len(data)]:
    # nombre de bouteilles
    total += 1
    # netoie les prix
    if re.match("^\$[0-9]{4}|^\$[0-9]{3}|^\$[0-9]{2}|^\$[0-9]{1}|^\$[0-9]", bottle[3]) and len(bottle[3]) <= 5:
        # compte le nombre de prix aprés nettoyage
        price_count += 1
        # compte le prix total de toutes les bouteilles
        price_sum += float(bottle[3][1:4])
        # variable pour traiter les bouteilles qui ont un prix
        price = float(bottle[3][1:4])
        if price >= 100:
            wine_more_100 += 1
        if price <= 50:
            wine_lower_50 += 1
        if price <= 25:
            wine_lower_25 += 1
        if price <= 10:
            wine_lower_10 += 1
        if price <= 5:
            wine_lower_5 += 1
    else:
        without_price_count += 1


# affichage de nos résultats
print("Bottles witht price :", price_count, " / ", total, "rows")
print("Bottles without price :", without_price_count, " / ", total, "rows")
print("Verif : with price + without price = ", price_count + without_price_count)
print("Average price:", price_sum / price_count)


# affichage de nos résultats
print(wine_more_100, "wines are more expensive than $100")
print(wine_lower_50, "wines are lower expensive than $50")
print(wine_lower_25, "wines are lower expensive than $25")
print(wine_lower_10, "wines are lower expensive than $10")
print(wine_lower_5, "wines are lower expensive than $5")



# fermeture du fichier
file.close()
