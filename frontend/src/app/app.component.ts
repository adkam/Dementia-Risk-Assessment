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

  constructor(private api: AssessmentApi) {}

  ngOnInit(): void {
    this.formData = new FormGroup({
      age: new FormControl(''),
      sex: new FormControl(''),
      ceradScore: new FormControl(''),
      gad1: new FormControl(''),
      gad2: new FormControl(''),
      gfap: new FormControl(''),
    });
  }

  createAssessment(formData: any) {
    console.log(formData);
    // this.api.createAssessment();
  }
}
