# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Implementation Summary

PawPal+ uses four core classes. `Owner` manages multiple `Pet` objects and exposes every task through `get_all_tasks()`. Each `Pet` owns a collection of `Task` objects. `Task` stores a description, `HH:MM` time, frequency, due date, completion status, and assigned pet. `Scheduler` reads tasks from the owner, sorts them by time, filters them by pet or completion status, detects exact-time conflicts, and creates the next occurrence of recurring tasks.

## Building Blocks

The main objects in PawPal+ are:

### Owner

**Attributes:** `name`, `pets`

**Methods:** `add_pet()`, `get_all_tasks()`

The owner provides the time limit and preferences that the scheduler must respect.

### Pet

**Attributes:** `name`, `species`, `tasks`

**Methods:** `add_task()`, `list_tasks()`

The pet identifies who the care tasks are for and records relevant care needs.

### Task

**Attributes:** `description`, `time`, `frequency`, `completed`, `pet`, `due_date`

**Methods:** `mark_complete()`

A care task represents one activity, such as feeding, walking, medication, grooming, or enrichment.

### Scheduler

**Attributes:** `owner`

**Methods:** `sort_by_time()`, `filter_tasks()`, `detect_conflicts()`, `mark_task_complete()`

The scheduler operates across all pets by calling `Owner.get_all_tasks()` rather than reading from one pet.

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## CLI Demo

Run the end-to-end demo with:

```bash
python3 main.py
```

Sample output:

```text
Today's Schedule
07:30 - Luna: Breakfast
08:00 - Mochi: Morning walk
08:00 - Mochi: Medication

Mochi's tasks
08:00 - Morning walk
08:00 - Medication

Warnings
Conflict at 08:00: Morning walk and Medication.

Recurring task: Morning walk due on 2026-10-20
```

## 🧪 Testing PawPal+

Run the test suite with `python3 -m pytest`.

The tests cover task completion, adding tasks to pets, multi-pet sorting, pet filtering, conflict detection, and daily recurrence.

```text
.....                                                                    [100%]
5 passed in 0.01s
```

## Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Sorts all household tasks chronologically. |
| Filtering | `Scheduler.filter_tasks()` | Filters across pets by pet name or completion status. |
| Conflict handling | `Scheduler.detect_conflicts()` | Warns when exact task times collide. |
| Recurring tasks | `Scheduler.mark_task_complete()` | Creates the next daily or weekly occurrence. |

## Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. `main.py` creates Jordan's household with Mochi and Luna.
2. It adds three tasks at different and duplicate times.
3. `Scheduler.sort_by_time()` prints tasks from both pets in chronological order.
4. `Scheduler.filter_tasks()` shows only Mochi's tasks.
5. `Scheduler.detect_conflicts()` prints a warning for the two 08:00 tasks, and recurrence creates tomorrow's walk.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
