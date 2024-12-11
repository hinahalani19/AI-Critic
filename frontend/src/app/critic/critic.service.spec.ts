import { TestBed } from '@angular/core/testing';

import { CriticService } from './critic.service';

describe('CriticService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: CriticService = TestBed.get(CriticService);
    expect(service).toBeTruthy();
  });
});
