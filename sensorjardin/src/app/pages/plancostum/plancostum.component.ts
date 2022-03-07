import { Component, OnInit } from '@angular/core';
import { ServiciosService } from 'src/app/servicios.service';
import { User } from 'src/app/user';

@Component({
  selector: 'app-plancostum',
  templateUrl: './plancostum.component.html',
  styleUrls: ['./plancostum.component.css']
})
export class PlancostumComponent implements OnInit {
  flores = ['secas','humedas'];
  cesped = ['artificial','natural'];
  userModel = new User(1,150,30 ,'','','')
  constructor(private servicios: ServiciosService) { }

  tiempo;

  
  ngOnInit(): void {
    this.servicios.recibirdata().subscribe(datos => {console.log(datos);
    this.tiempo = datos;
    })
  }
  onSubmit(){
    this.servicios.enroll(this.userModel)
    .subscribe(
      data => console.log('Success!', data),
      error => console.log('Error!', error)

    )

  }
}
