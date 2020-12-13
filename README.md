# hx711server

The first scale is on GPIO 21,20
The second scale is on GPIO 26,19

You can get the values via the rest api

http://localhost:8081/

for setting the reference correctly, use a known weight and put it on the scale and calculate the reference via

Sensor_raw_value / known_weight = reference_Unit

Example 

-882000 / 2000 = -441

Do that step for each scale seperate!

This Applikation is designed for my modified mainsail interface as addon
