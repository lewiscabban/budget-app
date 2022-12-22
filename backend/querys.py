import strawberry

from strawberry.types import Info

from classes import User, Budget, Income
from context import BudgetTrackerContext


@strawberry.type
class Query:
    @strawberry.field
    def get_users(self, info: Info[BudgetTrackerContext, None]) -> str:
        return "you cannot access all users, nice try!"
