import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { ComponenteIdadeComponent } from './componentes/componente-idade/componente-idade.component';
import { EstacoesComponent } from './componentes/estacoes/estacoes.component';
import { CalculadoraComponent } from './componentes/calculadora/calculadora.component';
import { TabuadaComponent } from './componentes/tabuada/tabuada.component';

@NgModule({
  declarations: [
    AppComponent,
    ComponenteIdadeComponent,
    EstacoesComponent,
    CalculadoraComponent,
    TabuadaComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule.forRoot([
      { path: 'idade', component: ComponenteIdadeComponent },
    ]),
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
