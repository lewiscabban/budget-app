from datetime import datetime

import strawberry
from strawberry.types import Info

from budget_tracker_backend.classes import Bill, Budget, BudgetTracker, Income
from budget_tracker_backend.context import BudgetTrackerContext


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_budget_tracker(self, info: Info[BudgetTrackerContext, None], budget_tracker_id: str) -> BudgetTracker:
        info.context.budget_trackers[budget_tracker_id] = BudgetTracker(budget_tracker_name=budget_tracker_id, incomes=[], budgets=[], bills=[])
        return info.context.budget_trackers[budget_tracker_id]

    @strawberry.mutation
    def get_budget_tracker(self, info: Info[BudgetTrackerContext, None], budget_tracker_id: str) -> BudgetTracker:
        return info.context.budget_trackers[budget_tracker_id]

    @strawberry.mutation
    def add_budget(self, info: Info[BudgetTrackerContext, None], budget_tracker_id: str, budget_name: str, amount: float, budget_type: str) -> BudgetTracker:
        info.context.budget_trackers[budget_tracker_id].budgets.append(Budget(budget_name=budget_name, amount=amount, budget_type=budget_type))
        return info.context.budget_trackers[budget_tracker_id]

    @strawberry.mutation
    def get_budget(self, info: Info[BudgetTrackerContext, None], budget_tracker_id: str, budget_name: str) -> Budget:
        for budget in info.context.budget_trackers[budget_tracker_id].budgets:
            if budget.budget_name == budget_name:
                return budget
        return {}

    @strawberry.mutation
    def update_budget(self, info: Info[BudgetTrackerContext, None], budget_tracker_id: str, old_budget_name: str, new_budget_name: str, amount: float, budget_type: str) -> BudgetTracker:
        for budget in info.context.budget_trackers[budget_tracker_id].budgets:
            if budget.budget_name == old_budget_name:
                budget.budget_name = new_budget_name
                budget.amount = amount
                budget.budget_type = budget_type
        return info.context.budget_trackers[budget_tracker_id]

    @strawberry.mutation
    def delete_budget(self, info: Info[BudgetTrackerContext, None], budget_tracker_id: str, budget_name: str) -> BudgetTracker:
        for budget in info.context.budget_trackers[budget_tracker_id].budgets:
            if budget.budget_name == budget_name:
                info.context.budget_trackers[budget_tracker_id].budgets.remove(budget)
                return info.context.budget_trackers[budget_tracker_id]
        return info.context.budget_trackers[budget_tracker_id]

    @strawberry.mutation
    def add_income(self, info: Info[BudgetTrackerContext, None], budget_tracker_id: str, income_name: str, amount: float, pay_rate: str, pay_day: str) -> BudgetTracker:
        info.context.budget_trackers[budget_tracker_id].incomes.append(Income(income_name=income_name, amount=amount, pay_rate=pay_rate, pay_day=pay_day))
        return info.context.budget_trackers[budget_tracker_id]

    @strawberry.mutation
    def get_income(self, info: Info[BudgetTrackerContext, None], budget_tracker_id: str, income_name: str) -> Income:
        for income in info.context.budget_trackers[budget_tracker_id].incomes:
            if income.income_name == income_name:
                return income
        return {}

    @strawberry.mutation
    def update_income(self, info: Info[BudgetTrackerContext, None], budget_tracker_id: str, old_income_name: str, new_income_name: str, amount: float, pay_rate: str, pay_day: str) -> BudgetTracker:
        for income in info.context.budget_trackers[budget_tracker_id].incomes:
            if income.income_name == old_income_name:
                income.income_name = new_income_name
                income.amount = amount
                income.pay_rate = pay_rate
                income.pay_day = pay_day
        return info.context.budget_trackers[budget_tracker_id]

    @strawberry.mutation
    def delete_income(self, info: Info[BudgetTrackerContext, None], budget_tracker_id: str, income_name: str) -> BudgetTracker:
        for income in info.context.budget_trackers[budget_tracker_id].incomes:
            if income.income_name == income_name:
                info.context.budget_trackers[budget_tracker_id].incomes.remove(income)
                return info.context.budget_trackers[budget_tracker_id]
        return info.context.budget_trackers[budget_tracker_id]

    @strawberry.mutation
    def add_bill(self, info: Info[BudgetTrackerContext, None], budget_tracker_id: str, bill_name: str, amount: float, pay_rate: str, pay_day: datetime) -> BudgetTracker:
        info.context.budget_trackers[budget_tracker_id].bills.append(Bill(bill_name=bill_name, amount=amount, pay_rate=pay_rate, pay_day=pay_day))
        return info.context.budget_trackers[budget_tracker_id]

    @strawberry.mutation
    def get_bill(self, info: Info[BudgetTrackerContext, None], budget_tracker_id: str, bill_name: str) -> Bill:
        for bill in info.context.budget_trackers[budget_tracker_id].bills:
            if bill.bill_name == bill_name:
                return bill
        return {}

    @strawberry.mutation
    def update_bill(self, info: Info[BudgetTrackerContext, None], budget_tracker_id: str, old_bill_name: str, new_bill_name: str, amount: float, pay_rate: str, pay_day: datetime) -> BudgetTracker:
        for bill in info.context.budget_trackers[budget_tracker_id].bills:
            if bill.bill_name == old_bill_name:
                bill.bill_name = new_bill_name
                bill.amount = amount
                bill.pay_rate = pay_rate
                bill.pay_day = pay_day
        return info.context.budget_trackers[budget_tracker_id]

    @strawberry.mutation
    def delete_bill(self, info: Info[BudgetTrackerContext, None], budget_tracker_id: str, bill_name: str) -> BudgetTracker:
        for bill in info.context.budget_trackers[budget_tracker_id].bills:
            if bill.bill_name == bill_name:
                info.context.budget_trackers[budget_tracker_id].bills.remove(bill)
                return info.context.budget_trackers[budget_tracker_id]
        return info.context.budget_trackers[budget_tracker_id]
