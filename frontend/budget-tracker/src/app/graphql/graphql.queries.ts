import { gql } from "apollo-angular"

const GET_USER = gql`
    mutation {
        getUser(userId: "chatooka") {
            userId
            incomeStreams {
              amount
              payDay
              payCycle
            }
            budgets {
              budgetId
              amount
              target
              percentage
            }
        }
    }
`

export {
    GET_USER,
}
