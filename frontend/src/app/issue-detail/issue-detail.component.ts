import { Component, OnInit, Input, TemplateRef, ViewChild } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Issue } from '../issue';

@Component({
  selector: 'app-issue-detail',
  templateUrl: './issue-detail.component.html',
  styleUrls: ['./issue-detail.component.css'],
})
export class IssueDetailComponent implements OnInit {

  @Input() issue: Issue;
  @ViewChild('content') content: TemplateRef<any>;

  constructor(private modalService: NgbModal) { }

  ngOnInit() {
  }

  openModal(): void {
    console.log(this.content)
    this.modalService.open(this.content, { centered: true });
  }
}
