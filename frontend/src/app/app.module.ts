import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { NotificationModule } from 'patternfly-ng/notification';

import { AppComponent } from './app.component';
import { IssuesComponent } from './issues/issues.component';
import { IssueDetailComponent } from './issue-detail/issue-detail.component';

@NgModule({
  declarations: [
    AppComponent,
    IssuesComponent,
    IssueDetailComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    NotificationModule,
    NgbModule.forRoot(),
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
