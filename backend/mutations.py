import strawberry

from strawberry.types import Info

from context import BudgetTrackerContext
from classes import User, Budget, Income


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_user(self, info: Info[BudgetTrackerContext, None], user_id: str) -> User:
        info.context.users[user_id] = User(user_id=user_id, income_streams=[], budgets=[])
        return info.context.users[user_id]

    @strawberry.mutation
    def get_user(self, info: Info[BudgetTrackerContext, None], user_id: str) -> User:
        return info.context.users[user_id]

    @strawberry.mutation
    def add_budget(self, info: Info[BudgetTrackerContext, None], user_id: str, target: float, amount: float, percentage: float) -> User:
        info.context.users[user_id].budgets.append(Budget(budget_id=user_id, target=target, amount=amount, percentage=percentage))
        return info.context.users[user_id]
