# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

My initial UML design included four classes required by the project. The `Owner` class stores the owner's name and pets. The `Pet` class stores identifying information and its collection of tasks. The `Task` class represents an activity with a description, scheduled time, frequency, due date, and completion status. Finally, the `Scheduler` class retrieves tasks from the owner, organizes them, and manages scheduling algorithms across all pets.

**b. Design changes**

During implementation, I changed the design from a single-pet care-plan model to the rubric's required multi-pet model. `Owner` now owns a list of pets and provides `get_all_tasks()`, which gives `Scheduler` one reliable source for household-wide operations. I also renamed the activity class to `Task`, added recurrence and due dates, and moved sorting, filtering, conflict detection, and recurrence management into `Scheduler`. These changes make the UML relationships match the working code and allow one schedule to include tasks from multiple pets.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler considers the household's pets, each task's scheduled time, completion status, and recurrence frequency. I treated the owner's task collection as the source of truth, sorted tasks chronologically, and filtered tasks by pet or completion status so the same logic works across multiple pets.

**b. Tradeoffs**

The conflict detector checks exact matching times instead of calculating whether task durations overlap. This keeps the feature easy to understand and produces a useful warning without inventing task durations that are not part of the required `Task` model. A future version could add duration and detect all interval overlaps.

---

## 3. AI Collaboration

**a. How you used AI**

I used the AI assistant to brainstorm the initial classes, review missing relationships, and turn the design into a multi-pet implementation. The most helpful prompts named the exact rubric requirement, such as asking how `Scheduler` should retrieve all tasks from an `Owner` instead of reading from one pet.

**b. Judgment and verification**

I did not keep the earlier single-pet scheduler design because it conflicted with the rubric's multi-pet requirement. I changed the model so `Owner.get_all_tasks()` is the scheduler's source, then verified it with a CLI demo and tests that sort tasks belonging to two different pets.

---

## 4. Testing and Verification

**a. What you tested**

I tested completion status changes, adding a task to a pet, chronological sorting across multiple pets, filtering by pet, exact-time conflict warnings, and daily recurrence. These tests cover the core state change and the scheduler behaviors demonstrated by the CLI.

**b. Confidence**

I am reasonably confident because all five automated tests pass and the CLI demonstrates the full workflow. Next I would test malformed time strings, duplicate task objects, weekly recurrence, and conflicts caused by overlapping durations rather than exact matching times.

---

## 5. Reflection

**a. What went well**

I am most satisfied that the scheduler genuinely works across a household of multiple pets instead of only holding a single pet's tasks.

**b. What you would improve**

I would connect the Streamlit form directly to the new `Owner`, `Pet`, `Task`, and `Scheduler` classes and add task duration so conflict detection could handle overlapping intervals.

**c. Key takeaway**

I learned that the human developer must check whether generated code matches the system relationships and grading requirements, not just whether it runs. Small tests for ownership and multi-pet retrieval exposed design problems that a single happy-path example would have missed.
