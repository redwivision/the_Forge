# 🎯 THE FORGE — MISSION CONTROL

*"Knowledge is not a library; it is a weapon. Forge it accordingly."*

---

## 🏔️ The Vision: From Choosing to Learning
In our last project ("theONE"), we focused on **Selecting** (picking a movie). 
In "The Forge," we are focusing on **Mastering**. 

The goal is to build a tool that doesn't just show you math problems, but understands **what you know** and **what you don't**. It acts like a digital tutor.

---

## 🏛️ The Architecture: The "Brain" (The Graph)
Since you are learning the ropes, we are going to use a special concept called a **Directed Acyclic Graph (DAG)**. 

### What is a Graph?
Imagine a bunch of dots (we call these **Nodes**) connected by arrows.
- **Node**: A specific topic (e.g., "Addition").
- **Arrow**: A prerequisite (to learn "Multiplication," you must first learn "Addition").

**Why do we do this?**
Because learning isn't a straight line. It's a map. If you fail a Physics problem about "Forces," the system can look at the map and see: *"Ah, he doesn't understand Vectors! Let's go back and fix that first."*

---

## 🗡️ The Forge Cycle: Feedback Loops
Every great piece of software is built on a **Feedback Loop**.
1. **Challenge**: The app gives you a problem.
2. **Action**: You solve it.
3. **Response**: The app says "Correct" or "Incorrect."
4. **Adjustment**: The app updates your "Mastery Score" and picks the next best challenge.

---

## ⚡ Level 1: The Steel Path (The Core Engine)
Our first goal is to build the bare-bones logic. No fancy UI yet—just the "Engine."

### 🛠️ The Roadmap

#### 1. The Domain (The "What")
We need to tell Python what a "Topic" looks like.
- **Topic A**: Prerequisite of Topic B?
- **Mastery Score**: A number from 0 to 100.
- **Problem Bank**: A list of questions for each topic.

#### 2. The Logic (The "How")
We build a simple "Choose Next" algorithm.
> *If Topic A is 100% mastered, unlock Topic B. If not, stay on Topic A.*

#### 3. The Bridge (FastAPI)
Connect our Python logic to the web so our Flutter app can talk to it later.

---

## 🎓 Why This Project?
This project will teach you the 3 most important skills in Software Engineering:
1. **Data Structures**: Using Graphs and Dictionaries to represent knowledge.
2. **State Management**: Tracking a user's progress over time.
3. **Algorithmic Thinking**: Writing code that making "decisions" based on data.

*"Most people write code. You are crafting a mind."*
