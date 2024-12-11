import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';  // Import RouterModule and Routes
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { CriticComponent } from './critic/critic.component';  // Import your custom component

// Define your routes
const appRoutes: Routes = [
  { path: '', redirectTo: '/critic', pathMatch: 'full' }, // Redirect to Critic component by default
  { path: 'critic', component: CriticComponent },  // Route for the Critic component
  // Add more routes here if you have other components
];

@NgModule({
  declarations: [
    AppComponent,
    CriticComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    RouterModule.forRoot(appRoutes)  // Register routes in the RouterModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
