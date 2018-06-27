import { Component, OnInit, ViewChild } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

import { Issue } from '../issue';
import { IssueService } from '../issue.service';
import { IssueDetailComponent } from '../issue-detail/issue-detail.component';

@Component({
  selector: 'app-issues',
  templateUrl: './issues.component.html',
  styleUrls: ['./issues.component.css'],
})
export class IssuesComponent implements OnInit {

  issues: Issue[];
  selectedIssue: Issue;
  @ViewChild(IssueDetailComponent) issueDetailComponent;

  constructor(private issueService: IssueService,
              private modalService: NgbModal ) { }

  ngOnInit() {
    this.getIssues();
  }

  onSelect(issue: Issue, content): void {
    this.selectedIssue = issue;
    this.issueDetailComponent.openModal();
  }

  onVote(event, issue: Issue): void {
    event.stopPropagation();
    this.issueService.voteForIssue(issue)
    .subscribe(issues => {
      this.issues = issues.issues;
      console.log('Voted for issue');
    });
  }

  getIssues(): void {
    this.issueService.getIssues()
    .subscribe(issues => {
      this.issues = issues.issues;
      console.log(issues.issues);
    });
  }
}
