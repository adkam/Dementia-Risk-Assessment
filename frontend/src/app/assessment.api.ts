import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, map, Observable, of } from 'rxjs';
import { API_URL } from './env';

@Injectable({
  providedIn: 'root',
})
export class AssessmentApi {
  constructor(private http: HttpClient) {}

  // POST
  createAssessment() {
    this.http
      .post(`${API_URL}/assessment`, { title: 'here' })
      .subscribe((assessment) => {
        console.log(assessment);
      });
  }
}