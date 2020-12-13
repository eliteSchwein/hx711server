var express = require('express');
var cors = require('cors');
var hx711 = require('@ataberkylmz/hx711');

const PORT = 8081;

var scalevalue1 = 0;
var scalevalue2 = 0;

const sensor1 = new hx711(29, 28);
const sensor2 = new hx711(25, 24);
var app = express();
app.use(cors());

setInterval(retrieveScaleData,500);

app.listen(PORT, () => {
  console.log(`Started listening on port `+PORT);
});

app.get('/get.json', function (req, res) {
	res.type("application/json");
  res.send('[{"id":"1","value":"'+scalevalue1+'"},{"id":"2","value":"'+scalevalue2+'"}]');
});

function retrieveScaleData(){
	sensor1.powerUp();
	sensor2.powerUp();
	scalevalue1=sensor1.getUnits();
	scalevalue2=sensor2.getUnits();
	sensor1.powerDown();
	sensor2.powerDown();
}

