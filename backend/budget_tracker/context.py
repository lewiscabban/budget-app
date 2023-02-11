from typing import Dict

from budget_tracker.classes import BudgetTracker
from strawberry.fastapi import BaseContext


class BudgetTrackerContext(BaseContext):
    """Custom context class for strawberry GraphQL"""

    def __init__(
        self,
        budget_trackers: Dict[str, BudgetTracker],
    ):
        super().__init__()
        self.budget_trackers = budget_trackers


class BudgetTrackerManager():

    def __init__(
        self,
        budget_trackers: Dict,
    ) -> None:
        self.budget_trackers = budget_trackers

    async def get_context(self) -> BudgetTrackerContext:
        return BudgetTrackerContext(
            budget_trackers=self.budget_trackers
        )
