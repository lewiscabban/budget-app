import strawberry

from typing import List
from datetime import datetime


@strawberry.type
class Budget:
    budget_id: str
    target: float
    amount: float
    percentage: float


@strawberry.type
class Income:
    income_id: str
    pay_cycle: str
    pay_day: datetime
    amount: float


@strawberry.type
class User:
    user_id: str
    income_streams: List[Income]
    budgets: List[Budget]
