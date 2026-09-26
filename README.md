# Your Name — Portfolio

A responsive Flask portfolio built with HTML and CSS only. All interactions and animations are CSS-based; there is no JavaScript.

## Run locally

1. Open a terminal in this folder.
2. Create and activate a virtual environment if you want an isolated Python install.
3. Install dependencies with `pip install -r requirements.txt`.
4. Start the site with `python app.py`.
5. Open `http://127.0.0.1:5000`.

## Personalize it

- Replace `YOUR NAME`, the introduction, project descriptions, principles, and contact email in `templates/index.html`.
- Replace `public/images/portrait.jpg` with your own image if desired.
- Adjust colors, layout, and motion in `public/css/style.css`.

The current portrait is the image supplied with the request. The three case-study artboards are original CSS illustrations intended as visual placeholders for real project work.

## Deploy to Vercel

Vercel detects the Flask app from `app.py` and installs Flask from `requirements.txt`. The CSS and portrait are in `public/`, which Vercel serves as static files. No `vercel.json` configuration is required.

1. Push this folder to a GitHub repository, or deploy it with the Vercel CLI.
2. Import the repository into Vercel. If the repository contains other folders, set the project root to this portfolio folder.
3. Keep the detected Flask framework and deploy.

Before publishing, replace the sample name, bio, project descriptions, and `hello@example.com` with your own details. The current case-study artboards are visual placeholders, not real client work.
