import { TestBed } from '@angular/core/testing';

import { AssessmentApi } from './assessment.api';

describe('AssessmentApi', () => {
  let service: AssessmentApi;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AssessmentApi);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
