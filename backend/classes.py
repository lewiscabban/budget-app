import strawberry

from typing import List
from enum import Enum
from datetime import datetime


class PayRate(Enum):
    DAY = "DAY"
    WEEK = "WEEK"
    FORTNIGHT = "FORTNIGHT"
    MONTH = "MONTH"
    QUARTER = "QUARTER"
    YEAR = "YEAR"


class BudgetType(Enum):
    PERCENTAGE = "PERCENTAGE"
    TOTAL = "TOTAL"


@strawberry.type
class Budget:
    name: str
    amount: float
    budget_type: BudgetType


@strawberry.type
class Income:
    name: str
    pay_rate: PayRate
    pay_day: datetime
    amount: float


@strawberry.type
class Bill:
    name: str
    pay_rate: PayRate
    pay_day: datetime
    amount: float


@strawberry.type
class BudgetTracker:
    name: str
    incomes: List[Income]
    budgets: List[Budget]
    bills: List[Bill]
