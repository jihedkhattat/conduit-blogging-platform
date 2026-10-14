import requests
import random
import lorem

API_BASE = "http://localhost:8081/api"

# Lade Benutzer-Tokens aus der vorher gespeicherten Datei
with open("test_tokens.txt", "r") as f:
    user_tokens = [line.strip().split(",") for line in f.readlines()]

# Rufe alle Artikel vom Backend ab (maximal 200)
r = requests.get(f"{API_BASE}/articles?limit=200")
articles = r.json().get("articles", [])


# Wähle zufällig 20 Artikel aus, die kommentiert werden sollen
articles_to_comment = random.sample(articles, 20)


# Durchlaufe alle ausgewählten Artikel
for article in articles_to_comment:
    slug = article["slug"]  # Eindeutiger Bezeichner des Artikels
    comment_count = random.randint(1, 3) # Anzahl der Kommentare für diesen Artikel (zwischen 1 und 3)

    # Erzeuge Kommentare für jeden Artikel
    for _ in range(comment_count):
        comment_text = lorem.sentence() # Erzeuge zufälligen Text als Kommentar
        _, token = random.choice(user_tokens)  # Wähle zufälligen Benutzer aus
        
        # Header mit Authentifizierung (Token)
        headers = {
            "Authorization": f"Token {token}",
            "Content-Type": "application/json"
        }

        # Kommentarinhalt im richtigen Format
        payload = {
            "comment": {
                "body": comment_text
            }
        }

        # Sende POST-Anfrage zum Hinzufügen des Kommentars
        res = requests.post(f"{API_BASE}/articles/{slug}/comments", json=payload, headers=headers)
        
        # Überprüfe, ob das Kommentieren erfolgreich war        
        if res.status_code == 200:
            print("Kommentar erfolgreich gepostet")
        else:
            print(f"Fehler beim Kommentieren: {res.status_code}")

print("Alle Kommentare erstellt")
