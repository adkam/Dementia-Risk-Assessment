import {
  HttpClient,
  HttpErrorResponse,
  HttpHeaders,
} from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, firstValueFrom, map, Observable, of } from 'rxjs';
import { API_URL } from './env';

@Injectable({
  providedIn: 'root',
})
export class AssessmentApi {
  constructor(private http: HttpClient) {}

  createAssessment() {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      }),
    };
    const request$ = this.http.post(
      `${API_URL}/assessment`,
      {
        age: 18,
      },
      httpOptions
    );
    return firstValueFrom(request$);
  }
}
