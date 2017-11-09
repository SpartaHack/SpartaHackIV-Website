import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

export class Sponsor {
  id: number;
  company: string;
  logoURL: string;
}

@Injectable()

export class SponsorService {

  headers = new Headers({
    // 'content-type': 'application/json',
    // 'authorization': 'Token token=9ba5cc744d40feb58d0bc6bce7c8d8be',
    // 'accept': 'vnd.example.v2'
    });

  constructor(private http: Http) { }

  getFaqs(): Observable<Sponsor[]> {
    let options = new RequestOptions({ headers : this.headers});
    return this.http.get('assets/data/sponsors.json', options)
      .map((response: Response) => <Sponsor[]>response.json())
      .catch(this.handleError);
  }

  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }
}