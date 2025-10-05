# AI Pet Designer 🐾

A simple, kid-friendly command-line game where you create a virtual pet, talk to it, and issue fun commands. The game keeps track of your pet’s **happiness** (0–10) and shows it with emoji hearts.

> Script: `pet.py` (English version)

---

## ✨ Features

- **Name & customize** your pet (type + personality).
- **Interactive commands:** talk, sing, play, feed, sleep, bye.
- **Happiness meter** clamped between 0 and 10, visualized with 💖/🤍 hearts.
- **Beginner-friendly**: plain Python, no third-party packages.

---

## 🧰 Requirements

- **Python**: 3.8 or newer  
- **OS**: Works on macOS, Windows, and Linux (terminal/command prompt)

No external libraries needed.

---

## ▶️ How to Run

From a terminal in the folder containing `pet.py`:

```bash
python pet.py
```

If you have multiple Python versions installed:

```bash
python3 pet.py
```

---

## 🎮 How to Play

1. **Start the game** and answer three prompts:
   - Pet name
   - Pet type (e.g., cat, dog, dragon)
   - Personality (e.g., friendly, shy, playful)

2. You’ll see a short intro and a list of available commands.  
3. Type one command at a time and press **Enter**.

The game continues in a loop until you type `bye`.

---

## 🗺️ Commands

| Command | What it does |
|---|---|
| `talk` | Your pet chats with you. |
| `sing` | Your pet sings a tune. |
| `play` | Playtime with your pet. |
| `feed` | Give your pet some food. |
| `sleep` | Let your pet rest. |
| `bye` | Say goodbye and exit the game. |

> The script maintains a simple happiness system and shows it as a bar of hearts after each action. Happiness is kept within **0–10**.

---

## 📸 Example Session

```
💾 Welcome to the AI Pet World!
What do you want to name your pet? Momo
What kind of animal is it? (e.g., cat, dog, dragon) cat
What is its personality? (e.g., friendly, shy, playful) playful

Awesome! You now have a playful cat named Momo! 💾
Momo: Hi! I'm your pet Momo. You can talk to me or ask me to do things.
You can type one of these commands: talk / sing / play / feed / sleep / bye

What do you want me to do?
> play
... (your pet reacts here)
Momo's happiness level: 💖💖💖💖💖💖🤍🤍🤍🤍

> sleep
... (your pet reacts here)
Momo's happiness level: 💖💖💖💖💖🤍🤍🤍🤍🤍

> bye
Momo: Okay, see you next time! I’ll miss you! 💾
🎮 Thanks for playing with your AI pet. Goodbye!
```

*(Exact messages may vary slightly; the script ensures happiness stays in range and displays it visually.)*

---

## 💡 Tips

- Use **short, lowercase** commands exactly as shown (`talk`, `play`, etc.).
- If the pet “doesn’t understand,” recheck the command spelling.
- Great classroom activity: ask students to add new commands (e.g., `dance`, `study`, `joke`) and adjust happiness accordingly.

---

## 🥪 Extending the Game (Optional)

If you want to expand the script:

- Add a **dictionary of commands** mapping to functions.
- Store pet state in a **`Pet` class** (name, type, personality, happiness).
- Persist progress by saving to a **JSON file** between sessions.
- Add **random events** (e.g., weather, visitors) that affect happiness.
- Localize by extracting messages for **i18n**.

---

## 🐍 Troubleshooting

- **`python: command not found`**  
  Install Python from [python.org](https://www.python.org/) and restart your terminal.

- **Windows runs the Microsoft Store**  
  Try `py pet.py` or `python3 pet.py`.

- **Unicode/emoji issues**  
  Use a terminal that supports UTF-8 (most modern terminals do). On Windows, use Windows Terminal or PowerShell.

---

## 📄 License

MIT (or your preferred license). Add a `LICENSE` file if you plan to share publicly.

---

## 🙌 Acknowledgments

- Inspired by classic virtual pet games and designed to be approachable for beginners learning loops, input handling, and simple state management.

