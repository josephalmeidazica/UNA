import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EstacoesComponent } from './estacoes.component';

describe('EstacoesComponent', () => {
  let component: EstacoesComponent;
  let fixture: ComponentFixture<EstacoesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EstacoesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EstacoesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
