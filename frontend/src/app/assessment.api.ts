import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, firstValueFrom, map, Observable, of } from 'rxjs';
import { API_URL } from './env';

@Injectable({
  providedIn: 'root',
})
export class AssessmentApi {
  constructor(private http: HttpClient) {}

  createAssessment() {
    const request$ = this.http.post(`${API_URL}/assessment`, {
      age: 18,
    });
    return firstValueFrom(request$);
  }
}
