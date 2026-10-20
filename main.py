from pawpal_system import Owner, Pet, Scheduler, Task


def main() -> None:
    owner = Owner("Jordan")
    mochi = Pet("Mochi", "dog")
    luna = Pet("Luna", "cat")
    owner.add_pet(mochi)
    owner.add_pet(luna)

    mochi.add_task(Task("Morning walk", "08:00", "daily"))
    luna.add_task(Task("Breakfast", "07:30"))
    mochi.add_task(Task("Medication", "08:00"))

    scheduler = Scheduler(owner)
    print("Today's Schedule")
    for task in scheduler.sort_by_time():
        print(f"{task.time} - {task.pet.name}: {task.description}")

    print("\nMochi's tasks")
    for task in scheduler.filter_tasks(pet_name="Mochi"):
        print(f"{task.time} - {task.description}")

    print("\nWarnings")
    for warning in scheduler.detect_conflicts():
        print(warning)

    recurring_task = mochi.tasks[0]
    next_task = scheduler.mark_task_complete(recurring_task)
    print(f"\nRecurring task: {next_task.description} due on {next_task.due_date}")


if __name__ == "__main__":
    main()
