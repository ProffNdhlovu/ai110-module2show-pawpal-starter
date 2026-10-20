from pawpal_system import Owner, Pet, Scheduler, Task


def make_household() -> tuple[Owner, Pet, Pet]:
    owner = Owner("Jordan")
    mochi = Pet("Mochi", "dog")
    luna = Pet("Luna", "cat")
    owner.add_pet(mochi)
    owner.add_pet(luna)
    return owner, mochi, luna


def test_task_completion_changes_status() -> None:
    task = Task("Feed", "08:00")

    task.mark_complete()

    assert task.completed is True


def test_pet_add_task_increases_task_count() -> None:
    _, mochi, _ = make_household()

    mochi.add_task(Task("Walk", "08:00"))

    assert len(mochi.tasks) == 1


def test_scheduler_sorts_tasks_across_multiple_pets() -> None:
    owner, mochi, luna = make_household()
    mochi.add_task(Task("Walk", "09:00"))
    luna.add_task(Task("Feed", "07:30"))

    sorted_tasks = Scheduler(owner).sort_by_time()

    assert [task.description for task in sorted_tasks] == ["Feed", "Walk"]


def test_scheduler_filters_by_pet_and_detects_conflicts() -> None:
    owner, mochi, luna = make_household()
    mochi.add_task(Task("Walk", "08:00"))
    luna.add_task(Task("Feed", "08:00"))
    scheduler = Scheduler(owner)

    assert [task.description for task in scheduler.filter_tasks(pet_name="Mochi")] == ["Walk"]
    assert len(scheduler.detect_conflicts()) == 1


def test_daily_task_creates_next_occurrence() -> None:
    owner, mochi, _ = make_household()
    task = Task("Medication", "08:00", "daily")
    mochi.add_task(task)

    next_task = Scheduler(owner).mark_task_complete(task)

    assert task.completed is True
    assert next_task is not None
    assert next_task.due_date > task.due_date
    assert len(mochi.tasks) == 2
