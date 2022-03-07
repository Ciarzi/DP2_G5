const { off } = require("process");
const mysql = require('mysql');


const connection = mysql.createConnection({
    host: '35.187.114.126',
    user: 'root',
    password: 'datapdb2',
    database: 'lestsprayDb'
});

exports.httpServer = function httpServer(req, res) {
    res.set('Access-Control-Allow-Origin', "*")
    res.set('Access-Control-Allow-Methods', 'GET, POST');

    if (req.method === "OPTIONS") {
        res.set('Access-Control-Allow-Headers', 'Content-Type');
        res.set('Access-Control-Max-Age', '3600');
        res.status(204).send('');
    }
    const path = req.path;
    if (path.startsWith('/users'))
        return handleUsers(req, res);
    else
        if (path.startsWith('/config'))
            return handleConfig(req, res);
        else
            return res.status(200).send('Server is working');

};

const handleUsers = (req, res) => {
    if (req.method === 'GET') {
        return getUsers(req, res);
    } else {
        return res.status(405).send();
    }
};

const handleConfig = (req, res) => {
    if (req.method === 'GET') {
        return getConfig(req,res);
    } else
    if (req.method === 'POST') {
        return insertConfig(req, res);
    } else {
        return res.status(405).send();
    }
};

const getUsers = (req, res) => {
    var userId = req.query.userId
    if (userId === undefined) {
        return res.status(404).send();
    }
    const sql = `SELECT sensorsInput.sensorId,
    soilHumidity,
    relativeHumidity,
    temperature,
    date FROM sensorsInput 
    inner join sensors on sensorsInput.sensorId = sensors.sensorId
    where sensors.userId = ?
    ORDER BY sensorsInput.sensorsInputId DESC LIMIT 1`

    connection.query(sql, [userId], (err, results) => {
        if (err) throw err;
        if (results.length > 0) {
            return res.status(200).json(results).send();
        } else {
            return res.status(404).send();
        }
    })
};

const insertConfig = (req, res) => {
    var obj = req.body;
    const sql = `CALL InsertUpdateSensorConfig (?)`;
    var values = [obj.idusuario, obj.metros_cuadrados, obj.humedad, obj.cespedPreference, obj.florPreference, obj.regadoPreference];

    connection.query(sql, [values], function (err, result) {
        if (err){
            return res.status(500).send(err);
        }
        else
            return res.status(201).send('ok');
    });
}

const getConfig = (req,res) => {
    var userId = req.query.userId
    if (userId === undefined) {
        return res.status(404).send();
    }
    const sql = `SELECT * FROM userSensorConfig
    where sensorId = ?`

    connection.query(sql, [userId], (err, results) => {
        if (err) throw err;
        if (results.length > 0) {
            return res.status(200).json(results).send();
        } else {
            return res.status(404).send();
        }
    })
}