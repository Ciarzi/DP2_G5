const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const mysql = require('mysql');
const PORT = process.env.PORT || 3050;


const app = express();

app.use(bodyParser.json());

const connection = mysql.createConnection({
    host     : 'db4free.net',
    user     : 'user_mda',
    password : 'r00tpass',
    database : 'db_users_mda'
  });


  app.get('/',(req,res) =>{
    const sql = 'SELECT * FROM Grouped_id' 
   connection.query(sql, (err,results) => {
       if(err) throw err;
       if(results.length > 0) {
           res.json(results);
       }else {
           res.send('not result')
       }
   })
  })

  app.get('/friends',(req,res) =>{
    const sql = 'SELECT * FROM friends_distance' 
   connection.query(sql, (err,results) => {
       if(err) throw err;
       if(results.length > 0) {
           res.json(results);
       }else {
           res.send('not result')
       }
   })
  })

  connection.connect(error => {
      if (error) throw error;
      console.log('database serve running')
  });

  app.listen(PORT, () => console.log(`server running on port ${PORT}`)); 
