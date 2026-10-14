ASP.NET:

- ASP.NET Core ist ein modernes Webframework von Microsoft. Es läuft auf verschiedenen Plattformen und wird verwendet, um Web-APIs und Webseiten zu erstellen. 
In unserem Projekt bildet ASP.NET Core das Backend. Es empfängt Anfragen vom Frontend, verarbeitet sie, spricht mit der Datenbank (SQLite) und liefert passende Antworten über eine REST-API zurück

- ASP.NET Core nutzt Dependency Injection, um Klassen zu verbinden. Die Datenbankanbindung erfolgt mit Entity Framework Core. REST-Controller stellen die 
API-Endpunkte bereit, und mit JWT erfolgt die Authentifizierung der Nutzer

Vue3.js:

- Vue3.js ist ein JavaScript-Framework, mit dem man moderne Webseiten mit einzelnen Komponenten aufbauen kann. Es ist leicht zu lernen und sehr flexibel. 
Vue.js wird im Projekt als Web-Frontend verwendet. Damit können Nutzer Artikel schreiben, Kommentare lesen und ihr Profil bearbeiten

- Die Oberfläche ist aus vielen Komponenten zusammengesetzt. Der Vue Router sorgt für die Navigation zwischen Seiten

Flutter:

- Flutter ist ein Framework von Google, mit dem man Apps für Android und iOS gleichzeitig entwickeln kann. Die Sprache, die dabei verwendet wird, heißt Dart. 
Flutter ist in diesem Projekt das mobile Frontend. Es bietet dieselben Funktionen wie die Webversion, nur eben für Smartphones

- Die App besteht aus sogenannten Widgets. Manche speichern Daten (StatefulWidget), andere nicht (StatelessWidget). Die Navigation zwischen Seiten erfolgt mit 
dem Navigator. API-Aufrufe werden mit http gemacht, und das Layout passt sich automatisch an den Bildschirm an

REST-APIs:

- REST ist eine Art, wie Frontend und Backend miteinander kommunizieren über das Internet und mit einfachen HTTP-Anfragen wie GET oder POST. Im Projekt sprechen
die Frontends (Vue.js und Flutter) über eine REST-API mit dem Backend. Zum Beispiel kann das Frontend einen Artikel abrufen oder einen Kommentar speichern, jeweils durch eine passende Anfrage

Reactive Programming:

- Bei reaktivem Programmieren reagieren Programme automatisch auf Änderungen – zum Beispiel wenn sich Daten ändern, wird die Oberfläche direkt aktualisiert

- In Vue.js wird mit ref und computed gearbeitet, um reaktiv zu sein. In Flutter nutzt man z.B. Bloc, Streams oder setState, damit sich das UI automatisch anpasst