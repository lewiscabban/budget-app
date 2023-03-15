import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { Apollo } from 'apollo-angular';

import { GraphQLService } from '../services/graphql.service';

@Component({
    selector: 'app-income',
    templateUrl: './income.component.html',
    styleUrls: ['./income.component.css']
})
export class IncomeComponent implements OnInit {

    budgetTrackerForm: FormGroup;
    incomeForm: FormGroup;
    // budgetForm: FormGroup;

    payRateOptions: string[]

    constructor(
        private graphQL: GraphQLService,
        private fb: FormBuilder
    ) {
        this.budgetTrackerForm = this.fb.group({
            name: [''] // initial value of name input
        });
        this.incomeForm = this.fb.group({
            name: [''], // initial value of name input
            incomeName: [''], // initial value of income name input
            amount: [0], // initial value of amount input
            payDay: [''], // initial value of pay day input
            payRate: [''] // initial value of pay rate input
        });
        this.payRateOptions = ['annually', 'bi-annually', 'quarterly', 'monthly', 'fortnightly', 'weekly', 'daily'];
    }

    ngOnInit(): void {
        
    }

    addBudgetTracker() {
        const name = this.budgetTrackerForm.controls['name'].value;
        this.graphQL.add_budget_tracker(name).subscribe(({data}: any) => {
            console.log(data)
        })
    }

    addIncome() {
        const name = this.incomeForm.controls['name'].value;
        const incomeName = this.incomeForm.controls['incomeName'].value;
        const amount = this.incomeForm.controls['amount'].value;
        const payDay = this.incomeForm.controls['payDay'].value;
        const payRate = this.incomeForm.controls['payRate'].value;
        this.graphQL.add_income(name, incomeName, amount, payDay, payRate).subscribe(({data}: any) => {
            console.log(data)
        })
    }
}
