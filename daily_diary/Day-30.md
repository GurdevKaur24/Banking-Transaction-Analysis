# Day 30 – Git, GitHub and Project Wrap-up

## Topics Covered
- Introduction to Git and GitHub
- Basic Git commands
- `.gitignore`, `README.md` and `requirements.txt`
- Pushing the project to GitHub
- Problem faced: push timeout with a large file
- Daily diary in the repository
- Final reflection on the training

## Git and GitHub

### Definitions
| Term | Meaning |
|---|---|
| **Git** | A **version control system** that tracks changes in files, so we can see history and go back to older versions |
| **GitHub** | A **website** that stores Git repositories online, so projects can be shared and backed up |
| **Repository (repo)** | A project folder tracked by Git |
| **Commit** | A saved snapshot of changes, with a message |
| **Branch** | A separate line of work; the main branch is usually `main` |
| **Remote** | The online copy of the repository (on GitHub), usually called `origin` |
| **Push** | Upload local commits to GitHub |
| **Pull** | Download changes from GitHub to the computer |

## Basic Git Commands
| Command | Purpose |
|---|---|
| `git init -b main` | Create a new repository with the `main` branch |
| `git status` | Show changed and new files |
| `git add .` | Stage all changes for the next commit |
| `git add file_name` | Stage one file |
| `git commit -m "message"` | Save staged changes with a message |
| `git log --oneline` | Show commit history |
| `git remote add origin URL` | Connect the local repo to GitHub |
| `git push -u origin main` | Upload commits for the first time |
| `git push` | Upload new commits |
| `git pull` | Get the latest changes from GitHub |

## Preparing the Project

### `.gitignore`
Lists files and folders Git should **not** track, such as cache files and editor settings.
```
__pycache__/
*.pyc
.ipynb_checkpoints/
venv/
.venv/
.vscode/
.idea/
Thumbs.db
.DS_Store
```

### `README.md`
The first page people see on GitHub. My README includes:
- Problem statement
- Dataset description
- Project files
- Tools used
- How to run the project
- Key findings, recommendations and limitations
- Dashboard features

### `requirements.txt`
Lists the libraries needed, so anyone can install them with one command:
```
pandas==3.0.3
numpy==2.5.1
matplotlib==3.11.1
seaborn==0.13.2
plotly==6.9.0
streamlit==1.60.0
jupyter
```
```bash
pip install -r requirements.txt
```

## Pushing the Project to GitHub
1. Created an **empty repository** on GitHub (without a README, since the project already had one).
2. Ran these commands in the project folder:

```bash
git init -b main
git add .
git commit -m "Banking transaction pattern analysis: notebook, Streamlit dashboard and data"
git remote add origin https://github.com/GurdevKaur24/Banking-Transaction-Analysis.git
git push -u origin main
```

## Problem Faced: Push Timeout
The first push **failed twice**:
```
error: RPC failed; curl 55 Send failure: Connection was reset
error: RPC failed; HTTP 408 curl 22 The requested URL returned error: 408
```

**Cause:** the project includes `transactions.csv` (about 75 MB). The whole upload was about 23 MB after compression, and the internet connection timed out before it finished.

**Fixes tried:**
1. Increased Git's upload buffer and used HTTP/1.1 for this repository:
   ```bash
   git config http.postBuffer 524288000
   git config http.version HTTP/1.1
   ```
   The push still timed out.
2. **Split the upload into two smaller pushes:**
   - First commit and push: code, notebook, README and the smaller CSV files (about 5 MB)
   - Second commit and push: only `transactions.csv` (about 19.5 MB compressed)

   ```bash
   git add . ':!transactions.csv'
   git commit -m "Add analysis notebook, Streamlit dashboard, README and cleaned data"
   git push -u origin main

   git add transactions.csv
   git commit -m "Add original dataset (1M transactions)"
   git push
   ```
   Both pushes succeeded.

GitHub showed a warning that `transactions.csv` (75.26 MB) is larger than the **recommended 50 MB**. It is still under GitHub's **100 MB limit**, so the file was uploaded. For bigger files, **Git LFS (Large File Storage)** can be used.

## Daily Diary in the Repository
The training diary is stored in the same repository so the project and daily log are together.
```
Banking-Transaction-Analysis/
├── README.md
├── main.ipynb
├── dash.py
├── requirements.txt
├── .streamlit/config.toml
├── transactions.csv
├── transactions_sample.csv
├── cleaned_transactions.csv
└── daily_diary/
    ├── day-01.md
    ├── ...
    └── day-30.md
```
- Git does not track empty folders, so a hidden `.gitkeep` file was used to add the empty `daily_diary` folder first.
- Each day is a separate Markdown file, and screenshots are stored in `daily_diary/images/` and linked with:
  ```markdown
  ![Day 2 examples](images/day-02-example.png)
  ```

## Final Project Summary
| Part | Details |
|---|---|
| Topic | Banking Transaction Pattern Analysis |
| Data | 1,000,000 transactions; random sample of 100,000 |
| Analysis | Data cleaning, EDA, customer behaviour, fraud rate analysis |
| Main finding | Fraud rate is about 3% and similar across categories, time and amount; groceries is slightly highest (3.24%) |
| Notebook | `main.ipynb` with observations, findings, recommendations and limitations |
| Dashboard | Streamlit + Plotly, black and orange/red theme, filters, KPIs, fraud pattern charts, insights |
| Repository | github.com/GurdevKaur24/Banking-Transaction-Analysis |

## Reflection on the Training
- **Python** (Days 1–13): data types, data structures, functions, lambda, recursion and OOP gave me a strong programming base.
- **Libraries** (Days 14–16): Pandas for data handling, Matplotlib and Seaborn for charts.
- **SQL** (Days 17–20): SQL commands, joins, aggregate functions and connecting MySQL with Python.
- **Excel** (Days 21–23): formulas, lookups, pivot tables, charts and conditional formatting.
- **Project** (Days 24–30): applied everything to a real analysis, from sampling and cleaning to EDA, fraud analysis, a dashboard and GitHub.


## Key Takeaway
Git tracks every change in a project and GitHub shares it online. A good repository has a clear README, a requirements file and a `.gitignore`. When the push failed because of a large file and a slow connection, splitting it into smaller pushes solved the problem. This completes my 30-day data analytics training, with a full project, dashboard and daily diary on GitHub.
