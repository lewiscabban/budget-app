import { gql } from "apollo-angular"

const GET_USERS = gql`
    query {
        getUsers {
            userId
        }
    }
`

export {
    GET_USERS,
}
