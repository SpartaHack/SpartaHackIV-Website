import { Component } from '@angular/core';
import {
  trigger,
  state,
  style,
  animate,
  transition
} from '@angular/animations';

@Component({
  selector: 'app-top',
  templateUrl: './top.component.html',
  animations: [
    trigger('mailState', [
      transition(':enter', [   // :enter is alias to 'void => *'
      style({opacity: 0}),
      animate(300, style({opacity: 1}))
    ])
  ]),
    trigger('logoIn', [
      transition(':enter', [   // :enter is alias to 'void => *'
      style({
        opacity: 0,
        transform: 'scale(1.1)'
      }),
      animate(700, style({
        opacity: 1,
        transform: 'scale(1.0)'
      }))
    ])
  ]),
    trigger('textIn', [
      transition(':enter', [   // :enter is alias to 'void => *'
      style({
        opacity: 0,
      }),
      animate('1s 700ms', style({
        opacity: 1,
        transform: 'scale(1.0)'
      }))
    ])
  ]),
    trigger('snowflakeIn1', [
      transition(':enter', [   // :enter is alias to 'void => *'
      style({
        opacity: 0,
        transform: 'translateY(-40%)'
      }),
      animate('3s 500ms', style({
        opacity: 1,
        transform: 'translateY(0)'
      }))
    ])
  ]),
    trigger('snowflakeIn2', [
      transition(':enter', [   // :enter is alias to 'void => *'
      style({
        opacity: 0,
        transform: 'translateY(-50%)'
      }),
      animate('2s 700ms', style({
        opacity: 1,
        transform: 'translateY(0)'
      }))
    ])
  ]),
    trigger('snowflakeIn3', [
      transition(':enter', [   // :enter is alias to 'void => *'
      style({
        opacity: 0,
        transform: 'translateY(-40%)'
      }),
      animate('2.1s 1.2s', style({
        opacity: 1,
        transform: 'translateY(0)'
      }))
    ])
  ]),
    trigger('snowflakeIn4', [
      transition(':enter', [   // :enter is alias to 'void => *'
      style({
        opacity: 0,
        transform: 'translateY(-50%)'
      }),
      animate('2.7s 1s', style({
        opacity: 1,
        transform: 'translateY(0)'
      }))
    ])
  ]),
    trigger('snowflakeIn5', [
      transition(':enter', [   // :enter is alias to 'void => *'
      style({
        opacity: 0,
        transform: 'translateY(-50%)'
      }),
      animate('2.1s 900ms', style({
        opacity: 1,
        transform: 'translateY(0)'
      }))
    ])
  ]),
    trigger('mailButtonIn', [
      transition(':enter', [   // :enter is alias to 'void => *'
      style({
        opacity: 0,
      }),
      animate('1s 1.7s', style({
        opacity: 1,
        transform: 'scale(1.0)'
      }))
    ])
  ]),
  ]
})
export class TopComponent {
  signingUp = false;
  mailState = 'inactive';
  OnSignUpClick() {
    this.signingUp = true;
    this.mailState = 'active';
  }
}
