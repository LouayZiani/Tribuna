import { Component, OnInit } from '@angular/core';
import { DatePipe, DecimalPipe } from '@angular/common';
import { ApiService } from '../../services/api.service';
import { Match } from '../../interfaces/models';
import { Router } from '@angular/router';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-matches',
  standalone: true,
  imports: [DatePipe, DecimalPipe],
  templateUrl: './matches.html',
  styleUrl: './matches.css'
})
export class MatchesComponent implements OnInit {
  matches: Match[] = [];
  isLoading = true;
  errorMessage = '';

  constructor(private api: ApiService, private router: Router) {}

  ngOnInit(): void {
    this.api.getMatches().subscribe({
      next: (data) => {
        this.matches = data;
        this.isLoading = false;
      },
      error: (_: HttpErrorResponse) => {
        this.errorMessage = 'Failed to load matches.';
        this.isLoading = false;
      }
    });
  }

  goToBooking(matchId: number): void {
    this.router.navigate(['/booking', matchId]);
  }
}
