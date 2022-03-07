import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-planauto',
  templateUrl: './planauto.component.html',
  styleUrls: ['./planauto.component.css']
})
export class PlanautoComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }
  elegir(){
    console.log("se ha inicializado la funcion Guardar")
  document.getElementById("humedo").style.backgroundColor="MediumSeaGreen";
  document.getElementById("seco").style.backgroundColor="White";
  
  }
  elegir1(){
    console.log("se ha inicializado la funcion Guardar")
  document.getElementById("seco").style.backgroundColor="MediumSeaGreen";
  document.getElementById("humedo").style.backgroundColor="White";
  
  }
  cancelar(){
    console.log("se ha inicializado la funcion Guardar")
  document.getElementById("seco").style.backgroundColor="White";
  document.getElementById("humedo").style.backgroundColor="White";

  }
}
