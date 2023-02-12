import { Injectable } from "@angular/core";
import { Apollo } from "apollo-angular";

import { 
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
} from "./graphql.queries";

@Injectable({
    providedIn: "root",
})
export class GraphQLService {
    constructor(private apollo: Apollo) {}

    public add_budget_tracker(budgetTrackerId: String) {
        return this.apollo.mutate({
            mutation: mutate_add_budget_tracker,
            variables: {
                budgetTrackerId: budgetTrackerId,
            }
        })
    }

    public get_budget_tracker(budgetTrackerId: String) {
        return this.apollo.mutate({
            mutation: mutate_get_budget_tracker,
            variables: {
                budgetTrackerId: budgetTrackerId,
            }
        })
    }

    public add_budget(budgetTrackerId: String, budgetName: String, amount: Number, budgetType: String) {
        return this.apollo.mutate({
            mutation: mutate_add_budget,
            variables: {
                budgetTrackerId: budgetTrackerId,
                budgetName: budgetName,
                amount: amount,
                budgetType: budgetType,
            }
        })
    }

    public get_budget(budgetTrackerId: String, budgetName: String) {
        return this.apollo.mutate({
            mutation: mutate_get_budget,
            variables: {
                budgetTrackerId: budgetTrackerId,
                budgetName: budgetName,
            }
        })
    }

    public update_budget(budgetTrackerId: String, budgetName: String, amount: Number, budgetType: String) {
        return this.apollo.mutate({
            mutation: mutate_update_budget,
            variables: {
                budgetTrackerId: budgetTrackerId,
                budgetName: budgetName,
                amount: amount,
                budgetType: budgetType,
            }
        })
    }

    public delete_budget(budgetTrackerId: String, budgetName: String) {
        return this.apollo.mutate({
            mutation: mutate_delete_budget,
            variables: {
                budgetTrackerId: budgetTrackerId,
                budgetName: budgetName,
            }
        })
    }

    public add_income(budgetTrackerId: String, incomeName: String, amount: Number, payDay: String, payRate: String) {
        return this.apollo.mutate({
            mutation: mutate_add_income,
            variables: {
                budgetTrackerId: budgetTrackerId,
                incomeName: incomeName,
                amount: amount,
                payDay: payDay,
                payRate: payRate,
            }
        })
    }

    public get_income(budgetTrackerId: String, incomeName: String) {
        return this.apollo.mutate({
            mutation: mutate_get_income,
            variables: {
                budgetTrackerId: budgetTrackerId,
                incomeName: incomeName,
            }
        })
    }

    public update_income(budgetTrackerId: String, incomeName: String, amount: Number, payDay: String, payRate: String) {
        return this.apollo.mutate({
            mutation: mutate_update_income,
            variables: {
                budgetTrackerId: budgetTrackerId,
                incomeName: incomeName,
                amount: amount,
                payDay: payDay,
                payRate: payRate,
            }
        })
    }

    public delete_income(budgetTrackerId: String, incomeName: String) {
        return this.apollo.mutate({
            mutation: mutate_delete_income,
            variables: {
                budgetTrackerId: budgetTrackerId,
                incomeName: incomeName,
            }
        })
    }

    public add_bill(budgetTrackerId: String, billName: String, amount: Number, payDay: String, payRate: String) {
        return this.apollo.mutate({
            mutation: mutate_add_bill,
            variables: {
                budgetTrackerId: budgetTrackerId,
                billName: billName,
                amount: amount,
                payDay: payDay,
                payRate: payRate,
            }
        })
    }

    public get_bill(budgetTrackerId: String, billName: String) {
        return this.apollo.mutate({
            mutation: mutate_get_bill,
            variables: {
                budgetTrackerId: budgetTrackerId,
                billName: billName,
            }
        })
    }

    public update_bill(budgetTrackerId: String, billName: String, amount: Number, payDay: String, payRate: String) {
        return this.apollo.mutate({
            mutation: mutate_update_bill,
            variables: {
                budgetTrackerId: budgetTrackerId,
                billName: billName,
                amount: amount,
                payDay: payDay,
                payRate: payRate,
            }
        })
    }

    public delete_bill(budgetTrackerId: String, billName: String) {
        return this.apollo.mutate({
            mutation: mutate_delete_bill,
            variables: {
                budgetTrackerId: budgetTrackerId,
                billName: billName,
            }
        })
    }
}