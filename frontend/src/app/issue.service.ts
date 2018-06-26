import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

import { Issue } from './issue';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class IssueService {

  constructor(private http: HttpClient) { }

  getIssues(): Observable<any> {
    return this.http.get<Issue[]>('http://127.0.0.1:5000/api/issues/all')
      .pipe(
        tap(issues => console.log(`fetched issues`)),
        catchError(this.handleError('getIssues', []))
      );
  }

  voteForIssue(issue: Issue): Observable<any> {
    return this.http.post<Issue>('http://127.0.0.1:5000/api/issues/vote',
      {"issueId": issue.id}, httpOptions).pipe(
      tap(_ => console.log(`Service: Voted for isssue id=$(issue.id}`)),
      catchError(this.handleError<any>('voteForIssue'))
    );
  }

  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      console.error('Error encountered');
      console.error(error); // log to console instead

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }
}
