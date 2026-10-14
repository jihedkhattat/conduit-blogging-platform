# Teil 3: 50 zufällige Artikel liken

import requests
import random

# Basis-URL der API
API_BASE = "http://localhost:8081/api"

# Lade Benutzer-Tokens aus der vorher gespeicherten Datei
with open("test_tokens.txt", "r") as f:
    user_tokens = [line.strip().split(",") for line in f.readlines()]

# Rufe alle Artikel vom Backend ab (maximal 200)
r = requests.get(f"{API_BASE}/articles?limit=200")
articles = r.json().get("articles", [])

# Gib die Anzahl der gefundenen Artikel aus
print(f"{len(articles)} Artikel gefunden")

# Wähle zufällig 50 Artikel aus, die geliked werden sollen
articles_to_like = random.sample(articles, 50)

# Durchlaufe alle ausgewählten Artikel
for article in articles_to_like:
    slug = article["slug"]  # Eindeutiger Bezeichner des Artikels
    like_count = random.randint(1, 5)   # Anzahl der Likes (zwischen 1 und 5)
    print(f"{slug} wird {like_count} mal geliked")

    # Liken durch zufällige Nutzer
    for _ in range(like_count):
        _, token = random.choice(user_tokens) # Wähle zufälliges Token aus

        # Header mit Authentifizierung (Token)
        headers = {
            "Authorization": f"Token {token}",
            "Content-Type": "application/json"
        }

        # Sende POST-Anfrage, um den Artikel zu liken
        res = requests.post(f"{API_BASE}/articles/{slug}/favorite", headers=headers)
        
        # Überprüfe, ob der Like erfolgreich war
        if res.status_code == 200:
            print("Like erfolgreich")
        else:
            print(f"Fehler beim Liken: {res.status_code}")

print("Alle Likes wurden vergeben")
