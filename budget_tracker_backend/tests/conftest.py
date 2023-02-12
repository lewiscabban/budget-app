from datetime import datetime

import pytest

from budget_tracker_backend.classes import Bill, Budget, BudgetTracker, Income
from budget_tracker_backend.context import BudgetTrackerManager


@pytest.fixture(scope="function")
def income() -> Income:
    return Income(income_name="work", pay_rate="FORTNIGHTLY", pay_day=datetime.now(), amount=2551)


@pytest.fixture(scope="function")
def budget() -> Budget:
    return Budget(budget_name="house savings", amount=500, budget_type="FORTNIGHTLY")


@pytest.fixture(scope="function")
def bill() -> Bill:
    return Bill(bill_name="phone", pay_rate="MONTHLY", pay_day=datetime.now(), amount=74)


@pytest.fixture(scope="function")
def budget_tracker() -> BudgetTracker:
    return BudgetTracker(budget_tracker_name="Lewis", incomes=[], budgets=[], bills=[])


@pytest.fixture(scope="function")
def budget_tracker_manager() -> BudgetTrackerManager:
    return BudgetTrackerManager(budget_trackers={})


@pytest.fixture(scope="function")
def mutate_add_budget_tracker() -> str:
    return """
        mutation {
            addBudgetTracker(budgetTrackerId: "lewis") {
                budgetTrackerName
            }
        }
    """


@pytest.fixture(scope="function")
def mutate_get_budget_tracker() -> str:
    return """
        mutation {
            getBudgetTracker(budgetTrackerId: "lewis") {
                budgetTrackerName
            }
        }
    """


@pytest.fixture(scope="function")
def mutate_add_budget() -> str:
    return """
        mutation {
            addBudget(budgetTrackerId: "lewis", budgetName: "house savings", amount: 500, budgetType: "TOTAL") {
                budgetTrackerName
            }
        }
    """


@pytest.fixture(scope="function")
def mutate_get_budget() -> str:
    return """
        mutation {
            getBudget(budgetTrackerId: "lewis", budgetName: "house savings") {
                budgetName
                amount
                budgetType
            }
        }
    """


@pytest.fixture(scope="function")
def mutate_update_budget() -> str:
    return """
        mutation {
            updateBudget(budgetTrackerId: "lewis", oldBudgetName: "house savings", newBudgetName: "house savings", amount: 500, budgetType: "TOTAL") {
                budgetTrackerName
            }
        }
    """


@pytest.fixture(scope="function")
def mutate_delete_budget() -> str:
    return """
        mutation {
            deleteBudget(budgetTrackerId: "lewis", budgetName: "house savings") {
                budgetTrackerName
            }
        }
    """


@pytest.fixture(scope="function")
def mutate_add_income() -> str:
    return """
        mutation {
            addIncome(budgetTrackerId: "lewis", incomeName: "work", amount: 2551, payDay: "2023-02-04T10:08:10.457310", payRate: "FORTNIGHTLY") {
                budgetTrackerName
            }
        }
    """


@pytest.fixture(scope="function")
def mutate_get_income() -> str:
    return """
        mutation {
            getIncome(budgetTrackerId: "lewis", incomeName: "work") {
                incomeName
            }
        }
    """


@pytest.fixture(scope="function")
def mutate_update_income() -> str:
    return """
        mutation {
            updateIncome(budgetTrackerId: "lewis", oldIncomeName: "work", newIncomeName: "work", amount: 2551, payDay: "2023-02-04T10:08:10.457310", payRate: "FORTNIGHTLY") {
                budgetTrackerName
            }
        }
    """


@pytest.fixture(scope="function")
def mutate_delete_income() -> str:
    return """
        mutation {
            deleteIncome(budgetTrackerId: "lewis", incomeName: "work") {
                budgetTrackerName
            }
        }
    """


@pytest.fixture(scope="function")
def mutate_add_bill() -> str:
    return """
        mutation {
            addBill(budgetTrackerId: "lewis", billName: "phone", amount: 74, payDay: "2023-02-04T10:08:10.457310", payRate: "FORTNIGHTLY") {
                budgetTrackerName
            }
        }
    """


@pytest.fixture(scope="function")
def mutate_get_bill() -> str:
    return """
        mutation {
            getBill(budgetTrackerId: "lewis", billName: "phone") {
                billName
            }
        }
    """


@pytest.fixture(scope="function")
def mutate_update_bill() -> str:
    return """
        mutation {
            updateBill(budgetTrackerId: "lewis", oldBillName: "house savings", newBillName: "house savings", amount: 74, payDay: "2023-02-04T10:08:10.457310", payRate: "FORTNIGHTLY") {
                budgetTrackerName
            }
        }
    """


@pytest.fixture(scope="function")
def mutate_delete_bill() -> str:
    return """
        mutation {
            deleteBill(budgetTrackerId: "lewis", billName: "phone") {
                budgetTrackerName
            }
        }
    """
