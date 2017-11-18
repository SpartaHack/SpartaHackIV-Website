import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

export class Faq {
  id: number;
  question: string;
  answer: string;
  user_id: number;
  created_at: string;
  updated_at: string;
  display: string;
  priority: number;
  placement: string;
}

@Injectable()

export class FaqService {

  headers = new Headers({
    });

  constructor(private http: Http) { }

  getFaqs(): Observable<Faq[]> {
    let options = new RequestOptions({ headers : this.headers});
    return this.http.get('https://api.spartahack.com/faqs', options)
      .map((response: Response) => <Faq[]>response.json())
      .catch(this.handleError);
  }

  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }
}
