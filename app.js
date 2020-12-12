var express = require('express');
var cors = require('cors');

const PORT = 8081;

var scalevalue1 = 1500;
var scalevalue2 = 0;

const sensor1 = new HX711(21, 20);
const sensor2 = new HX711(26, 19);
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
  scalevalue1=sensor1.read();
  scalevalue2=sensor2.read();
}

