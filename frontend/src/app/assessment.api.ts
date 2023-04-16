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

  createAssessment(formData: any) {
    const request$ = this.http.post(`${API_URL}/assessment`, formData, {
      responseType: 'text',
    });
    return firstValueFrom(request$);
  }
}
