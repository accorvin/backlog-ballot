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
  votedOnIssues: String[];
  selectedIssue: Issue;
  @ViewChild(IssueDetailComponent) issueDetailComponent;
  p: number = 1;

  constructor(private issueService: IssueService,
              private modalService: NgbModal ) { }

  ngOnInit() {
    this.getIssues();
    this.votedOnIssues = JSON.parse(localStorage.getItem('votedOnIssues') || '[]');
    console.log('Issues already voted on: ' + this.votedOnIssues);
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
    this.votedOnIssues.push(issue.jiraKey);
    localStorage.setItem('votedOnIssues', JSON.stringify(this.votedOnIssues));
  }

  getIssues(): void {
    this.issueService.getIssues()
    .subscribe(issues => {
      this.issues = issues.issues;
      console.log(issues.issues);
    });
  }
}
