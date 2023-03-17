from datetime import datetime
from enum import Enum
from typing import List

import strawberry


class PayRate(str, Enum):
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    FORTNIGHTLY = "FORTNIGHTLY"
    MONTHLY = "MONTHLY"
    QUARTERLY = "QUARTERLY"
    BI_ANNUALLY = "BI_ANNUALLY"
    ANNUALLY = "ANNUALLY"


class BudgetType(str, Enum):
    PERCENTAGE = "PERCENTAGE"
    TOTAL = "TOTAL"


@strawberry.type
class Budget:
    budget_name: str
    amount: float
    budget_type: str


@strawberry.type
class Income:
    income_name: str
    pay_rate: str
    pay_day: str
    amount: float


@strawberry.type
class Bill:
    bill_name: str
    pay_rate: str
    pay_day: str
    amount: float


@strawberry.type
class BudgetTracker:
    budget_tracker_name: str
    incomes: List[Income]
    budgets: List[Budget]
    bills: List[Bill]
