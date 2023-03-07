import { Component } from '@angular/core';
import { AssessmentApi } from './assessment.api';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  title = 'Dementia Risk Assessment';

  constructor(private api: AssessmentApi) {}

  createAssessment() {
    this.api.createAssessment();
  }
}
