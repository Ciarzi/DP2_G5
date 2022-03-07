import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PlancostumComponent } from './plancostum.component';

describe('PlancostumComponent', () => {
  let component: PlancostumComponent;
  let fixture: ComponentFixture<PlancostumComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PlancostumComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PlancostumComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
