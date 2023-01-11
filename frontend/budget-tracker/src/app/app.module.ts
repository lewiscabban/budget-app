import { HttpClientModule } from '@angular/common/http'
import { ApolloModule } from 'apollo-angular'
import { NgModule, CUSTOM_ELEMENTS_SCHEMA  } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { IncomeComponent } from './income/income.component';
import { BudgetComponent } from './budget/budget.component';
import { ConfigServiceProvider } from './providers/config.service.provider';
import { apolloServiceProvider } from './providers/apollo.provider';

@NgModule({
  declarations: [
    AppComponent,
    IncomeComponent,
    BudgetComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ApolloModule,
    HttpClientModule,
  ],
  providers: [
    ConfigServiceProvider,
    apolloServiceProvider,
  ],
  bootstrap: [AppComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class AppModule { }
