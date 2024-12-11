import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class CriticService {
  private baseUrl = 'http://127.0.0.1:5000/api/v1/critics'; // Flask API base URL

  constructor(private http: HttpClient) {}

  generateCritic(movieName: string): Observable<any> {
    return this.http.get(`${this.baseUrl}/generate/${movieName}`);
  }

  translateText(payload: { response_text: string; target_language: string; source_language: string }): Observable<any> {
    return this.http.post(`${this.baseUrl}/translate`, payload);
  }

  playSpeech(payload: { response_text: string; language: string }): Observable<any> {
    return this.http.post(`${this.baseUrl}/speak`, payload);
  }
}
