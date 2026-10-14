import requests
import time

# Basis-URL der API
API_BASE = "http://localhost:8081/api"

# Listen zur Speicherung der Benutzernamen und Tokens
users = []
tokens = []

# Zeitstempel wird zur Namensgebung genutzt, um Duplikate zu vermeiden
timestamp = int(time.time())

# Schleife zur Erstellung von 20 Testbenutzern
for i in range(1, 21):
    # Einzigartigen Benutzernamen mit Index und Zeitstempel erstellen
    username = f"user{i}_{timestamp}"
    email = f"{username}@example.com"
    password = "Test123"  # Standard-Passwort für alle Testbenutzer

    # Anfrage zum Registrieren des Benutzers senden
    r = requests.post(f"{API_BASE}/users", json={
        "user": {
            "username": username,
            "email": email,
            "password": password
        }
    })

    # Überprüfen, ob die Registrierung erfolgreich war
    if r.status_code == 200:
        print(f"Nutzer {username} erstellt")
    else:
        print(f"Fehler bei {username}: {r.status_code}")
        continue    # Bei Fehler: überspringen und nächsten Nutzer versuchen

    # Login durchführen, um Token zu erhalten
    login = requests.post(f"{API_BASE}/users/login", json={
        "user": {
            "email": email,
            "password": password
        }
    })

    # Überprüfen, ob der Login erfolgreich war
    if login.status_code == 200:
        # Token aus der Login-Antwort extrahieren
        token = login.json()['user']['token']
        
        # Benutzerdaten und Token in Listen speichern
        tokens.append(token)
        users.append(username)
        print(f"Token gespeichert für {username}")
    else:
        print(f"Login fehlgeschlagen für {username}")

# Alle Benutzer + Tokens in Datei speichern für spätere Nutzung
with open("test_tokens.txt", "w") as f:
    for i in range(len(users)):
        f.write(f"{users[i]},{tokens[i]}\n")

print("Alle Tokens wurden gespeichert in test_tokens.txt")