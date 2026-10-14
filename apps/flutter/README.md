# Conduit mobile app (Flutter)

Cross-platform client of the Conduit platform (BLoC architecture). See the [main README](../../README.md) for the full picture.

```bash
flutter pub get
flutter run -d chrome   # or an emulator / device
flutter test
```

The API address is configured in `lib/config/constant.dart` (`BASE_URL`, default `http://localhost:8081`).
On the Android emulator, use `http://10.0.2.2:8081` instead.
