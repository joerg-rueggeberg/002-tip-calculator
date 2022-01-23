print("Willkommen zum 'Trinkgeld-Rechner'.")
rechnung = float(input("Wie hoch war die Gesamtrechnung? €"))
prozent = int(input("Wie viel Prozent Trinkgeld soll gegeben werden? 10, 12 oder 15? ")) / 100 + 1
personen = int(input("Auf wie viele Personen soll die Rechnung aufgeteilt werden? "))
rechnung_pro = round((rechnung / personen) * prozent, 2)
print(f"Jede:r muss {rechnung_pro}€ zahlen.")