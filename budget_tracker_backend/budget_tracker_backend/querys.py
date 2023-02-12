import strawberry
from strawberry.types import Info

from budget_tracker_backend.context import BudgetTrackerContext


@strawberry.type
class Query:
    @strawberry.field
    def get_budget_trackers(self, info: Info[BudgetTrackerContext, None]) -> str:
        return "you cannot access all budget trackers, nice try!"
