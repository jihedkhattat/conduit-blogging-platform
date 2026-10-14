1. Artikel anlegen

Vue.js nutzt eine komponentenbasierte Architektur mit Methoden wie
onSubmit() und createArticle() direkt in der ArticleForm.vue. Die Daten
werden aus einem Formular gesammelt und per POST-Request über eine
zentrale API-Schicht (api.createArticle()) an das Backend gesendet. Die
Steuerung erfolgt über einfache Methodenaufrufe, während die
Weiterleitung zur Artikeldetailseite direkt in der Komponente passiert.

Flutter hingegen verwendet das BLoC-Pattern. Hier wird durch das Drücken
des \"Publish Article\"-Buttons ein SubmitArticleEvent ausgelöst, das
vom ArticleBloc verarbeitet wird. Die Daten befinden sich in einem
ArticleModel und werden über ein Repository (repo.createArticle(\...))
an das Backend gesendet. Die UI reagiert auf Statusänderungen wie
ArticleSuccessState, um z. B. Navigation oder Erfolgsmeldungen
auszulösen.

Hauptunterschiede: - Vue.js nutzt Methoden in Komponenten; Flutter nutzt
Events, BLoC und States. - Navigation und Zustandsänderungen werden in
Flutter über BlocConsumer und States gesteuert, in Vue.js direkt in der
Methode.

2. Nutzer anlegen (Sign Up)

Vue.js verwendet im Sign-Up-Prozess den UserStore (Pinia oder Vuex), wo
handleAuthAction(\'register\', userData) ausgeführt wird. Diese Methode
ruft ein POST an /api/users auf. Das Formularhandling findet direkt in
der Komponente statt, inklusive Fehleranzeige oder Weiterleitung.

Flutter setzt ebenfalls auf das BLoC-Pattern. Hier wird ein
RegisterSubmitEvent ausgelöst, der im RegisterBloc verarbeitet wird. Die
Registrierung läuft über das Repository (repo.register(\...)), das den
HTTP-Request sendet. Der UI-State wechselt zu RegisterDoneState, sobald
der Server eine erfolgreiche Antwort liefert. Fehler oder
Validierungsprobleme werden ebenfalls über States behandelt.

Hauptunterschiede: - Vue.js verarbeitet alles direkt in der Komponente
und im Store. - Flutter trennt die Logik durch Events, Blocs und
Repositories -- stärker entkoppelt.
