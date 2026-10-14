import requests
import random
import lorem

# Basis-URL der API
API_BASE = "http://localhost:8081/api"

# Lade Benutzer-Tokens aus der vorher gespeicherten Datei
with open("test_tokens.txt", "r") as f:
    user_tokens = [line.strip().split(",") for line in f.readlines()]

# Liste von Tags
tags_pool = ["tech", "life", "dev", "open-source", "fun", "science", "flutter", "vue", "ai", "dotnet"]

# Schleife, um 200 Artikel zu erstellen
for i in range(200):

    # Wähle zufällig einen Benutzer, der den Artikel erstellt
    username, token = random.choice(user_tokens)

     # Titel, Beschreibung und Text des Artikels zufällig generieren
    title = f"Testartikel Nr. {i+1}"
    description = lorem.sentence()
    body = lorem.paragraph()
    tags = random.sample(tags_pool, random.randint(3, 4))    # Wähle 3 bis 4 zufällige Tags aus der Tag-Liste

    # Erstelle Header mit dem Token des Benutzers zur Authentifizierung

    # Header mit Authentifizierung (Token)
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }
    
    # Zusammenstellung der Artikeldaten
    payload = {
        "article": {
            "title": title,
            "description": description,
            "body": body,
            "tagList": tags
        }
    }

    # Sende POST-Anfrage zur Erstellung des Artikels
    r = requests.post(f"{API_BASE}/articles", json=payload, headers=headers)

    # Erfolgs- oder Fehlermeldung in der Konsole ausgeben
    if r.status_code == 200:
        print(f" Artikel {i+1} erfolgreich erstellt")
    else:
        print(f" Fehler bei Artikel {i+1}: {r.status_code}")

print(" Artikel-Erstellung abgeschlossen!")
