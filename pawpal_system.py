"""Core domain classes for the PawPal+ pet-care scheduler."""

from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class Task:
    """Represent one pet-care activity."""

    description: str
    time: str
    frequency: str = "once"
    completed: bool = False
    pet: "Pet | None" = None
    due_date: date = field(default_factory=date.today)

    def mark_complete(self) -> "Task | None":
        """Mark this task complete and return its next occurrence when recurring."""
        self.completed = True
        if self.frequency == "daily":
            next_date = self.due_date + timedelta(days=1)
        elif self.frequency == "weekly":
            next_date = self.due_date + timedelta(days=7)
        else:
            return None
        return Task(self.description, self.time, self.frequency, pet=self.pet, due_date=next_date)


@dataclass
class Pet:
    """Store identifying information and the pet's care tasks."""

    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet and link the task back to the pet."""
        task.pet = self
        self.tasks.append(task)

    def list_tasks(self) -> list[Task]:
        """Return all tasks belonging to this pet."""
        return list(self.tasks)


@dataclass
class Owner:
    """Manage an owner's pets and provide access to all of their tasks."""

    name: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's household."""
        self.pets.append(pet)

    def get_all_tasks(self) -> list[Task]:
        """Return tasks from every pet in the household."""
        return [task for pet in self.pets for task in pet.list_tasks()]


@dataclass
class Scheduler:
    """Organize and manage tasks across all of an owner's pets."""

    owner: Owner

    def sort_by_time(self, tasks: list[Task] | None = None) -> list[Task]:
        """Return household tasks in chronological HH:MM order."""
        source = self.owner.get_all_tasks() if tasks is None else tasks
        return sorted(source, key=lambda task: task.time)

    def filter_tasks(
        self,
        pet_name: str | None = None,
        completed: bool | None = None,
    ) -> list[Task]:
        """Filter household tasks by pet name and completion status."""
        tasks = self.owner.get_all_tasks()
        if pet_name is not None:
            tasks = [task for task in tasks if task.pet and task.pet.name == pet_name]
        if completed is not None:
            tasks = [task for task in tasks if task.completed is completed]
        return tasks

    def detect_conflicts(self, tasks: list[Task] | None = None) -> list[str]:
        """Return warnings for tasks assigned to the same exact time."""
        ordered = self.sort_by_time(tasks)
        warnings = []
        for index, task in enumerate(ordered):
            for other in ordered[index + 1 :]:
                if task.time != other.time:
                    break
                warnings.append(
                    f"Conflict at {task.time}: {task.description} and {other.description}."
                )
        return warnings

    def mark_task_complete(self, task: Task) -> Task | None:
        """Complete a task and add its next recurring occurrence to the same pet."""
        next_task = task.mark_complete()
        if next_task is not None and task.pet is not None:
            task.pet.add_task(next_task)
        return next_task


CareTask = Task