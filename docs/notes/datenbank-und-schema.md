Das Backend erstellt die Datenbank mit Entity Framework Core (EF Core). Dieses Tool hilft dem Programm, mit der Datenbank zu arbeiten, ohne
dass man selbst komplizierte SQL-Befehle schreiben muss.In der Datei Program.cs wird zuerst eine Verbindung zu einer 
sogenannten In-Memory-Datenbank hergestellt, das bedeutet, die Datenbank befindet sich nur im Arbeitsspeicher und ist leer, sobald das Programm beendet wird. Das geschieht mit folgenden Zeilen:  


var connectionString = configuration.GetConnectionString("Sqlite") ?? "Filename=:memory:";
var connection = new SqliteConnection(connectionString);
connection.Open();

Hier schaut Das Programm zuerst nach, ob ein Speicherort für die Datenbank angegeben wurde,
wenn nicht, wird automatisch eine temporäre Datenbank im Arbeitsspeicher erstellt und dann wird die Verbindung zu dieser Datenbank geöffnet


Danach wird EF Core so eingerichtet, dass es mit dieser Datenbank arbeitet. Das steht hier:  

builder.Services.AddDbContext<ConduitContext>(options => { options.UseSqlite(connection); });

und ganz am Ende sagt das Programm mit folgendem Befehl:  

context?.Database.EnsureCreated();

dass die Datenbank, falls sie leer ist, automatisch alle Tabellen erstellen soll. Diese Tabellen entstehen dabei aus dem Code, das alles passiert, sobald 
das Programm gestartet wird. Man muss also keine Datenbank von Hand anlegen, EF Core übernimmt das automatisch im Hintergrund
