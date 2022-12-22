import { Component, OnInit } from '@angular/core';
import { Apollo } from 'apollo-angular';

import { GET_USERS } from '../graphql/graphql.queries';

@Component({
  selector: 'app-income',
  templateUrl: './income.component.html',
  styleUrls: ['./income.component.css']
})
export class IncomeComponent implements OnInit {
  
  userId: string = ""

  constructor(
    private apollo: Apollo,
  ) { }

  ngOnInit(): void {
      this.apollo.query({
      query: GET_USERS,
    }).subscribe(({ data, error }: any) => {
      this.userId = data.getUsers.userId;
    })
  }
}
