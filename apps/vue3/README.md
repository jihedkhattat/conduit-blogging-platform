# Conduit web client (Vue 3 + TypeScript)

Web frontend of the Conduit platform. See the [main README](../../README.md) for the full picture.

```bash
npm ci
npm run dev        # http://localhost:5173, proxies /api to http://localhost:8081
npm run build      # type-check + production build
npm run test:e2e   # Cypress end-to-end tests (API and dev server must be running)
```

Based on the MIT-licensed RealWorld Vue 3 example (see `LICENSE`).
