import { gql } from "apollo-angular"

const mutate_add_budget_tracker = gql`
        mutation AddBudgetTracker($budgetTrackerId: String!) {
            addBudgetTracker(budgetTrackerId: $budgetTrackerId) {
                budgetTrackerName
                incomes {
                  incomeName
                  amount
                  payDay
                  payRate
                }
                bills {
                  billName
                  amount
                  payDay
                  payRate
                }
                budgets {
                  budgetName
                  amount
                  budgetType
                }
            }
        }
    `

const mutate_get_budget_tracker = gql`
        mutation GetBudgetTracker($budgetTrackerId: String!) {
            getBudgetTracker(budgetTrackerId: $budgetTrackerId) {
                budgetTrackerName
                incomes {
                  incomeName
                  amount
                  payDay
                  payRate
                }
                bills {
                  billName
                  amount
                  payDay
                  payRate
                }
                budgets {
                  budgetName
                  amount
                  budgetType
                }
            }
        }
    `

const mutate_add_budget = gql`
        mutation AddBudget($budgetTrackerId: String!, $budgetName: String!, $amount: Float!, $budgetType: String!) {
            addBudget(budgetTrackerId: $budgetTrackerId, budgetName: $budgetName, amount: $amount, budgetType: $budgetType) {
                budgetTrackerName
                incomes {
                  incomeName
                  amount
                  payDay
                  payRate
                }
                bills {
                  billName
                  amount
                  payDay
                  payRate
                }
                budgets {
                  budgetName
                  amount
                  budgetType
                }
            }
        }
    `

const mutate_get_budget = gql`
        mutation GetBudget($budgetTrackerId: String!, $budgetName: String!) {
          getBudget(budgetTrackerId: $budgetTrackerId, budgetName: $budgetName) {
                budgetName
                amount
                budgetType
            }
        }
    `

const mutate_update_budget = gql`
        mutation UpdateBudget($budgetTrackerId: String!, $oldBudgetName: String!, $newBudgetName: String!, $amount: Float!, $budgetType: String!) {
          updateBudget(budgetTrackerId: $budgetTrackerId, oldBudgetName: $oldBudgetName, newBudgetName: $newBudgetName, amount: $amount, budgetType: $budgetType) {
                budgetTrackerName
                incomes {
                  incomeName
                  amount
                  payDay
                  payRate
                }
                bills {
                  billName
                  amount
                  payDay
                  payRate
                }
                budgets {
                  budgetName
                  amount
                  budgetType
                }
            }
        }
    `

const mutate_delete_budget = gql`
        mutation DeleteBudget($budgetTrackerId: String!, $budgetName: String!) {
          deleteBudget(budgetTrackerId: $budgetTrackerId, budgetName: $budgetName) {
                budgetTrackerName
                incomes {
                  incomeName
                  amount
                  payDay
                  payRate
                }
                bills {
                  billName
                  amount
                  payDay
                  payRate
                }
                budgets {
                  budgetName
                  amount
                  budgetType
                }
            }
        }
    `

const mutate_add_income = gql`
        mutation AddIncome($budgetTrackerId: String!, $incomeName: String!, $amount: Float!, $payDay: String!, $payRate: String!) {
            addIncome(budgetTrackerId: $budgetTrackerId, incomeName: $incomeName, amount: $amount, payDay: $payDay, payRate: $payRate) {
                budgetTrackerName
                incomes {
                  incomeName
                  amount
                  payDay
                  payRate
                }
                bills {
                  billName
                  amount
                  payDay
                  payRate
                }
                budgets {
                  budgetName
                  amount
                  budgetType
                }
            }
        }
    `

const mutate_get_income = gql`
        mutation GetIncome($budgetTrackerId: String!, $incomeName: String!) {
          getIncome(budgetTrackerId: $budgetTrackerId, incomeName: $incomeName) {
                incomeName
                pay_rate
                pay_day
                amount
            }
        }
    `

const mutate_update_income = gql`
        mutation UpdateIncome($budgetTrackerId: String!, $oldIncomeName: String!, $newIncomeName: String!, $amount: Float!, $payDay: String!, $payRate: String!) {
          updateIncome(budgetTrackerId: $budgetTrackerId, oldIncomeName: $oldIncomeName, newIncomeName: $newIncomeName, amount: $amount, payDay: $payDay, payRate: $payRate) {
                budgetTrackerName
                incomes {
                  incomeName
                  amount
                  payDay
                  payRate
                }
                bills {
                  billName
                  amount
                  payDay
                  payRate
                }
                budgets {
                  budgetName
                  amount
                  budgetType
                }
            }
        }
    `

const mutate_delete_income = gql`
        mutation DeleteIncome($budgetTrackerId: String!, $incomeName: String!) {
          deleteIncome(budgetTrackerId: $budgetTrackerId, incomeName: $incomeName) {
                budgetTrackerName
                incomes {
                  incomeName
                  amount
                  payDay
                  payRate
                }
                bills {
                  billName
                  amount
                  payDay
                  payRate
                }
                budgets {
                  budgetName
                  amount
                  budgetType
                }
            }
        }
    `

const mutate_add_bill = gql`
        mutation AddBill($budgetTrackerId: String!, $billName: String!, $amount: Float!, $payDay: String!, $payRate: String!) {
            addBill(budgetTrackerId: $budgetTrackerId, billName: $billName, amount: $amount, payDay: $payDay, payRate: $payRate) {
                budgetTrackerName
                incomes {
                  incomeName
                  amount
                  payDay
                  payRate
                }
                bills {
                  billName
                  amount
                  payDay
                  payRate
                }
                budgets {
                  budgetName
                  amount
                  budgetType
                }
            }
        }
    `

const mutate_get_bill = gql`
        mutation GetBill($budgetTrackerId: String!, $billName: String!) {
          getBill(budgetTrackerId: $budgetTrackerId, billName: $billName) {
                billName
                pay_rate
                pay_day
                amount
            }
        }
    `

const mutate_update_bill = gql`
        mutation UpdateBill($budgetTrackerId: String!, $oldBillName: String!, $newBillName: String!, $amount: Float!, $payDay: String!, $payRate: String!) {
          updateBill(budgetTrackerId: $budgetTrackerId, oldBillName: $oldBillName, newBillName: $newBillName, amount: $amount, payDay: $payDay, payRate: $payRate) {
                budgetTrackerName
                incomes {
                  incomeName
                  amount
                  payDay
                  payRate
                }
                bills {
                  billName
                  amount
                  payDay
                  payRate
                }
                budgets {
                  budgetName
                  amount
                  budgetType
                }
            }
        }
    `

const mutate_delete_bill = gql`
        mutation DeleteBill($budgetTrackerId: String!, $billName: String!) {
          deleteBill(budgetTrackerId: $budgetTrackerId, billName: $billName) {
                budgetTrackerName
                incomes {
                  incomeName
                  amount
                  payDay
                  payRate
                }
                bills {
                  billName
                  amount
                  payDay
                  payRate
                }
                budgets {
                  budgetName
                  amount
                  budgetType
                }
            }
        }
    `

export {
  mutate_add_budget_tracker,
  mutate_get_budget_tracker,
  mutate_add_budget,
  mutate_get_budget,
  mutate_update_budget,
  mutate_delete_budget,
  mutate_add_income,
  mutate_get_income,
  mutate_update_income,
  mutate_delete_income,
  mutate_add_bill,
  mutate_get_bill,
  mutate_update_bill,
  mutate_delete_bill,
}
