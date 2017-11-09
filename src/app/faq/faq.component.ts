import { Component } from '@angular/core';
import { OnInit } from '@angular/core';
import { FaqService , Faq } from '../services/faq.service';

@Component({
  selector: 'app-faq',
  templateUrl: './faq.component.html'
})
export class FaqComponent implements OnInit {

  faqs: Faq[];
  viewPortItems = [];
  selectedfaq: Faq = {
    id: 0,
    question: '',
    answer: '',
    user_id: 0,
    created_at: '',
    updated_at: '',
    display: '',
    priority: 0,
    placement: '',
  };

  constructor(private faqService: FaqService) {
    this.faqs = [];
  }

  ngOnInit(): void {
    this.faqService.getFaqs().subscribe(
      (data) => {
        this.faqs = data;
      },
      (err) => console.error(err),
      () => {
        this.faqs = this.faqs.sort((faq1, faq2) => faq1.priority - faq2.priority);
        this.faqs = this.faqs.filter(faq => faq.placement === 'home');
        this.selectedfaq = this.faqs[0];
      }
    );
  }

  OnClick(faq: Faq): void {
    this.selectedfaq = faq;
  }
}
