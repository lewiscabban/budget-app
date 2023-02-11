from datetime import datetime

import pytest
import strawberry
from budget_tracker.classes import Bill, Budget, BudgetTracker, Income
from budget_tracker.context import BudgetTrackerManager
from budget_tracker.main import schema
from budget_tracker.mutations import Mutation
from strawberry.types import Info


@pytest.mark.asyncio
async def test_budget_tracker(
    budget_tracker: BudgetTracker,
    mutate_add_budget_tracker: str,
    mutate_get_budget_tracker: str,
    budget_tracker_manager: BudgetTrackerManager,
) -> None:
    result = await schema.execute(
        mutate_add_budget_tracker,
        context_value=budget_tracker_manager
    )
    assert result.errors is None
    result = await schema.execute(
        mutate_get_budget_tracker,
        context_value=budget_tracker_manager
    )
    assert result.errors is None


@pytest.mark.asyncio
async def test_budget(
    budget_tracker: BudgetTracker,
    mutate_add_budget: str,
    mutate_get_budget: str,
    mutate_update_budget: str,
    mutate_delete_budget: str,
    mutate_add_budget_tracker: str,
    budget_tracker_manager: BudgetTrackerManager,
) -> None:
    await schema.execute(
        mutate_add_budget_tracker,
        context_value=budget_tracker_manager
    )
    result = await schema.execute(
        mutate_add_budget,
        context_value=budget_tracker_manager
    )
    assert result.errors is None
    result = await schema.execute(
        mutate_get_budget,
        context_value=budget_tracker_manager
    )
    assert result.errors is None
    result = await schema.execute(
        mutate_update_budget,
        context_value=budget_tracker_manager
    )
    assert result.errors is None
    result = await schema.execute(
        mutate_delete_budget,
        context_value=budget_tracker_manager
    )
    assert result.errors is None


@pytest.mark.asyncio
async def test_income(
    budget_tracker: BudgetTracker,
    mutate_add_income: str,
    mutate_get_income: str,
    mutate_update_income: str,
    mutate_delete_income: str,
    mutate_add_budget_tracker: str,
    budget_tracker_manager: BudgetTrackerManager,
) -> None:
    await schema.execute(
        mutate_add_budget_tracker,
        context_value=budget_tracker_manager
    )
    result = await schema.execute(
        mutate_add_income,
        context_value=budget_tracker_manager
    )
    assert result.errors is None
    result = await schema.execute(
        mutate_get_income,
        context_value=budget_tracker_manager
    )
    assert result.errors is None
    result = await schema.execute(
        mutate_update_income,
        context_value=budget_tracker_manager
    )
    assert result.errors is None
    result = await schema.execute(
        mutate_delete_income,
        context_value=budget_tracker_manager
    )
    assert result.errors is None


@pytest.mark.asyncio
async def test_bill(
    budget_tracker: BudgetTracker,
    mutate_add_bill: str,
    mutate_get_bill: str,
    mutate_update_bill: str,
    mutate_delete_bill: str,
    mutate_add_budget_tracker: str,
    budget_tracker_manager: BudgetTrackerManager,
) -> None:
    await schema.execute(
        mutate_add_budget_tracker,
        context_value=budget_tracker_manager
    )
    result = await schema.execute(
        mutate_add_bill,
        context_value=budget_tracker_manager
    )
    assert result.errors is None
    result = await schema.execute(
        mutate_get_bill,
        context_value=budget_tracker_manager
    )
    assert result.errors is None
    result = await schema.execute(
        mutate_update_bill,
        context_value=budget_tracker_manager
    )
    assert result.errors is None
    result = await schema.execute(
        mutate_delete_bill,
        context_value=budget_tracker_manager
    )
    assert result.errors is None
