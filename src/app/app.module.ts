import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { VirtualScrollModule } from 'angular2-virtual-scroll';
import { ScrollToModule } from 'ng2-scroll-to';
import { StickyNavModule } from 'ng2-sticky-nav';

import { AppComponent } from './app.component';
import { TopComponent } from './top/top.component';
import { HeadComponent } from './header/header.component';
import { FaqComponent } from './faq/faq.component';
import { SponsorsComponent } from './sponsors/sponsors.component';
import { FooterComponent } from './footer/footer.component';

import { FaqService } from './services/faq.service';
import { SponsorService } from './services/sponsor.service';


@NgModule({
  declarations: [
    AppComponent,
    TopComponent,
    HeadComponent,
    FaqComponent,
    SponsorsComponent,
    FooterComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    VirtualScrollModule,
    BrowserAnimationsModule,
    ScrollToModule,
    StickyNavModule
  ],
  providers: [
    FaqService,
    SponsorService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
