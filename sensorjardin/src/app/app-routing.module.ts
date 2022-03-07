import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './pages/login/login.component';
import { PlanautoComponent } from './pages/planauto/planauto.component';
import { PlancostumComponent } from './pages/plancostum/plancostum.component';

const routes: Routes = [
  {path:'',component:LoginComponent},
  {path:'auto',component:PlanautoComponent},
  {path:'costum', component:PlancostumComponent}
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
