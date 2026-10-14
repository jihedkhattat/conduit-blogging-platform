# Conduit API (ASP.NET Core 7)

REST backend of the Conduit platform. See the [main README](../../README.md) for the full picture.

```bash
cd src/Api
dotnet run --urls http://localhost:8081
```

- Base URL: `http://localhost:8081/api`
- Swagger UI: `http://localhost:8081/api/swagger`
- Tests: `dotnet test` (run from this folder)

Run the API from `src/Api`. The SQLite database (`../../realworld.db`) and the image upload folder
(`wwwroot/uploads`) are resolved relative to that folder.

Based on the MIT-licensed RealWorld .NET example (see `LICENSE.txt`).
