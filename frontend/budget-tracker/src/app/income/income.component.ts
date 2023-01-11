import { Component, OnInit } from '@angular/core';
import { Apollo } from 'apollo-angular';

import { GraphQLService } from '../services/graphql.service';

@Component({
  selector: 'app-income',
  templateUrl: './income.component.html',
  styleUrls: ['./income.component.css']
})
export class IncomeComponent implements OnInit {
  
  userId: string = ""

  constructor(
    private graphQL: GraphQLService
  ) { }

  ngOnInit(): void {
    this.graphQL.getUser().subscribe(({ data, error }: any) => {
      this.userId = data.getUser.userId;
    })
  }
}
