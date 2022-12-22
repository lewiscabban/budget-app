from typing import Dict
from strawberry.fastapi import BaseContext

from classes import User


class BudgetTrackerContext(BaseContext):
    """Custom context class for strawberry GraphQL"""

    def __init__(
        self,
        users: Dict[str, User],
    ):
        super().__init__()
        self.users = users


class BudgetTrackerManager():

    def __init__(
        self,
        users: Dict,
    ) -> None:
        self.users = users

    async def get_context(self) -> BudgetTrackerContext:
        return BudgetTrackerContext(
            users=self.users
        )
