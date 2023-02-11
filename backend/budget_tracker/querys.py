import strawberry
from budget_tracker.context import BudgetTrackerContext
from strawberry.types import Info


@strawberry.type
class Query:
    @strawberry.field
    def get_budget_trackers(self, info: Info[BudgetTrackerContext, None]) -> str:
        return "you cannot access all budget trackers, nice try!"
