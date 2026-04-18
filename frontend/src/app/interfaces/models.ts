export interface Match {
  id: number;
  home_team: string;
  away_team: string;
  date: string;
  stadium: string;
  city: string;
  total_seats: number;
  available_seats: number;
  vip_price: number;
  regular_price: number;
}

export interface Seat {
  id: number;
  match: number;
  row: string;
  number: number;
  section: 'VIP' | 'Regular';
  is_available: boolean;
}

export interface Ticket {
  id: number;
  match: number;
  seat: number;
  user: number;
  created_at: string;
  match_details: Match;
  seat_details: Seat;
}

export interface SeatAvailability {
  match_id: number;
  total_seats: number;
  available_seats: number;
  vip_available: number;
  regular_available: number;
}

export interface AuthResponse {
  access: string;
  refresh: string;
  username: string;
}
