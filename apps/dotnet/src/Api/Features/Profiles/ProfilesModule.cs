using Microsoft.AspNetCore.Mvc;
using Realworlddotnet.Core.Dto;

namespace Realworlddotnet.Api.Features.Profiles;

public class ProfilesModule : ICarterModule
{
    public void AddRoutes(IEndpointRouteBuilder app)
    {
        var group = app.MapGroup("profiles")
            .RequireAuthorization()
            .WithTags("Profile")
            .IncludeInOpenApi();

        group.MapGet("{username}",
                async Task<Ok<ProfilesEnvelope<ProfileDto>>>
                    (string username, IProfilesHandler profilesHandler, ClaimsPrincipal claimsPrincipal) =>
                {
                    var user = claimsPrincipal.FindFirstValue(ClaimTypes.NameIdentifier);
                    var result = await profilesHandler.GetAsync(username, user, new CancellationToken());
                    return TypedResults.Ok(new ProfilesEnvelope<ProfileDto>(result));
                })
            .WithName("GetProfile");

        group.MapPost("{followUsername}/follow",
                async Task<Ok<ProfilesEnvelope<ProfileDto>>>
                    (string followUsername, IProfilesHandler profilesHandler, ClaimsPrincipal claimsPrincipal) =>
                {
                    var user = claimsPrincipal.FindFirstValue(ClaimTypes.NameIdentifier);
                    var result =
                        await profilesHandler.FollowProfileAsync(followUsername, user!, new CancellationToken());
                    return TypedResults.Ok(new ProfilesEnvelope<ProfileDto>(result));
                })
            .WithName("FollowProfile");

        group.MapDelete("{followUsername}/follow",
                async Task<Ok<ProfilesEnvelope<ProfileDto>>>
                    (string followUsername, IProfilesHandler profilesHandler, ClaimsPrincipal claimsPrincipal) =>
                {
                    var user = claimsPrincipal.FindFirstValue(ClaimTypes.NameIdentifier);
                    var result =
                        await profilesHandler.UnFollowProfileAsync(followUsername, user!, new CancellationToken());
                    return TypedResults.Ok(new ProfilesEnvelope<ProfileDto>(result));
                })
            .WithName("UnfollowProfile");



        // Diese Route ermöglicht es einem angemeldeten Benutzer, ein Profilbild hochzuladen
        group.MapPost("image",
                async Task<IResult>
                    ([FromForm] IFormFile file, ClaimsPrincipal claimsPrincipal, IProfilesHandler profilesHandler, HttpContext context) =>
                {
                    // Zuerst wird geprüft, ob überhaupt eine Datei hochgeladen wurde
                    if (file == null || file.Length == 0)
                        throw new ProblemDetailsException(400, "Keine Datei hochgeladen.");

                    // Es werden nur die Dateiformate JPG, JPEG und PNG akzeptiert
                    var allowedExtensions = new[] { ".jpg", ".jpeg", ".png" };
                    var extension = Path.GetExtension(file.FileName).ToLowerInvariant();

                    // Wenn das hochgeladene Dateiformat nicht erlaubt ist, wird ein Fehler mit Status 400 zurückgegeben
                    if (!allowedExtensions.Contains(extension))
                        throw new ProblemDetailsException(400, "Nur JPG, JPEG und PNG erlaubt.");

                    // Der aktuell angemeldete Benutzer wird aus dem Authentifizierungs-Token ausgelesen
                    var username = claimsPrincipal.FindFirstValue(ClaimTypes.NameIdentifier);

                    // Falls der Benutzer nicht authentifiziert ist, wird 401 Unauthorized zurückgegeben
                    if (string.IsNullOrEmpty(username))
                        throw new ProblemDetailsException(401, "Nicht autorisiert.");

                    // Der Speicherpfad für die hochgeladenen Dateien wird festgelegt
                    var uploadsPath = Path.Combine("wwwroot", "uploads");

                    // Falls das Upload-Verzeichnis noch nicht existiert, wird es automatisch erstellt
                    if (!Directory.Exists(uploadsPath))
                        Directory.CreateDirectory(uploadsPath);

                    // Der Dateiname wird aus dem Benutzernamen und der Dateiendung zusammengesetzt
                    var fileName = $"{username}{extension}";

                    // Der vollständige Speicherpfad der Datei wird erstellt
                    var filePath = Path.Combine(uploadsPath, fileName);

                    // Die hochgeladene Datei wird im Speicherpfad gespeichert
                    using var stream = new FileStream(filePath, FileMode.Create);
                    await file.CopyToAsync(stream);

                    // Die URL zur gespeicherten Datei wird generiert, damit das Frontend das Bild später abrufen kann
                    var imageUrl = $"{context.Request.Scheme}://{context.Request.Host}/uploads/{fileName}";

                    // Die neue Bild-URL wird im Benutzerprofil gespeichert
                    await profilesHandler.UpdateUserImageAsync(username, imageUrl, CancellationToken.None);

                    // Am Ende wird die Bild-URL als Bestätigung an das Frontend zurückgegeben
                    return TypedResults.Ok(new { imageUrl });
                })
            .WithName("UploadProfileImage");


    }
}
