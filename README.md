# 🏓 Ping Pong Game – Python (4 Files)

## Overview

A simple **Ping Pong** game built in **Python** using the built‑in **turtle** graphics module. The project is split into four files (`main.py`, `paddles.py`, `ball.py`, `score.py`) for better structure and readability.

**Goal of the game:** Hit the ball back with your paddle. If your opponent misses, you score a point.

---

## Features

* Two paddles (left and right) controlled with the keyboard.
* Ball that bounces off walls and paddles.
* Increasing speed when the ball hits a paddle.
* Scoreboard that tracks and displays the points of both players.
* Organized OOP design: `Paddles`, `Ball`, `Score` classes.

---

## Requirements

* Python 3.8+
* No external libraries needed (only Python’s built‑in `turtle`).

---

## How to Run

```bash
python main.py
```

---

## Project Structure

```text
pong/
├─ main.py       # Main game loop: screen setup, event listeners, collisions
├─ paddles.py    # Paddle class: create and move paddles (left & right)
├─ ball.py       # Ball class: handles movement, reset, speed increase
└─ score.py      # Score class: display and update player scores
```

---

## How It Works

* **main.py:** Creates the game window, paddles, ball, and scoreboard. Contains the game loop that updates the ball’s position, checks collisions, and updates scores.
* **paddles.py (Paddles):** A class for the paddle objects. Each paddle can move up or down with keyboard input.
* **ball.py (Ball):** A class for the ball object. Handles movement, resetting to the center, and gradually increasing speed.
* **score.py (Score):** A class to keep track of and display the score. Provides methods to add points to either the left or right player.

---

## Controls

* **Right Player:** Arrow keys `Up` and `Down`
* **Left Player:** `W` (up) and `S` (down)

---
