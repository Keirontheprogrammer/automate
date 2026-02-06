# Automate

Automate is a lightweight, cross-platform productivity automation tool that monitors distracting applications and gently :) redirects the user back to productive work in this case an IDE.

It currently supports **Linux and Windows** and is designed to be extensible into a full AI-powered personal assistant.

---

## Features

- Cross-platform support (Linux & Windows)
- Monitors running applications in real-time
- Tracks continuous usage time of distracting apps (e.g. VLC...at this point but many finna be added)
- Automatically closes distractions after a configurable time limit
- Launches productive tools such as:
  - Windows Terminal
  - VS Code
  - Linux terminals
- Config-driven behavior (no hardcoding)
- Minimal resource usage
- Clean modular architecture

---

##  How It Works

1. The agent runs in the background after system startup
2. It continuously monitors running processes
3. When a configured distraction app is detected:
   - A timer starts
4. If the app runs continuously beyond the allowed time:
   - The app is terminated
   - One or more productive applications are launched
5. The agent resets and continues monitoring


