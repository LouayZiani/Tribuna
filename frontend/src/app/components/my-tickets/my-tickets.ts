import { Component, OnInit } from '@angular/core';
import { RouterLink } from '@angular/router';
import { DatePipe } from '@angular/common';
import { ApiService } from '../../services/api.service';
import { Ticket } from '../../interfaces/models';

@Component({
  selector: 'app-my-tickets',
  standalone: true,
  imports: [RouterLink, DatePipe],
  templateUrl: './my-tickets.html',
  styleUrl: './my-tickets.css'
})
export class MyTicketsComponent implements OnInit {
  tickets: Ticket[] = [];
  errorMessage = '';
  cancellingId: number | null = null;
  isLoading = true;

  constructor(private api: ApiService) {}

  ngOnInit(): void {
    this.loadTickets();
  }

  loadTickets(): void {
    this.isLoading = true;
    this.errorMessage = '';

    this.api.getMyTickets().subscribe({
      next: (data) => {
        this.tickets = data;
        this.isLoading = false;
      },
      error: () => {
        this.errorMessage = 'Failed to load your tickets. Please try again.';
        this.isLoading = false;
      }
    });
  }

  cancel(ticketId: number): void {
    this.cancellingId = ticketId;
    this.errorMessage = '';

    this.api.cancelTicket(ticketId).subscribe({
      next: () => {
        this.cancellingId = null;
        this.loadTickets();
      },
      error: () => {
        this.cancellingId = null;
        this.errorMessage = 'Failed to cancel ticket. Please try again.';
      }
    });
  }
}
