import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PlanautoComponent } from './planauto.component';

describe('PlanautoComponent', () => {
  let component: PlanautoComponent;
  let fixture: ComponentFixture<PlanautoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PlanautoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PlanautoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
