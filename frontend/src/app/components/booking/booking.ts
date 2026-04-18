import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { DatePipe } from '@angular/common';
import { ApiService } from '../../services/api.service';
import { Seat, Match } from '../../interfaces/models';
import { FormsModule } from '@angular/forms';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-booking',
  standalone: true,
  imports: [FormsModule, DatePipe],
  templateUrl: './booking.html',
  styleUrl: './booking.css'
})
export class BookingComponent implements OnInit {
  matchId!: number;
  matchInfo: Match | null = null;
  seats: Seat[] = [];

  selectedSection = '';
  errorMessage = '';
  successMessage = '';
  isLoading = true;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private api: ApiService
  ) {}

  ngOnInit(): void {
    this.matchId = Number(this.route.snapshot.paramMap.get('id'));
    this.api.getMatch(this.matchId).subscribe({
      next: (m) => this.matchInfo = m,
      error: () => {}
    });
    this.loadSeats();
  }

  loadSeats(): void {
    this.isLoading = true;
    this.api.getSeatsByMatch(this.matchId, this.selectedSection || undefined).subscribe({
      next: (data) => {
        this.seats = data;
        this.isLoading = false;
      },
      error: (_: HttpErrorResponse) => {
        this.errorMessage = 'Failed to load seats.';
        this.isLoading = false;
      }
    });
  }

  bookSeat(seatId: number): void {
    this.errorMessage = '';
    this.successMessage = '';
    this.api.bookTicket(this.matchId, seatId).subscribe({
      next: () => {
        this.successMessage = '🎉 Ticket booked successfully!';
        this.loadSeats();
        if (this.matchInfo) this.matchInfo.available_seats--;
      },
      error: () => {
        this.errorMessage = 'Booking failed — seat may already be taken.';
      }
    });
  }

  goBack(): void {
    this.router.navigate(['/matches']);
  }
}
