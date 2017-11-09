import { Component } from '@angular/core';
import { OnInit } from '@angular/core';
import { SponsorService , Sponsor } from '../services/sponsor.service';

@Component({
  selector: 'app-sponsors',
  templateUrl: './sponsors.component.html'
})
export class SponsorsComponent implements OnInit {

  sponsors: Sponsor[] = [];

  constructor(private sponsorService: SponsorService) {
    this.sponsors = [];
  }

  ngOnInit(): void {
    this.sponsorService.getFaqs().subscribe(
      (data) => {
        this.sponsors = data;
      },
      (err) => console.error(err),
      () => {
        this.sponsors = this.sponsors.sort((sponsor1, sponsor2) => sponsor1.id - sponsor2.id);
      }
    );
  }
}
