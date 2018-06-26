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

  readonly backendUrl: String = environment.api

  constructor(private http: HttpClient) { }

  getIssues(): Observable<any> {
    const url = `${this.backendUrl}issues/all`
    return this.http.get<Issue[]>(url)
      .pipe(
        tap(issues => console.log(`fetched issues`)),
        catchError(this.handleError('getIssues', []))
      );
  }

  voteForIssue(issue: Issue): Observable<any> {
    const url = `${this.backendUrl}issues/vote`
    return this.http.post<Issue>(url,
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
