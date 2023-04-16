import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { AssessmentApi } from './assessment.api';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
  title = 'Dementia Risk Assessment';
  formData: any;
  returnedData: any;
  showForm = true;

  constructor(private api: AssessmentApi) {}

  ngOnInit(): void {
    this.formData = new FormGroup({
      tau: new FormControl(0),
      gfap: new FormControl(0),
      at8: new FormControl(0),
      at8Ffp: new FormControl(0),
      alphaBeta: new FormControl(0),
      tau2: new FormControl(0),
      tdp: new FormControl(0),
    });
  }

  async createAssessment(formData: any) {
    this.showForm = false;
    this.returnedData = await this.api.createAssessment(formData);
  }

  openForm() {
    this.showForm = true;
  }
}
