import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import { User } from './user';
@Injectable({
  providedIn: 'root'
})
export class ServiciosService {

  url='https://europe-west1-sensorproject-342620.cloudfunctions.net/httpServer/config';
  url2='https://europe-west1-sensorproject-342620.cloudfunctions.net/httpServer/users?userId=1'
  constructor(private client:HttpClient) { }
  
  enroll(user:User){
   return this.client.post<any>(this.url, user);

  }
  recibirdata(){
   return this.client.get(this.url2);
  }
}
