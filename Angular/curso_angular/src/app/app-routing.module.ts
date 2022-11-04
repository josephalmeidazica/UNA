import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {GetUserComponent} from './componentes/get-user/get-user.component'

const routes: Routes = [
  {path: 'get', component: GetUserComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
