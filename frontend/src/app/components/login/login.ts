import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterLink, Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { HttpErrorResponse } from '@angular/common/http';

type Tab = 'login' | 'register';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule, RouterLink],
  templateUrl: './login.html',
  styleUrl: './login.css'
})
export class LoginComponent {
  activeTab: Tab = 'login';

  // [(ngModel)] form controls — requirement #3
  loginUsername = '';
  loginPassword = '';
  registerUsername = '';
  registerEmail = '';
  registerPassword = '';

  errorMessage = '';
  successMessage = '';
  isLoading = false;

  constructor(private auth: AuthService, private router: Router) {}

  switchTab(tab: Tab): void {
    this.activeTab = tab;
    this.errorMessage = '';
    this.successMessage = '';
  }

  // click event → API request — requirement #2 + #7 + #9
  onLogin(): void {
    this.errorMessage = '';
    if (!this.loginUsername || !this.loginPassword) {
      this.errorMessage = 'Please fill in all fields.';
      return;
    }
    this.isLoading = true;
    this.auth.login(this.loginUsername, this.loginPassword).subscribe({
      next: () => {
        this.isLoading = false;
        this.router.navigate(['/matches']);
      },
      error: (err: HttpErrorResponse) => {
        this.isLoading = false;
        this.errorMessage =
          err.error?.detail ||
          err.error?.non_field_errors?.[0] ||
          'Invalid username or password.';
      }
    });
  }

  // click event → API request — requirement #2 + #9
  onRegister(): void {
    this.errorMessage = '';
    this.successMessage = '';
    if (!this.registerUsername || !this.registerEmail || !this.registerPassword) {
      this.errorMessage = 'Please fill in all fields.';
      return;
    }
    this.isLoading = true;
    this.auth.register(this.registerUsername, this.registerEmail, this.registerPassword).subscribe({
      next: () => {
        this.isLoading = false;
        this.successMessage = 'Account created! You can now sign in.';
        this.activeTab = 'login';
        this.loginUsername = this.registerUsername;
      },
      error: (err: HttpErrorResponse) => {
        this.isLoading = false;
        const first = Object.values(err.error || {})[0];
        this.errorMessage = Array.isArray(first)
          ? first[0]
          : err.error?.detail || 'Registration failed.';
      }
    });
  }
}
