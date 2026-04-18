import { Routes } from '@angular/router';
import { authGuard } from './guards/auth.guard';

export const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  {
    path: 'home',
    loadComponent: () => import('./components/home/home').then(m => m.HomeComponent)
  },
  {
    path: 'login',
    loadComponent: () => import('./components/login/login').then(m => m.LoginComponent)
  },
  {
    path: 'matches',
    loadComponent: () => import('./components/matches/matches').then(m => m.MatchesComponent),
    canActivate: [authGuard]
  },
  {
    path: 'booking/:id',
    loadComponent: () => import('./components/booking/booking').then(m => m.BookingComponent),
    canActivate: [authGuard]
  },
  {
    path: 'my-tickets',
    loadComponent: () => import('./components/my-tickets/my-tickets').then(m => m.MyTicketsComponent),
    canActivate: [authGuard]
  },
  { path: '**', redirectTo: '/home' }
];
