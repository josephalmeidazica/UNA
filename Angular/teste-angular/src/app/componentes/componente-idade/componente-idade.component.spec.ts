import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ComponenteIdadeComponent } from './componente-idade.component';

describe('ComponenteIdadeComponent', () => {
  let component: ComponenteIdadeComponent;
  let fixture: ComponentFixture<ComponenteIdadeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ComponenteIdadeComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ComponenteIdadeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
