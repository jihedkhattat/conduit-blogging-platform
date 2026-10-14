import requests
import random

# Basis-URL der API
API_BASE = "http://localhost:8081/api"

# Lade Benutzer-Tokens aus der vorher gespeicherten Datei
with open("test_tokens.txt", "r") as f:
    user_tokens = [line.strip().split(",") for line in f.readlines()]

# Wähle 5 zufällige Nutzer aus, die anderen Nutzern folgen sollen
followers = random.sample(user_tokens, 5)

# Für jeden dieser 5 Nutzer
for follower_name, follower_token in followers:
    # Wähle 1 bis 3 andere Nutzer aus, denen gefolgt werden soll (ausschließlich andere)
    other_users = [u for u in user_tokens if u[0] != follower_name]
    followees = random.sample(other_users, random.randint(1, 3))

    print(f"{follower_name} folgt: {[f[0] for f in followees]}")


    # Sende für jeden ausgewählten Nutzer eine Follow-Anfrage
    for followee_name, _ in followees:
        
        # Header mit Authentifizierung (Token)
        headers = {
            "Authorization": f"Token {follower_token}",
            "Content-Type": "application/json"
        }

        # Sende POST-Anfrage an das Backend, um Follow-Beziehung zu erstellen
        res = requests.post(f"{API_BASE}/profiles/{followee_name}/follow", headers=headers)
        
        # Überprüfe, ob die Anfrage erfolgreich war
        if res.status_code == 200:
            print(f"  folgt {followee_name}")
        else:
            print(f"  Fehler beim Folgen von {followee_name}: {res.status_code}")

print("Alle Follower-Beziehungen erstellt")
