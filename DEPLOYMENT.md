# Deployment Instructions

How to publish this profile to `github.com/esammostafa9-cloud`.

## 1. Create the profile repository

Create a **public** repository named exactly:

```
esammostafa9-cloud/esammostafa9-cloud
```

The repository name must match the username exactly — that is what makes GitHub show its README on the profile page. Do **not** initialize it with a README (this folder already has one).

## 2. Commit the files

From this folder:

```bash
git init
git add README.md assets/header.svg assets/footer.svg .github/workflows/snake.yml
git commit -m "Add profile README, animated header/footer, snake workflow"
git branch -M main
git remote add origin https://github.com/esammostafa9-cloud/esammostafa9-cloud.git
git push -u origin main
```

Required layout in the repository:

```
esammostafa9-cloud/
├── README.md
├── assets/
│   ├── header.svg
│   └── footer.svg
└── .github/
    └── workflows/
        └── snake.yml
```

(`REPOSITORIES.md` and `DEPLOYMENT.md` are working documents — you can commit them too or keep them local.)

## 3. Run the snake workflow once

The contribution snake image does not exist until the workflow generates it:

1. Open the repository on GitHub → **Actions** tab.
2. If prompted, click **"I understand my workflows, enable them"**.
3. Select **Generate Contribution Snake** → **Run workflow** → run on `main`.
4. Wait for it to finish (about a minute). It publishes the SVGs to the `output` branch, and the snake section in the README starts rendering. It then refreshes automatically every day at 00:00 UTC.

If the run fails with a permissions error: **Settings → Actions → General → Workflow permissions → Read and write permissions → Save**, then re-run.

## 4. Verify the profile

- Open `https://github.com/esammostafa9-cloud` and confirm the header, typing animation, badges, analytics cards, and snake all render.
- The stats/analytics cards are served by public third-party instances (Vercel deployments); an occasional slow load is normal.
- Update repository links in `README.md` if your actual repo names differ from the suggested names in `REPOSITORIES.md`.

## 5. Apply repository metadata

For each project repository, copy its description, topics, and badges from `REPOSITORIES.md` (repo page → ⚙️ next to About → paste description and topics).
