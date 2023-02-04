import strawberry

from strawberry.types import Info

from context import BudgetTrackerContext
from classes import BudgetTracker, Budget, Income


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_user(self, info: Info[BudgetTrackerContext, None], user_id: str) -> BudgetTracker:
        info.context.users[user_id] = BudgetTracker(user_id=user_id, incomes=[], budgets=[], bills=[])
        return info.context.users[user_id]

    @strawberry.mutation
    def get_user(self, info: Info[BudgetTrackerContext, None], user_id: str) -> BudgetTracker:
        return info.context.users[user_id]

    @strawberry.mutation
    def add_budget(self, info: Info[BudgetTrackerContext, None], user_id: str, target: float, amount: float, percentage: float) -> BudgetTracker:
        info.context.users[user_id].budgets.append(Budget(budget_id=user_id, target=target, amount=amount, percentage=percentage))
        return info.context.users[user_id]
