import { Injectable } from "@angular/core";
import { Apollo } from "apollo-angular";

import { GET_USER } from "./graphql.queries";

@Injectable({
    providedIn: "root",
})
export class GraphQLService {
    constructor(private apollo: Apollo) {}

    public getUser() {
        return this.apollo.mutate({
            mutation: GET_USER,
        })
    }
}