import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Match, Seat, Ticket, SeatAvailability } from '../interfaces/models';

const API = 'http://localhost:8000/api';

@Injectable({ providedIn: 'root' })
export class ApiService {
  constructor(private http: HttpClient) {}

  // ── Matches ──────────────────────────────────────────────
  getMatches(): Observable<Match[]> {
    return this.http.get<Match[]>(`${API}/matches/`);
  }

  getMatch(id: number): Observable<Match> {
    return this.http.get<Match>(`${API}/matches/${id}/`);
  }

  // ── Seats ─────────────────────────────────────────────────
  getSeatsByMatch(matchId: number, section?: string): Observable<Seat[]> {
    let params = new HttpParams().set('match', matchId.toString());
    if (section) params = params.set('section', section);
    return this.http.get<Seat[]>(`${API}/seats/`, { params });
  }

  getSeatAvailability(matchId: number): Observable<SeatAvailability> {
    return this.http.get<SeatAvailability>(`${API}/seats/availability/${matchId}/`);
  }

  // ── Tickets ───────────────────────────────────────────────
  getMyTickets(): Observable<Ticket[]> {
    return this.http.get<Ticket[]>(`${API}/tickets/`);
  }

  bookTicket(matchId: number, seatId: number): Observable<Ticket> {
    return this.http.post<Ticket>(`${API}/tickets/`, { match: matchId, seat: seatId });
  }

  cancelTicket(ticketId: number): Observable<void> {
    return this.http.delete<void>(`${API}/tickets/${ticketId}/`);
  }
}
