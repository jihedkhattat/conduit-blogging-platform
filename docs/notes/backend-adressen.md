- Vue3.js

Im Vue3.js-Frontend erfolgt die Konfiguration der Backend-Adresse über die Datei vite.config.ts. Dort ist ein Proxy (leitet Anfragen vom Frontend an das Backend weiter, ohne dass das Frontend die genaue Adresse des Backends kennen muss)
für alle API-Anfragen definiert:


proxy: {
      '/api': {
        changeOrigin: true,
        target: 'http://localhost:8081', // '^http:\/\/(localhost|127\.0\.0\.1|api)(:\d+)?',
        rewrite: path => path.replace(/^\/api/, ''), // Entfernt '/api' aus dem Pfad
      },
    },


Diese Einstellung bewirkt, dass alle HTTP-Anfragen, die mit /api beginnen, automatisch an http://localhost:8081 weitergeleitet werden, das ist die Adresse des ASP.NET-Backends 
und so müssen die Komponenten im Frontend keine vollständigen URLs angeben und bleiben unabhängig von der genauen Serveradresse


- Flutter

Im Flutter-Frontend befindet sich die zentrale Konfiguration der Backend-Adresse in der Datei constant.dart. Dort ist BASE_URL auf die lokale Backend-Adresse gesetzt:

static const BASE_URL = "http://localhost:8081";

Darauf werden in derselben Datei alle weiteren API-Endpunkte wie Login, Registrierung, Artikel, Kommentare usw. definiert :


static const LOGIN = BASE_URL + SUB_URL + "/users/login";
static const ALL_ARTICLES = BASE_URL + SUB_URL + "/articles";


Durch diese zentrale Struktur kann die Backend-Adresse leicht angepasst werden, ohne jede einzelne Komponente ändern zu müssen