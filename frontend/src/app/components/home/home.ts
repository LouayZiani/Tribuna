import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { AsyncPipe } from '@angular/common';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [RouterLink, AsyncPipe],
  templateUrl: './home.html',
  styleUrl: './home.css'
})
export class HomeComponent {
  constructor(public auth: AuthService) {}

  features = [
    { icon: '', title: 'Live Seat Maps', desc: 'Real-time availability for every stadium in Kazakhstan.' },
    { icon: '', title: 'All KPL Matches', desc: 'Browse the full Premier League fixture list.' },
    { icon: '', title: 'Instant Booking', desc: 'Secure your seat in seconds: VIP or Regular.' },
    { icon: '', title: 'Secure Accounts', desc: 'JWT-backed login keeps your tickets safe.' },
  ];
}
