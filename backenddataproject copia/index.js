
const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const mysql = require('mysql');
const PORT = process.env.PORT || 3050;


const app = express();

app.use(bodyParser.json());

const connection = mysql.createConnection({
    host: '35.187.114.126',
    user: 'root',
    password: 'datapdb2',
    database: 'lestsprayDb'
});

//   app.get('/documents/:format/:type', function (req, res) {
//     var format = req.params.format,
//         type = req.params.type;
//  });

app.get('/:userId', (req, res) => {
    var userId = req.params.userId
    const sql = `SELECT sensorsInput.sensorId,
    soilHumidity,
    relativeHumidity,
    temperature,
    date FROM sensorsInput 
    inner join sensors on sensorsInput.sensorId = sensors.sensorId
    where sensors.userId = ?
    ORDER BY sensorsInput.sensorsInputId DESC LIMIT 1`

    connection.query(sql, userId, (err, results) => {
        if (err) throw err;
        if (results.length > 0) {
            res.json(results);
        } else {
            res.send('not result')
        }
    })
});

app.post('/config', function (req, res) {
    var post_body = req.body;
    const obj = JSON.parse(post_body);
    const sql = `INSERT INTO userSensorConfig (sensorId, squareMeter, soilHumidity, grass, flowerPreference, timePreference)
    VALUES ?`;
    var values = [obj.idusuario, obj.metros_cuadrados, obj.humedad, obj.cespedPreference, obj.florPreference, obj.regadoPreference]
    connection.query(sql, values, function (err, result) {
        if (err) throw err;
        console.log("1 record inserted");
        console.log(post_body);
    })
});


connection.connect(error => {
    if (error) throw error;
    console.log('database serve running')
});

app.listen(PORT, () => console.log(`server running on port ${PORT}`));
