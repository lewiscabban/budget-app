import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';

import { GraphQLService } from '../services/graphql.service';

@Component({
  selector: 'app-tracker',
  templateUrl: './tracker.component.html',
  styleUrls: ['./tracker.component.css']
})
export class TrackerComponent {
    budgetTrackerForm: FormGroup;
    incomeForm: FormGroup;
    budgetForm: FormGroup;
    billForm: FormGroup;

    payRateOptions: string[]
    budgetTypeOptions: string[]

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
        this.budgetForm = this.fb.group({
            name: '',
            budgetName: '',
            amount: 0,
            budgetType: ''
        });
        this.billForm = this.fb.group({
            name: '',
            billName: '',
            amount: 0,
            payDay: '',
            payRate: ""
          });
        this.payRateOptions = ['ANNUALLY', 'BI_ANNUALLY', 'QUARTERLY', 'MONTHLY', 'FORTNIGHTLY', 'WEEKLY', 'DAILY'];
        this.budgetTypeOptions = ['PERCENTAGE', 'TOTAL'];
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

    addBudget() {
        const name = this.budgetForm.controls['name'].value;
        const budgetName = this.budgetForm.controls['budgetName'].value;
        const amount = this.budgetForm.controls['amount'].value;
        const budgetType = this.budgetForm.controls['budgetType'].value;
        this.graphQL.add_budget(name, budgetName, amount, budgetType).subscribe(({data}: any) => {
            console.log(data)
        })
    }

    addBill() {
        const name = this.billForm.controls['name'].value;
        const billName = this.billForm.controls['billName'].value;
        const amount = this.billForm.controls['amount'].value;
        const payDay = this.billForm.controls['payDay'].value;
        const payRate = this.billForm.controls['payRate'].value;
        this.graphQL.add_bill(name, billName, amount, payDay, payRate).subscribe(({data}: any) => {
            console.log(data)
        })
    }
}
