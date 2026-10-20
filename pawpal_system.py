"""PawPal+ core classes (skeleton based on diagrams/uml.mmd)."""

from dataclasses import dataclass, field
from datetime import date as Date


@dataclass
class Owner:
    """The pet owner; supplies the time limit and preferences the scheduler must respect."""

    name: str
    available_minutes: int
    preferences: dict = field(default_factory=dict)

    def update_preferences(self, preferences: dict) -> None:
        """Merge new preferences into the owner's existing preferences."""
        pass

    def has_time_for(self, duration_minutes: int) -> bool:
        """Return True if the owner has enough available minutes for a task."""
        pass

    def describe(self) -> str:
        """Return a short human-readable summary of the owner."""
        pass


@dataclass
class Pet:
    """The pet that care tasks are planned for."""

    name: str
    species: str
    age: int
    needs: list[str] = field(default_factory=list)

    def add_need(self, need: str) -> None:
        """Record a care need for this pet."""
        pass

    def remove_need(self, need: str) -> None:
        """Remove a care need from this pet."""
        pass

    def describe(self) -> str:
        """Return a short human-readable summary of the pet."""
        pass


@dataclass
class CareTask:
    """A single care activity such as feeding, walking, medication, or grooming."""

    title: str
    duration_minutes: int
    priority: int
    pet: Pet
    preferred_time: str | None = None
    completed: bool = False

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        pass

    def is_eligible(self, preferences: dict) -> bool:
        """Return True if this task fits the owner's preferences."""
        pass

    def describe(self) -> str:
        """Return a short human-readable summary of the task."""
        pass


@dataclass
class DailyPlan:
    """The scheduler's output: which tasks were scheduled, which were skipped, and why."""

    date: Date
    scheduled_tasks: list[tuple[CareTask, str]] = field(default_factory=list)  # (task, start_time)
    skipped_tasks: list[tuple[CareTask, str]] = field(default_factory=list)  # (task, reason)
    total_minutes: int = 0
    explanation: str = ""

    def add_task(self, task: CareTask, start_time: str) -> None:
        """Add a task to the plan at the given start time."""
        pass

    def skip_task(self, task: CareTask, reason: str) -> None:
        """Record a task that was left out of the plan, with the reason."""
        pass

    def remaining_minutes(self) -> int:
        """Return how many of the owner's minutes are still unscheduled."""
        pass

    def display(self) -> str:
        """Return the plan formatted for display in the UI."""
        pass


@dataclass
class Scheduler:
    """Builds a DailyPlan from the owner's constraints and the pet's care tasks."""

    owner: Owner
    pet: Pet
    tasks: list[CareTask] = field(default_factory=list)

    def prioritize_tasks(self) -> list[CareTask]:
        """Return tasks ordered from highest to lowest priority."""
        pass

    def filter_tasks(self) -> list[CareTask]:
        """Return only the tasks that are eligible under the owner's preferences."""
        pass

    def create_plan(self) -> DailyPlan:
        """Build and return a DailyPlan that fits within the owner's available time."""
        pass

    def explain_plan(self) -> str:
        """Return an explanation of why tasks were scheduled or skipped."""
        pass
