# 📝 To-Do App

A simple and interactive To-Do application built with Python, FreeSimpleGUI, and Streamlit.  
Users can add, update, and manage tasks using either a local GUI or a responsive web interface.

---

## 📌 Features

- ✅ Add, edit, and delete tasks
- 🌙 Dark mode and live clock (GUI)
- 🌐 Web interface using Streamlit
- 💾 Persistent task storage via file handling

---

## 🚀 Run the App

### Option 1: Streamlit Web App

> 📢 Recommended for most users

```bash
# Clone the repo
git clone https://github.com/tobifotis/todo_app.git
cd todo_app

# Install dependencies
pip freeze > requirements.txt

# Run the web app
streamlit run web.py
```

### Option 2: Local GUI App

> Requires Python installed locally

```bash
# Run the GUI version
python gui.py
```

### Option 3: Windows Executable (No Python Needed)

- Download the `todo_app.exe` file (built with PyInstaller)
- Double-click to launch the app
- No Python installation required

---

## 📦 Requirements

Install the required libraries:

```bash
pip install streamlit PySimpleGUI
```

Or use:

```bash
pip install -r requirements.txt
```

---

## 🌍 Deployment (Optional)

To deploy the app online:

1. Sign in to [Streamlit Community Cloud](https://streamlit.io/cloud)
2. Click **New app** and select this GitHub repo
3. Set `web.py` as the main file
4. Click **Deploy**

You’ll get a live shareable URL like:  
`https://your-username.streamlit.app`

---

## 📁 Project Structure

```
todo_app/
│
├── cli.py           # (Optional CLI interface)
├── functions.py     # Handles file I/O and task logic
├── gui.py           # FreeSimpleGUI interface
├── web.py           # Streamlit web interface
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Author

[Tobi Emmanuel](https://github.com/tobifotis)
