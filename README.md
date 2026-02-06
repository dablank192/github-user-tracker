# github-user-tracker

A simple and interactive Command Line Interface (CLI) tool built with Python to fetch and display recent activities of any GitHub user.

## 🚀 Features

- **Interactive CLI:** Runs in a continuous loop until you decide to exit.
- **Data Filtering:** Specifically extracts the event type and repository information.
- **Smart Linking:** Generates clickable GitHub repository URLs.
- **Error Handling:** Gracefully handles invalid usernames or API connection issues.

## 🛠️ Prerequisites

Before running this project, ensure you have the following installed:
- Python 3.x
- `requests` library

## 📦 Installation

1. **Clone the repository** (or download the source code):
   ```bash
   git clone <your-repo-link>
   cd <your-project-folder>

2. **Set up virtual environment:**
   python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

3. **Install Dependencies: This project requires the requests module.**
   pip install requests

## 💻 Usage
Follow the on-screen prompt:

- Enter a GitHub username (e.g., torvalds, microsoft).

- View the recent activities (Type, Repo Name, and URL).

- Type exit or quit to stop the program.

