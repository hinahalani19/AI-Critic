import { Component } from '@angular/core';
import { CriticService } from './critic.service';

@Component({
  selector: 'app-critic',
  templateUrl: './critic.component.html',
  styleUrls: ['./critic.component.css']
})
export class CriticComponent {
  movieName: string = '';
  responseText: string = '';
  targetLanguage: string = 'en';
  sourceLanguage: string = 'auto';
  generatedReview: string = '';
  translatedText: string = '';
  languages: { [key: string]: string } = {
    English: 'en',
    Hindi: 'hi',
    Spanish: 'es',
    French: 'fr',
    German: 'de',
    Italian: 'it',
    Portuguese: 'pt',
    Russian: 'ru',
    Chinese: 'zh',
    Japanese: 'ja',
    Telugu: 'te',
  };

  constructor(private criticService: CriticService) {}

  generateCritic(): void {
    if (!this.movieName) {
      alert('Please enter a movie name.');
      return;
    }
    this.criticService.generateCritic(this.movieName).subscribe(
      (response: any) => {
        this.generatedReview = response.review;
      },
      (error) => {
        console.error('Error generating review:', error);
        alert('Failed to generate review. Please try again.');
      }
    );
  }

  translateText(): void {
    const payload = {
      response_text: this.responseText,
      target_language: this.targetLanguage,
      source_language: this.sourceLanguage,
    };
    this.criticService.translateText(payload).subscribe(
      (response: any) => {
        this.translatedText = response.translated_text;
      },
      (error) => {
        console.error('Error translating text:', error);
        alert('Failed to translate text. Please try again.');
      }
    );
  }

  playSpeech(): void {
    const payload = {
      response_text: this.responseText,
      language: this.targetLanguage,
    };
    this.criticService.playSpeech(payload).subscribe(
      () => {
        alert('Speech played successfully.');
      },
      (error) => {
        console.error('Error playing speech:', error);
        alert('Failed to play speech. Please try again.');
      }
    );
  }
}
