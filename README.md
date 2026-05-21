# Public Streamlit Hosting

This folder hosts `copilot.html` inside a Streamlit app that can be deployed publicly on Streamlit Community Cloud.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Deploy publicly for free on Streamlit Community Cloud

Streamlit Community Cloud deploys apps from GitHub and gives them a public `*.streamlit.app` URL.

1. Create a GitHub repository, for example `host-documentation`.
2. Push this folder to that repository.
3. Go to <https://share.streamlit.io/> and sign in with the Streamlit account you want to host from.
4. Connect GitHub if Streamlit asks for access.
5. Click **Create app**.
6. Choose the GitHub repository and branch.
7. Set the main file path to `app.py`.
8. Pick a custom app URL if you want one, then click **Deploy**.

Keep these files in the repository root:

- `app.py`
- `copilot.html`
- `requirements.txt`

## Push commands

If this folder is not already a Git repository:

```bash
git init
git add app.py copilot.html requirements.txt README.md .gitignore
git commit -m "Host documentation on Streamlit"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/host-documentation.git
git push -u origin main
```

Replace `YOUR_GITHUB_USERNAME` with your GitHub username and create the GitHub repository before running the `git remote add` command.

## Free hosting note

Streamlit Community Cloud is free for public apps, but free apps can go to sleep after inactivity. The public URL remains available; when someone opens a sleeping app, Streamlit can wake it back up.
