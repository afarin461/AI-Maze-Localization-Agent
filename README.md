# AI-Maze-Localization-Agent
KNTU AI project: Localization Agent implementing Hypothesis Elimination to track Belief State in a maze (Pygame visualization).

# 🤖 Hypothesis Elimination Maze Localization Agent

[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)](https://www.python.org/) 
[![Pygame](https://img.shields.io/badge/GUI-Pygame-red?logo=pygame)](https://www.pygame.org/news)
[![Academic Project](https://img.shields.io/badge/Academic_Project-KNTU-green)](https://en.kntu.ac.ir/)

---

## 🎯 Project Overview & Academic Context

This project is an implementation for an **Artificial Intelligence (AI) course** at **K. N. Toosi University of Technology (Spring 2024)**.

The objective is to simulate a "lost" **Localization Agent** that must deduce its precise location within a known maze using only its **movement history** and **sensory data** (percepts).

### Core AI Algorithm: Hypothesis Elimination

The agent's "brain" is built around the **Hypothesis Elimination** algorithm, which iteratively refines its **Belief State** (the set of possible locations) until only one consistent position remains.

## 💡 How the Localization Works

The agent maintains `self.possible_locations` (the blue squares in the GUI) representing its current belief.

1.  **Initial State:** The Belief State includes **every open cell** in the maze.
2.  **Move & Percept:** The agent attempts a move and records the resulting **percept** (e.g., `(1, 0, 1, 0)` for walls North and East) at its **true, secret** position.
3.  **Simulation Check:** For *every* initial candidate location, the agent **simulates** the entire movement history.
4.  **Elimination:** If the **simulated percept** at any point does not match the **actual percept** recorded in the history, that initial candidate is **eliminated** (removed from the Belief State).
5.  **Localization:** The process repeats until the Belief State contains only **one location**, meaning the agent is fully localized.

## 🚀 Getting Started

### Prerequisites

You need **Python 3.x** and the **Pygame** library installed.

```bash
# Install Pygame
pip install pygame
