Zigbee2MQTT:debug 2021-12-24 03:29:57: Clearing Home Assistant discovery topic for 'Kitchen Sink'
Zigbee2MQTT:info  2021-12-24 03:29:57: MQTT publish: topic 'homeassistant/light/0x0017880102952daf/light/config', payload 'null'
Zigbee2MQTT:info  2021-12-24 03:29:57: MQTT publish: topic 'homeassistant/sensor/0x0017880102952daf/linkquality/config', payload 'null'
Zigbee2MQTT:info  2021-12-24 03:29:57: MQTT publish: topic 'homeassistant/sensor/0x0017880102952daf/last_seen/config', payload 'null'
Zigbee2MQTT:info  2021-12-24 03:29:57: MQTT publish: topic 'homeassistant/sensor/0x0017880102952daf/update_state/config', payload 'null'
Zigbee2MQTT:info  2021-12-24 03:29:57: MQTT publish: topic 'homeassistant/binary_sensor/0x0017880102952daf/update_available/config', payload 'null'
Zigbee2MQTT:info  2021-12-24 03:29:57: MQTT publish: topic 'zigbee2mqtt/Kitchen Sink', payload ''
Zigbee2MQTT:info  2021-12-24 03:29:57: Successfully removed device 'Kitchen Sink' (block: false, force: false)
Zigbee2MQTT:info  2021-12-24 03:29:57: MQTT publish: topic 'zigbee2mqtt/bridge/response/device/remove', payload '{"data":{"block":false,"force":false,"id":"Kitchen Sink"},"status":"ok","transaction":"uc2wr-2"}'
2021-12-24T03:29:57.859Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,13,69,201,234,212,175,45,149,2,1,136,23,0,0,0,0,52]
2021-12-24T03:29:57.859Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,13,69,201,234,212,175,45,149,2,1,136,23,0,0,0,0,52]
2021-12-24T03:29:57.859Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 13 - 2 - 5 - 201 - [234,212,175,45,149,2,1,136,23,0,0,0,0] - 52
2021-12-24T03:29:57.859Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - leaveInd - {"srcaddr":54506,"extaddr":"0x0017880102952daf","request":0,"removechildren":0,"rejoin":0}
Zigbee2MQTT:warn  2021-12-24 03:29:57: Device '0x0017880102952daf' left the network
2021-12-24T03:29:57.860Z zigbee-herdsman:controller:log Device leave '0x0017880102952daf'
Zigbee2MQTT:info  2021-12-24 03:29:57: MQTT publish: topic 'zigbee2mqtt/bridge/event', payload '{"data":{"friendly_name":"0x0017880102952daf","ieee_address":"0x0017880102952daf"},"type":"device_leave"}'
Zigbee2MQTT:info  2021-12-24 03:29:57: MQTT publish: topic 'zigbee2mqtt/bridge/log', payload '{"message":"left_network","meta":{"friendly_name":"0x0017880102952daf"},"type":"device_removed"}'
2021-12-24T03:29:57.943Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
Zigbee2MQTT:debug 2021-12-24 03:29:57: Received MQTT message on 'homeassistant/light/0x0017880102952daf/light/config' with data ''
Zigbee2MQTT:debug 2021-12-24 03:29:57: Received MQTT message on 'homeassistant/sensor/0x0017880102952daf/linkquality/config' with data ''
Zigbee2MQTT:debug 2021-12-24 03:29:57: Received MQTT message on 'homeassistant/sensor/0x0017880102952daf/last_seen/config' with data ''
Zigbee2MQTT:debug 2021-12-24 03:29:57: Received MQTT message on 'homeassistant/sensor/0x0017880102952daf/update_state/config' with data ''
Zigbee2MQTT:debug 2021-12-24 03:29:57: Received MQTT message on 'homeassistant/binary_sensor/0x0017880102952daf/update_available/config' with data ''
2021-12-24T03:29:58.371Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,3,69,196,85,238,0,57]
2021-12-24T03:29:58.371Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,3,69,196,85,238,0,57]
2021-12-24T03:29:58.372Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 3 - 2 - 5 - 196 - [85,238,0] - 57
2021-12-24T03:29:58.372Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - srcRtgInd - {"dstaddr":61013,"relaycount":0,"relaylist":[]}
2021-12-24T03:29:58.372Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
2021-12-24T03:29:58.374Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,3,69,196,126,138,0,118,254,3,69,196,43,139,0,34]
2021-12-24T03:29:58.375Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,3,69,196,126,138,0,118,254,3,69,196,43,139,0,34]
2021-12-24T03:29:58.375Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 3 - 2 - 5 - 196 - [126,138,0] - 118
2021-12-24T03:29:58.375Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - srcRtgInd - {"dstaddr":35454,"relaycount":0,"relaylist":[]}
2021-12-24T03:29:58.375Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,3,69,196,43,139,0,34]
2021-12-24T03:29:58.376Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 3 - 2 - 5 - 196 - [43,139,0] - 34
2021-12-24T03:29:58.376Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - srcRtgInd - {"dstaddr":35627,"relaycount":0,"relaylist":[]}
2021-12-24T03:29:58.376Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
2021-12-24T03:29:58.377Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,3,69,196,46,232,0,68,254,5,69,196,71,122,1,85,238,3,254,5,69,196,71,122,1,85,238,3,254,5,69,196,82,151,1,201,166,47]
2021-12-24T03:29:58.378Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,3,69,196,46,232,0,68,254,5,69,196,71,122,1,85,238,3,254,5,69,196,71,122,1,85,238,3,254,5,69,196,82,151,1,201,166,47]
2021-12-24T03:29:58.378Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 3 - 2 - 5 - 196 - [46,232,0] - 68
2021-12-24T03:29:58.378Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - srcRtgInd - {"dstaddr":59438,"relaycount":0,"relaylist":[]}
2021-12-24T03:29:58.378Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,5,69,196,71,122,1,85,238,3,254,5,69,196,71,122,1,85,238,3,254,5,69,196,82,151,1,201,166,47]
2021-12-24T03:29:58.379Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 5 - 2 - 5 - 196 - [71,122,1,85,238] - 3
2021-12-24T03:29:58.379Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - srcRtgInd - {"dstaddr":31303,"relaycount":1,"relaylist":[61013]}
2021-12-24T03:29:58.379Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,5,69,196,71,122,1,85,238,3,254,5,69,196,82,151,1,201,166,47]
2021-12-24T03:29:58.379Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 5 - 2 - 5 - 196 - [71,122,1,85,238] - 3
2021-12-24T03:29:58.380Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - srcRtgInd - {"dstaddr":31303,"relaycount":1,"relaylist":[61013]}
2021-12-24T03:29:58.380Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,5,69,196,82,151,1,201,166,47]
2021-12-24T03:29:58.380Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 5 - 2 - 5 - 196 - [82,151,1,201,166] - 47
2021-12-24T03:29:58.380Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - srcRtgInd - {"dstaddr":38738,"relaycount":1,"relaylist":[42697]}
2021-12-24T03:29:58.381Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
2021-12-24T03:29:58.382Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,3,69,196,46,232,0,68,254,3,69,196,126,138,0,118,254,5,69,196,40,113,1,43,139,124,254,3,69,196,201,166,0,237]
2021-12-24T03:29:58.382Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,3,69,196,46,232,0,68,254,3,69,196,126,138,0,118,254,5,69,196,40,113,1,43,139,124,254,3,69,196,201,166,0,237]
2021-12-24T03:29:58.382Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 3 - 2 - 5 - 196 - [46,232,0] - 68
2021-12-24T03:29:58.383Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - srcRtgInd - {"dstaddr":59438,"relaycount":0,"relaylist":[]}
2021-12-24T03:29:58.383Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,3,69,196,126,138,0,118,254,5,69,196,40,113,1,43,139,124,254,3,69,196,201,166,0,237]
2021-12-24T03:29:58.383Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 3 - 2 - 5 - 196 - [126,138,0] - 118
2021-12-24T03:29:58.383Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - srcRtgInd - {"dstaddr":35454,"relaycount":0,"relaylist":[]}
2021-12-24T03:29:58.383Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,5,69,196,40,113,1,43,139,124,254,3,69,196,201,166,0,237]
2021-12-24T03:29:58.384Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 5 - 2 - 5 - 196 - [40,113,1,43,139] - 124
2021-12-24T03:29:58.384Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - srcRtgInd - {"dstaddr":28968,"relaycount":1,"relaylist":[35627]}
2021-12-24T03:29:58.384Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,3,69,196,201,166,0,237]
2021-12-24T03:29:58.384Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 3 - 2 - 5 - 196 - [201,166,0] - 237
2021-12-24T03:29:58.384Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - srcRtgInd - {"dstaddr":42697,"relaycount":0,"relaylist":[]}
2021-12-24T03:29:58.385Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
2021-12-24T03:29:58.385Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,5,69,196,82,151,1,201,166,47,254,3,69,196,201,166,0,237,254,3,69,196,201,166,0,237,254,5,69,196,40,113,1,43,139,124]
2021-12-24T03:29:58.385Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,5,69,196,82,151,1,201,166,47,254,3,69,196,201,166,0,237,254,3,69,196,201,166,0,237,254,5,69,196,40,113,1,43,139,124]
2021-12-24T03:29:58.386Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 5 - 2 - 5 - 196 - [82,151,1,201,166] - 47
2021-12-24T03:29:58.386Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - srcRtgInd - {"dstaddr":38738,"relaycount":1,"relaylist":[42697]}
2021-12-24T03:29:58.386Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,3,69,196,201,166,0,237,254,3,69,196,201,166,0,237,254,5,69,196,40,113,1,43,139,124]
2021-12-24T03:29:58.386Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 3 - 2 - 5 - 196 - [201,166,0] - 237
2021-12-24T03:29:58.386Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - srcRtgInd - {"dstaddr":42697,"relaycount":0,"relaylist":[]}
2021-12-24T03:29:58.386Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,3,69,196,201,166,0,237,254,5,69,196,40,113,1,43,139,124]
2021-12-24T03:29:58.386Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 3 - 2 - 5 - 196 - [201,166,0] - 237
2021-12-24T03:29:58.387Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - srcRtgInd - {"dstaddr":42697,"relaycount":0,"relaylist":[]}
2021-12-24T03:29:58.387Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,5,69,196,40,113,1,43,139,124]
2021-12-24T03:29:58.387Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 5 - 2 - 5 - 196 - [40,113,1,43,139] - 124
2021-12-24T03:29:58.387Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - srcRtgInd - {"dstaddr":28968,"relaycount":1,"relaylist":[35627]}
2021-12-24T03:29:58.387Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
2021-12-24T03:30:01.113Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,3,69,196,201,166,0,237]
2021-12-24T03:30:01.113Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,3,69,196,201,166,0,237]
2021-12-24T03:30:01.113Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 3 - 2 - 5 - 196 - [201,166,0] - 237
2021-12-24T03:30:01.114Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - srcRtgInd - {"dstaddr":42697,"relaycount":0,"relaylist":[]}
2021-12-24T03:30:01.114Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
2021-12-24T03:30:01.114Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,3,69,196,201,166,0,237]
2021-12-24T03:30:01.114Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,3,69,196,201,166,0,237]
2021-12-24T03:30:01.115Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 3 - 2 - 5 - 196 - [201,166,0] - 237
2021-12-24T03:30:01.115Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - srcRtgInd - {"dstaddr":42697,"relaycount":0,"relaylist":[]}
2021-12-24T03:30:01.115Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
2021-12-24T03:30:01.229Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,12,69,202,7,170,175,45,149,2,1,136,23,0,201,166,202]
2021-12-24T03:30:01.229Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,12,69,202,7,170,175,45,149,2,1,136,23,0,201,166,202]
2021-12-24T03:30:01.229Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 12 - 2 - 5 - 202 - [7,170,175,45,149,2,1,136,23,0,201,166] - 202
2021-12-24T03:30:01.230Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - tcDeviceInd - {"nwkaddr":43527,"extaddr":"0x0017880102952daf","parentaddr":42697}
2021-12-24T03:30:01.230Z zigbee-herdsman:controller:log Device '0x0017880102952daf' joined
2021-12-24T03:30:01.230Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
2021-12-24T03:30:01.230Z zigbee-herdsman:controller:log Device '0x0017880102952daf' accepted by handler
2021-12-24T03:30:01.230Z zigbee-herdsman:controller:log Delete device '0x0017880102952daf' joined, undeleting
Zigbee2MQTT:info  2021-12-24 03:30:01: Device '0x0017880102952daf' joined
Zigbee2MQTT:info  2021-12-24 03:30:01: MQTT publish: topic 'zigbee2mqtt/bridge/event', payload '{"data":{"friendly_name":"0x0017880102952daf","ieee_address":"0x0017880102952daf"},"type":"device_joined"}'
Zigbee2MQTT:info  2021-12-24 03:30:01: Configuring '0x0017880102952daf'
Zigbee2MQTT:info  2021-12-24 03:30:01: MQTT publish: topic 'zigbee2mqtt/bridge/log', payload '{"message":{"friendly_name":"0x0017880102952daf"},"type":"device_connected"}'
Zigbee2MQTT:info  2021-12-24 03:30:01: MQTT publish: topic 'homeassistant/light/0x0017880102952daf/light/config', payload '{"availability":[{"topic":"zigbee2mqtt/bridge/state"}],"brightness":true,"brightness_scale":254,"command_topic":"zigbee2mqtt/0x0017880102952daf/set","device":{"identifiers":["zigbee2mqtt_0x0017880102952daf"],"manufacturer":"Philips","model":"Hue white A60 bulb E27/B22 (9290011370)","name":"0x0017880102952daf","sw_version":"1.50.2_r30933"},"effect":true,"effect_list":["blink","breathe","okay","channel_change","finish_effect","stop_effect"],"json_attributes_topic":"zigbee2mqtt/0x0017880102952daf","name":"0x0017880102952daf","schema":"json","state_topic":"zigbee2mqtt/0x0017880102952daf","unique_id":"0x0017880102952daf_light_zigbee2mqtt"}'
Zigbee2MQTT:info  2021-12-24 03:30:01: MQTT publish: topic 'homeassistant/sensor/0x0017880102952daf/linkquality/config', payload '{"availability":[{"topic":"zigbee2mqtt/bridge/state"}],"device":{"identifiers":["zigbee2mqtt_0x0017880102952daf"],"manufacturer":"Philips","model":"Hue white A60 bulb E27/B22 (9290011370)","name":"0x0017880102952daf","sw_version":"1.50.2_r30933"},"enabled_by_default":false,"entity_category":"diagnostic","icon":"mdi:signal","json_attributes_topic":"zigbee2mqtt/0x0017880102952daf","name":"0x0017880102952daf linkquality","state_class":"measurement","state_topic":"zigbee2mqtt/0x0017880102952daf","unique_id":"0x0017880102952daf_linkquality_zigbee2mqtt","unit_of_measurement":"lqi","value_template":"{{ value_json.linkquality }}"}'
Zigbee2MQTT:info  2021-12-24 03:30:01: MQTT publish: topic 'homeassistant/sensor/0x0017880102952daf/last_seen/config', payload '{"availability":[{"topic":"zigbee2mqtt/bridge/state"}],"device":{"identifiers":["zigbee2mqtt_0x0017880102952daf"],"manufacturer":"Philips","model":"Hue white A60 bulb E27/B22 (9290011370)","name":"0x0017880102952daf","sw_version":"1.50.2_r30933"},"device_class":"timestamp","enabled_by_default":false,"entity_category":"diagnostic","icon":"mdi:clock","json_attributes_topic":"zigbee2mqtt/0x0017880102952daf","name":"0x0017880102952daf last seen","state_topic":"zigbee2mqtt/0x0017880102952daf","unique_id":"0x0017880102952daf_last_seen_zigbee2mqtt","value_template":"{{ value_json.last_seen }}"}'
Zigbee2MQTT:info  2021-12-24 03:30:01: MQTT publish: topic 'homeassistant/sensor/0x0017880102952daf/update_state/config', payload '{"availability":[{"topic":"zigbee2mqtt/bridge/state"}],"device":{"identifiers":["zigbee2mqtt_0x0017880102952daf"],"manufacturer":"Philips","model":"Hue white A60 bulb E27/B22 (9290011370)","name":"0x0017880102952daf","sw_version":"1.50.2_r30933"},"enabled_by_default":false,"entity_category":"diagnostic","icon":"mdi:update","json_attributes_topic":"zigbee2mqtt/0x0017880102952daf","name":"0x0017880102952daf update state","state_topic":"zigbee2mqtt/0x0017880102952daf","unique_id":"0x0017880102952daf_update_state_zigbee2mqtt","value_template":"{{ value_json['update']['state'] }}"}'
Zigbee2MQTT:info  2021-12-24 03:30:01: MQTT publish: topic 'homeassistant/binary_sensor/0x0017880102952daf/update_available/config', payload '{"availability":[{"topic":"zigbee2mqtt/bridge/state"}],"device":{"identifiers":["zigbee2mqtt_0x0017880102952daf"],"manufacturer":"Philips","model":"Hue white A60 bulb E27/B22 (9290011370)","name":"0x0017880102952daf","sw_version":"1.50.2_r30933"},"device_class":"update","enabled_by_default":true,"entity_category":"diagnostic","json_attributes_topic":"zigbee2mqtt/0x0017880102952daf","name":"0x0017880102952daf update available","payload_off":false,"payload_on":true,"state_topic":"zigbee2mqtt/0x0017880102952daf","unique_id":"0x0017880102952daf_update_available_zigbee2mqtt","value_template":"{{ value_json['update']['state'] == \"available\" }}"}'
2021-12-24T03:30:01.423Z zigbee-herdsman:controller:log Device '0x0017880102952daf' is already in database with different networkAddress, updating networkAddress
Zigbee2MQTT:info  2021-12-24 03:30:01: MQTT publish: topic 'zigbee2mqtt/0x0017880102952daf', payload '{"device":{"applicationVersion":2,"dateCode":"20191218","friendlyName":"0x0017880102952daf","hardwareVersion":1,"ieeeAddr":"0x0017880102952daf","manufacturerID":4107,"manufacturerName":"Philips","model":"9290011370","networkAddress":43527,"powerSource":"Mains (single phase)","softwareBuildID":"1.50.2_r30933","stackVersion":1,"type":"Router","zclVersion":1},"last_seen":"2021-12-24T03:30:01.428Z","linkquality":72,"state":null,"update_available":null}'
2021-12-24T03:30:01.432Z zigbee-herdsman:controller:log Not interviewing '0x0017880102952daf', completed 'true', in progress 'false'
Zigbee2MQTT:info  2021-12-24 03:30:01: Successfully configured '0x0017880102952daf'
Zigbee2MQTT:info  2021-12-24 03:30:01: MQTT publish: topic 'zigbee2mqtt/0x0017880102952daf', payload '{"device":{"applicationVersion":2,"dateCode":"20191218","friendlyName":"0x0017880102952daf","hardwareVersion":1,"ieeeAddr":"0x0017880102952daf","manufacturerID":4107,"manufacturerName":"Philips","model":"9290011370","networkAddress":43527,"powerSource":"Mains (single phase)","softwareBuildID":"1.50.2_r30933","stackVersion":1,"type":"Router","zclVersion":1},"last_seen":"2021-12-24T03:30:01.524Z","linkquality":72,"state":null,"update_available":null}'
Zigbee2MQTT:debug 2021-12-24 03:30:01: Device '0x0017880102952daf' announced itself
2021-12-24T03:30:01.522Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,12,69,202,7,170,175,45,149,2,1,136,23,0,201,166,202,254,13,69,193,7,170,7,170,175,45,149,2,1,136,23,0,142,140]
2021-12-24T03:30:01.523Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,12,69,202,7,170,175,45,149,2,1,136,23,0,201,166,202,254,13,69,193,7,170,7,170,175,45,149,2,1,136,23,0,142,140]
2021-12-24T03:30:01.523Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 12 - 2 - 5 - 202 - [7,170,175,45,149,2,1,136,23,0,201,166] - 202
2021-12-24T03:30:01.523Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - tcDeviceInd - {"nwkaddr":43527,"extaddr":"0x0017880102952daf","parentaddr":42697}
2021-12-24T03:30:01.523Z zigbee-herdsman:controller:log Device '0x0017880102952daf' joined
2021-12-24T03:30:01.524Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,13,69,193,7,170,7,170,175,45,149,2,1,136,23,0,142,140]
2021-12-24T03:30:01.524Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 13 - 2 - 5 - 193 - [7,170,7,170,175,45,149,2,1,136,23,0,142] - 140
2021-12-24T03:30:01.524Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - endDeviceAnnceInd - {"srcaddr":43527,"nwkaddr":43527,"ieeeaddr":"0x0017880102952daf","capabilities":142}
2021-12-24T03:30:01.524Z zigbee-herdsman:controller:log Device announce '0x0017880102952daf'
Zigbee2MQTT:info  2021-12-24 03:30:01: MQTT publish: topic 'zigbee2mqtt/bridge/event', payload '{"data":{"friendly_name":"0x0017880102952daf","ieee_address":"0x0017880102952daf"},"type":"device_announce"}'
Zigbee2MQTT:info  2021-12-24 03:30:01: MQTT publish: topic 'zigbee2mqtt/bridge/log', payload '{"message":"announce","meta":{"friendly_name":"0x0017880102952daf"},"type":"device_announced"}'
2021-12-24T03:30:01.721Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
2021-12-24T03:30:01.721Z zigbee-herdsman:controller:log Device '0x0017880102952daf' accepted by handler
Zigbee2MQTT:info  2021-12-24 03:30:01: MQTT publish: topic 'zigbee2mqtt/0x0017880102952daf', payload '{"device":{"applicationVersion":2,"dateCode":"20191218","friendlyName":"0x0017880102952daf","hardwareVersion":1,"ieeeAddr":"0x0017880102952daf","manufacturerID":4107,"manufacturerName":"Philips","model":"9290011370","networkAddress":43527,"powerSource":"Mains (single phase)","softwareBuildID":"1.50.2_r30933","stackVersion":1,"type":"Router","zclVersion":1},"last_seen":"2021-12-24T03:30:01.721Z","linkquality":72,"state":null,"update_available":null}'
2021-12-24T03:30:01.725Z zigbee-herdsman:controller:log Not interviewing '0x0017880102952daf', completed 'true', in progress 'false'
Zigbee2MQTT:debug 2021-12-24 03:30:01: Received MQTT message on 'homeassistant/light/0x0017880102952daf/light/config' with data '{"availability":[{"topic":"zigbee2mqtt/bridge/state"}],"brightness":true,"brightness_scale":254,"command_topic":"zigbee2mqtt/0x0017880102952daf/set","device":{"identifiers":["zigbee2mqtt_0x0017880102952daf"],"manufacturer":"Philips","model":"Hue white A60 bulb E27/B22 (9290011370)","name":"0x0017880102952daf","sw_version":"1.50.2_r30933"},"effect":true,"effect_list":["blink","breathe","okay","channel_change","finish_effect","stop_effect"],"json_attributes_topic":"zigbee2mqtt/0x0017880102952daf","name":"0x0017880102952daf","schema":"json","state_topic":"zigbee2mqtt/0x0017880102952daf","unique_id":"0x0017880102952daf_light_zigbee2mqtt"}'
Zigbee2MQTT:debug 2021-12-24 03:30:01: Received MQTT message on 'homeassistant/sensor/0x0017880102952daf/linkquality/config' with data '{"availability":[{"topic":"zigbee2mqtt/bridge/state"}],"device":{"identifiers":["zigbee2mqtt_0x0017880102952daf"],"manufacturer":"Philips","model":"Hue white A60 bulb E27/B22 (9290011370)","name":"0x0017880102952daf","sw_version":"1.50.2_r30933"},"enabled_by_default":false,"entity_category":"diagnostic","icon":"mdi:signal","json_attributes_topic":"zigbee2mqtt/0x0017880102952daf","name":"0x0017880102952daf linkquality","state_class":"measurement","state_topic":"zigbee2mqtt/0x0017880102952daf","unique_id":"0x0017880102952daf_linkquality_zigbee2mqtt","unit_of_measurement":"lqi","value_template":"{{ value_json.linkquality }}"}'
Zigbee2MQTT:debug 2021-12-24 03:30:01: Received MQTT message on 'homeassistant/sensor/0x0017880102952daf/last_seen/config' with data '{"availability":[{"topic":"zigbee2mqtt/bridge/state"}],"device":{"identifiers":["zigbee2mqtt_0x0017880102952daf"],"manufacturer":"Philips","model":"Hue white A60 bulb E27/B22 (9290011370)","name":"0x0017880102952daf","sw_version":"1.50.2_r30933"},"device_class":"timestamp","enabled_by_default":false,"entity_category":"diagnostic","icon":"mdi:clock","json_attributes_topic":"zigbee2mqtt/0x0017880102952daf","name":"0x0017880102952daf last seen","state_topic":"zigbee2mqtt/0x0017880102952daf","unique_id":"0x0017880102952daf_last_seen_zigbee2mqtt","value_template":"{{ value_json.last_seen }}"}'
Zigbee2MQTT:debug 2021-12-24 03:30:01: Received MQTT message on 'homeassistant/sensor/0x0017880102952daf/update_state/config' with data '{"availability":[{"topic":"zigbee2mqtt/bridge/state"}],"device":{"identifiers":["zigbee2mqtt_0x0017880102952daf"],"manufacturer":"Philips","model":"Hue white A60 bulb E27/B22 (9290011370)","name":"0x0017880102952daf","sw_version":"1.50.2_r30933"},"enabled_by_default":false,"entity_category":"diagnostic","icon":"mdi:update","json_attributes_topic":"zigbee2mqtt/0x0017880102952daf","name":"0x0017880102952daf update state","state_topic":"zigbee2mqtt/0x0017880102952daf","unique_id":"0x0017880102952daf_update_state_zigbee2mqtt","value_template":"{{ value_json['update']['state'] }}"}'
Zigbee2MQTT:debug 2021-12-24 03:30:01: Received MQTT message on 'homeassistant/binary_sensor/0x0017880102952daf/update_available/config' with data '{"availability":[{"topic":"zigbee2mqtt/bridge/state"}],"device":{"identifiers":["zigbee2mqtt_0x0017880102952daf"],"manufacturer":"Philips","model":"Hue white A60 bulb E27/B22 (9290011370)","name":"0x0017880102952daf","sw_version":"1.50.2_r30933"},"device_class":"update","enabled_by_default":true,"entity_category":"diagnostic","json_attributes_topic":"zigbee2mqtt/0x0017880102952daf","name":"0x0017880102952daf update available","payload_off":false,"payload_on":true,"state_topic":"zigbee2mqtt/0x0017880102952daf","unique_id":"0x0017880102952daf_update_available_zigbee2mqtt","value_template":"{{ value_json['update']['state'] == \"available\" }}"}'
Zigbee2MQTT:debug 2021-12-24 03:30:03: Retrieving state of '0x0017880102952daf' after reconnect
2021-12-24T03:30:03.723Z zigbee-herdsman:controller:endpoint Read 0x0017880102952daf/11 genOnOff(["onOff"], {"timeout":10000,"disableResponse":false,"disableRecovery":false,"disableDefaultResponse":true,"direction":0,"srcEndpoint":null,"reservedBits":0,"manufacturerCode":null,"transactionSequenceNumber":null,"writeUndiv":false})
2021-12-24T03:30:03.723Z zigbee-herdsman:adapter:zStack:adapter sendZclFrameToEndpointInternal 0x0017880102952daf:43527/11 (0,0,1)
2021-12-24T03:30:03.723Z zigbee-herdsman:adapter:zStack:znp:SREQ --> AF - dataRequest - {"dstaddr":43527,"destendpoint":11,"srcendpoint":1,"clusterid":6,"transid":61,"options":0,"radius":30,"len":5,"data":{"type":"Buffer","data":[16,50,0,0,0]}}
2021-12-24T03:30:03.724Z zigbee-herdsman:adapter:zStack:unpi:writer --> frame [254,15,36,1,7,170,11,1,6,0,61,0,30,5,16,50,0,0,0,143]
2021-12-24T03:30:03.738Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,1,100,1,0,100]
2021-12-24T03:30:03.739Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,1,100,1,0,100]
2021-12-24T03:30:03.739Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 1 - 3 - 4 - 1 - [0] - 100
2021-12-24T03:30:03.739Z zigbee-herdsman:adapter:zStack:znp:SRSP <-- AF - dataRequest - {"status":0}
2021-12-24T03:30:03.739Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
2021-12-24T03:30:04.103Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,3,68,128,0,1,61,251]
2021-12-24T03:30:04.103Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,3,68,128,0,1,61,251]
2021-12-24T03:30:04.103Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 3 - 2 - 4 - 128 - [0,1,61] - 251
2021-12-24T03:30:04.103Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- AF - dataConfirm - {"status":0,"endpoint":1,"transid":61}
2021-12-24T03:30:04.104Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
Zigbee2MQTT:debug 2021-12-24 03:30:04: Received Zigbee message from '0x0017880102952daf', type 'readResponse', cluster 'genOnOff', data '{"onOff":1}' from endpoint 11 with groupID 0
2021-12-24T03:30:04.163Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,28,68,129,0,0,6,0,7,170,11,1,0,69,0,16,79,137,0,0,8,24,50,1,0,0,0,16,1,201,166,28,170]
2021-12-24T03:30:04.163Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,28,68,129,0,0,6,0,7,170,11,1,0,69,0,16,79,137,0,0,8,24,50,1,0,0,0,16,1,201,166,28,170]
2021-12-24T03:30:04.163Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 28 - 2 - 4 - 129 - [0,0,6,0,7,170,11,1,0,69,0,16,79,137,0,0,8,24,50,1,0,0,0,16,1,201,166,28] - 170
2021-12-24T03:30:04.163Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- AF - incomingMsg - {"groupid":0,"clusterid":6,"srcaddr":43527,"srcendpoint":11,"dstendpoint":1,"wasbroadcast":0,"linkquality":69,"securityuse":0,"timestamp":8998672,"transseqnumber":0,"len":8,"data":{"type":"Buffer","data":[24,50,1,0,0,0,16,1]}}
2021-12-24T03:30:04.164Z zigbee-herdsman:controller:log Received 'zcl' data '{"frame":{"Header":{"frameControl":{"frameType":0,"manufacturerSpecific":false,"direction":1,"disableDefaultResponse":true,"reservedBits":0},"transactionSequenceNumber":50,"manufacturerCode":null,"commandIdentifier":1},"Payload":[{"attrId":0,"status":0,"dataType":16,"attrData":1}],"Command":{"ID":1,"name":"readRsp","parameters":[{"name":"attrId","type":33},{"name":"status","type":32},{"name":"dataType","type":32,"conditions":[{"type":"statusEquals","value":0}]},{"name":"attrData","type":1000,"conditions":[{"type":"statusEquals","value":0}]}]}},"address":43527,"endpoint":11,"linkquality":69,"groupID":0,"wasBroadcast":false,"destinationEndpoint":1}'
2021-12-24T03:30:04.167Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
Zigbee2MQTT:info  2021-12-24 03:30:04: MQTT publish: topic 'zigbee2mqtt/0x0017880102952daf', payload '{"device":{"applicationVersion":2,"dateCode":"20191218","friendlyName":"0x0017880102952daf","hardwareVersion":1,"ieeeAddr":"0x0017880102952daf","manufacturerID":4107,"manufacturerName":"Philips","model":"9290011370","networkAddress":43527,"powerSource":"Mains (single phase)","softwareBuildID":"1.50.2_r30933","stackVersion":1,"type":"Router","zclVersion":1},"last_seen":"2021-12-24T03:30:04.165Z","linkquality":69,"state":"ON","update_available":null}'
2021-12-24T03:30:04.173Z zigbee-herdsman:controller:endpoint Read 0x0017880102952daf/11 genLevelCtrl(["currentLevel"], {"timeout":10000,"disableResponse":false,"disableRecovery":false,"disableDefaultResponse":true,"direction":0,"srcEndpoint":null,"reservedBits":0,"manufacturerCode":null,"transactionSequenceNumber":null,"writeUndiv":false})
2021-12-24T03:30:04.174Z zigbee-herdsman:adapter:zStack:adapter sendZclFrameToEndpointInternal 0x0017880102952daf:43527/11 (0,0,1)
2021-12-24T03:30:04.174Z zigbee-herdsman:adapter:zStack:znp:SREQ --> AF - dataRequest - {"dstaddr":43527,"destendpoint":11,"srcendpoint":1,"clusterid":8,"transid":62,"options":0,"radius":30,"len":5,"data":{"type":"Buffer","data":[16,51,0,0,0]}}
2021-12-24T03:30:04.174Z zigbee-herdsman:adapter:zStack:unpi:writer --> frame [254,15,36,1,7,170,11,1,8,0,62,0,30,5,16,51,0,0,0,131]
2021-12-24T03:30:04.188Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,1,100,1,0,100]
2021-12-24T03:30:04.188Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,1,100,1,0,100]
2021-12-24T03:30:04.188Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 1 - 3 - 4 - 1 - [0] - 100
2021-12-24T03:30:04.188Z zigbee-herdsman:adapter:zStack:znp:SRSP <-- AF - dataRequest - {"status":0}
2021-12-24T03:30:04.188Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
2021-12-24T03:30:04.191Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,3,68,128,0,1,62,248]
2021-12-24T03:30:04.191Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,3,68,128,0,1,62,248]
2021-12-24T03:30:04.192Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 3 - 2 - 4 - 128 - [0,1,62] - 248
2021-12-24T03:30:04.192Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- AF - dataConfirm - {"status":0,"endpoint":1,"transid":62}
2021-12-24T03:30:04.192Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
2021-12-24T03:30:04.225Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,28,68,129,0,0,8,0,7,170,11,1,0,69,0,137,100,137,0,0,8,24,51,1,0,0,0,32,254,201,166,28,216]
2021-12-24T03:30:04.225Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,28,68,129,0,0,8,0,7,170,11,1,0,69,0,137,100,137,0,0,8,24,51,1,0,0,0,32,254,201,166,28,216]
2021-12-24T03:30:04.225Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 28 - 2 - 4 - 129 - [0,0,8,0,7,170,11,1,0,69,0,137,100,137,0,0,8,24,51,1,0,0,0,32,254,201,166,28] - 216
2021-12-24T03:30:04.226Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- AF - incomingMsg - {"groupid":0,"clusterid":8,"srcaddr":43527,"srcendpoint":11,"dstendpoint":1,"wasbroadcast":0,"linkquality":69,"securityuse":0,"timestamp":9004169,"transseqnumber":0,"len":8,"data":{"type":"Buffer","data":[24,51,1,0,0,0,32,254]}}
2021-12-24T03:30:04.227Z zigbee-herdsman:controller:log Received 'zcl' data '{"frame":{"Header":{"frameControl":{"frameType":0,"manufacturerSpecific":false,"direction":1,"disableDefaultResponse":true,"reservedBits":0},"transactionSequenceNumber":51,"manufacturerCode":null,"commandIdentifier":1},"Payload":[{"attrId":0,"status":0,"dataType":32,"attrData":254}],"Command":{"ID":1,"name":"readRsp","parameters":[{"name":"attrId","type":33},{"name":"status","type":32},{"name":"dataType","type":32,"conditions":[{"type":"statusEquals","value":0}]},{"name":"attrData","type":1000,"conditions":[{"type":"statusEquals","value":0}]}]}},"address":43527,"endpoint":11,"linkquality":69,"groupID":0,"wasBroadcast":false,"destinationEndpoint":1}'
Zigbee2MQTT:debug 2021-12-24 03:30:04: Received Zigbee message from '0x0017880102952daf', type 'readResponse', cluster 'genLevelCtrl', data '{"currentLevel":254}' from endpoint 11 with groupID 0
2021-12-24T03:30:04.230Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
Zigbee2MQTT:info  2021-12-24 03:30:04: MQTT publish: topic 'zigbee2mqtt/0x0017880102952daf', payload '{"brightness":254,"device":{"applicationVersion":2,"dateCode":"20191218","friendlyName":"0x0017880102952daf","hardwareVersion":1,"ieeeAddr":"0x0017880102952daf","manufacturerID":4107,"manufacturerName":"Philips","model":"9290011370","networkAddress":43527,"powerSource":"Mains (single phase)","softwareBuildID":"1.50.2_r30933","stackVersion":1,"type":"Router","zclVersion":1},"last_seen":"2021-12-24T03:30:04.227Z","linkquality":69,"state":"ON","update_available":null}'
2021-12-24T03:30:11.295Z zigbee-herdsman:adapter:zStack:znp:SREQ --> ZDO - mgmtPermitJoinReq - {"addrmode":15,"dstaddr":65532,"duration":254,"tcsignificance":0}
2021-12-24T03:30:11.295Z zigbee-herdsman:adapter:zStack:unpi:writer --> frame [254,5,37,54,15,252,255,254,0,228]
2021-12-24T03:30:11.309Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,1,101,54,0,82]
2021-12-24T03:30:11.309Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,1,101,54,0,82]
2021-12-24T03:30:11.309Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 1 - 3 - 5 - 54 - [0] - 82
2021-12-24T03:30:11.309Z zigbee-herdsman:adapter:zStack:znp:SRSP <-- ZDO - mgmtPermitJoinReq - {"status":0}
2021-12-24T03:30:11.309Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
2021-12-24T03:30:11.310Z zigbee-herdsman:adapter:zStack:znp:SREQ --> AF - dataRequestExt - {"dstaddrmode":2,"dstaddr":"0x000000000000fffd","destendpoint":242,"dstpanid":0,"srcendpoint":242,"clusterid":33,"transid":63,"options":0,"radius":30,"len":6,"data":{"type":"Buffer","data":[25,52,2,11,254,0]}}
2021-12-24T03:30:11.311Z zigbee-herdsman:adapter:zStack:unpi:writer --> frame [254,26,36,2,2,253,255,0,0,0,0,0,0,242,0,0,242,33,0,63,0,30,6,0,25,52,2,11,254,0,224]
2021-12-24T03:30:11.312Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,3,69,182,0,0,0,240]
2021-12-24T03:30:11.312Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,3,69,182,0,0,0,240]
2021-12-24T03:30:11.312Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 3 - 2 - 5 - 182 - [0,0,0] - 240
2021-12-24T03:30:11.312Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - mgmtPermitJoinRsp - {"srcaddr":0,"status":0}
2021-12-24T03:30:11.312Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
2021-12-24T03:30:11.325Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,1,100,2,0,103]
2021-12-24T03:30:11.325Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,1,100,2,0,103]
2021-12-24T03:30:11.325Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 1 - 3 - 4 - 2 - [0] - 103
2021-12-24T03:30:11.326Z zigbee-herdsman:adapter:zStack:znp:SRSP <-- AF - dataRequestExt - {"status":0}
2021-12-24T03:30:11.326Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
2021-12-24T03:30:11.328Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,3,68,128,0,242,63,10]
2021-12-24T03:30:11.329Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,3,68,128,0,242,63,10]
2021-12-24T03:30:11.329Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 3 - 2 - 4 - 128 - [0,242,63] - 10
2021-12-24T03:30:11.329Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- AF - dataConfirm - {"status":0,"endpoint":242,"transid":63}
2021-12-24T03:30:11.329Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
2021-12-24T03:30:33.758Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,11,69,200,71,122,35,27,206,254,255,114,2,92,1,97]
2021-12-24T03:30:33.758Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,11,69,200,71,122,35,27,206,254,255,114,2,92,1,97]
2021-12-24T03:30:33.758Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 11 - 2 - 5 - 200 - [71,122,35,27,206,254,255,114,2,92,1] - 97
2021-12-24T03:30:33.758Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - concentratorIndCb - {"srcaddr":31303,"extaddr":"0x5c0272fffece1b23","pktCost":1}
2021-12-24T03:30:33.758Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
2021-12-24T03:30:55.676Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,11,69,200,85,238,227,254,205,254,255,114,2,92,1,193]
2021-12-24T03:30:55.676Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,11,69,200,85,238,227,254,205,254,255,114,2,92,1,193]
2021-12-24T03:30:55.676Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 11 - 2 - 5 - 200 - [85,238,227,254,205,254,255,114,2,92,1] - 193
2021-12-24T03:30:55.676Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - concentratorIndCb - {"srcaddr":61013,"extaddr":"0x5c0272fffecdfee3","pktCost":1}
2021-12-24T03:30:55.677Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
Zigbee2MQTT:debug 2021-12-24 03:30:58: Received MQTT message on 'zigbee2mqtt/bridge/request/device/rename' with data '{"from":"0x0017880102952daf","homeassistant_rename":false,"to":"kitchen Sink","transaction":"uc2wr-3"}'
Zigbee2MQTT:info  2021-12-24 03:30:58: MQTT publish: topic 'zigbee2mqtt/0x0017880102952daf', payload ''
Zigbee2MQTT:info  2021-12-24 03:30:58: MQTT publish: topic 'zigbee2mqtt/kitchen Sink/availability', payload 'online'
Zigbee2MQTT:debug 2021-12-24 03:30:58: Refreshing Home Assistant discovery topic for '0x0017880102952daf'
Zigbee2MQTT:info  2021-12-24 03:30:58: MQTT publish: topic 'homeassistant/light/0x0017880102952daf/light/config', payload '{"availability":[{"topic":"zigbee2mqtt/bridge/state"}],"brightness":true,"brightness_scale":254,"command_topic":"zigbee2mqtt/kitchen Sink/set","device":{"identifiers":["zigbee2mqtt_0x0017880102952daf"],"manufacturer":"Philips","model":"Hue white A60 bulb E27/B22 (9290011370)","name":"kitchen Sink","sw_version":"1.50.2_r30933"},"effect":true,"effect_list":["blink","breathe","okay","channel_change","finish_effect","stop_effect"],"json_attributes_topic":"zigbee2mqtt/kitchen Sink","name":"kitchen Sink","schema":"json","state_topic":"zigbee2mqtt/kitchen Sink","unique_id":"0x0017880102952daf_light_zigbee2mqtt"}'
Zigbee2MQTT:info  2021-12-24 03:30:58: MQTT publish: topic 'homeassistant/sensor/0x0017880102952daf/linkquality/config', payload '{"availability":[{"topic":"zigbee2mqtt/bridge/state"}],"device":{"identifiers":["zigbee2mqtt_0x0017880102952daf"],"manufacturer":"Philips","model":"Hue white A60 bulb E27/B22 (9290011370)","name":"kitchen Sink","sw_version":"1.50.2_r30933"},"enabled_by_default":false,"entity_category":"diagnostic","icon":"mdi:signal","json_attributes_topic":"zigbee2mqtt/kitchen Sink","name":"kitchen Sink linkquality","state_class":"measurement","state_topic":"zigbee2mqtt/kitchen Sink","unique_id":"0x0017880102952daf_linkquality_zigbee2mqtt","unit_of_measurement":"lqi","value_template":"{{ value_json.linkquality }}"}'
Zigbee2MQTT:info  2021-12-24 03:30:58: MQTT publish: topic 'homeassistant/sensor/0x0017880102952daf/last_seen/config', payload '{"availability":[{"topic":"zigbee2mqtt/bridge/state"}],"device":{"identifiers":["zigbee2mqtt_0x0017880102952daf"],"manufacturer":"Philips","model":"Hue white A60 bulb E27/B22 (9290011370)","name":"kitchen Sink","sw_version":"1.50.2_r30933"},"device_class":"timestamp","enabled_by_default":false,"entity_category":"diagnostic","icon":"mdi:clock","json_attributes_topic":"zigbee2mqtt/kitchen Sink","name":"kitchen Sink last seen","state_topic":"zigbee2mqtt/kitchen Sink","unique_id":"0x0017880102952daf_last_seen_zigbee2mqtt","value_template":"{{ value_json.last_seen }}"}'
Zigbee2MQTT:info  2021-12-24 03:30:58: MQTT publish: topic 'homeassistant/sensor/0x0017880102952daf/update_state/config', payload '{"availability":[{"topic":"zigbee2mqtt/bridge/state"}],"device":{"identifiers":["zigbee2mqtt_0x0017880102952daf"],"manufacturer":"Philips","model":"Hue white A60 bulb E27/B22 (9290011370)","name":"kitchen Sink","sw_version":"1.50.2_r30933"},"enabled_by_default":false,"entity_category":"diagnostic","icon":"mdi:update","json_attributes_topic":"zigbee2mqtt/kitchen Sink","name":"kitchen Sink update state","state_topic":"zigbee2mqtt/kitchen Sink","unique_id":"0x0017880102952daf_update_state_zigbee2mqtt","value_template":"{{ value_json['update']['state'] }}"}'
Zigbee2MQTT:info  2021-12-24 03:30:58: MQTT publish: topic 'homeassistant/binary_sensor/0x0017880102952daf/update_available/config', payload '{"availability":[{"topic":"zigbee2mqtt/bridge/state"}],"device":{"identifiers":["zigbee2mqtt_0x0017880102952daf"],"manufacturer":"Philips","model":"Hue white A60 bulb E27/B22 (9290011370)","name":"kitchen Sink","sw_version":"1.50.2_r30933"},"device_class":"update","enabled_by_default":true,"entity_category":"diagnostic","json_attributes_topic":"zigbee2mqtt/kitchen Sink","name":"kitchen Sink update available","payload_off":false,"payload_on":true,"state_topic":"zigbee2mqtt/kitchen Sink","unique_id":"0x0017880102952daf_update_available_zigbee2mqtt","value_template":"{{ value_json['update']['state'] == \"available\" }}"}'
Zigbee2MQTT:info  2021-12-24 03:30:58: MQTT publish: topic 'zigbee2mqtt/kitchen Sink', payload '{"brightness":254,"device":{"applicationVersion":2,"dateCode":"20191218","friendlyName":"kitchen Sink","hardwareVersion":1,"ieeeAddr":"0x0017880102952daf","manufacturerID":4107,"manufacturerName":"Philips","model":"9290011370","networkAddress":43527,"powerSource":"Mains (single phase)","softwareBuildID":"1.50.2_r30933","stackVersion":1,"type":"Router","zclVersion":1},"last_seen":"2021-12-24T03:30:04.227Z","linkquality":69,"state":"ON","update_available":null}'
Zigbee2MQTT:info  2021-12-24 03:30:58: MQTT publish: topic 'zigbee2mqtt/bridge/response/device/rename', payload '{"data":{"from":"0x0017880102952daf","homeassistant_rename":false,"to":"kitchen Sink"},"status":"ok","transaction":"uc2wr-3"}'
Zigbee2MQTT:debug 2021-12-24 03:30:58: Received MQTT message on 'homeassistant/light/0x0017880102952daf/light/config' with data '{"availability":[{"topic":"zigbee2mqtt/bridge/state"}],"brightness":true,"brightness_scale":254,"command_topic":"zigbee2mqtt/kitchen Sink/set","device":{"identifiers":["zigbee2mqtt_0x0017880102952daf"],"manufacturer":"Philips","model":"Hue white A60 bulb E27/B22 (9290011370)","name":"kitchen Sink","sw_version":"1.50.2_r30933"},"effect":true,"effect_list":["blink","breathe","okay","channel_change","finish_effect","stop_effect"],"json_attributes_topic":"zigbee2mqtt/kitchen Sink","name":"kitchen Sink","schema":"json","state_topic":"zigbee2mqtt/kitchen Sink","unique_id":"0x0017880102952daf_light_zigbee2mqtt"}'
Zigbee2MQTT:debug 2021-12-24 03:30:58: Received MQTT message on 'homeassistant/sensor/0x0017880102952daf/linkquality/config' with data '{"availability":[{"topic":"zigbee2mqtt/bridge/state"}],"device":{"identifiers":["zigbee2mqtt_0x0017880102952daf"],"manufacturer":"Philips","model":"Hue white A60 bulb E27/B22 (9290011370)","name":"kitchen Sink","sw_version":"1.50.2_r30933"},"enabled_by_default":false,"entity_category":"diagnostic","icon":"mdi:signal","json_attributes_topic":"zigbee2mqtt/kitchen Sink","name":"kitchen Sink linkquality","state_class":"measurement","state_topic":"zigbee2mqtt/kitchen Sink","unique_id":"0x0017880102952daf_linkquality_zigbee2mqtt","unit_of_measurement":"lqi","value_template":"{{ value_json.linkquality }}"}'
Zigbee2MQTT:debug 2021-12-24 03:30:58: Received MQTT message on 'homeassistant/sensor/0x0017880102952daf/last_seen/config' with data '{"availability":[{"topic":"zigbee2mqtt/bridge/state"}],"device":{"identifiers":["zigbee2mqtt_0x0017880102952daf"],"manufacturer":"Philips","model":"Hue white A60 bulb E27/B22 (9290011370)","name":"kitchen Sink","sw_version":"1.50.2_r30933"},"device_class":"timestamp","enabled_by_default":false,"entity_category":"diagnostic","icon":"mdi:clock","json_attributes_topic":"zigbee2mqtt/kitchen Sink","name":"kitchen Sink last seen","state_topic":"zigbee2mqtt/kitchen Sink","unique_id":"0x0017880102952daf_last_seen_zigbee2mqtt","value_template":"{{ value_json.last_seen }}"}'
Zigbee2MQTT:debug 2021-12-24 03:30:58: Received MQTT message on 'homeassistant/sensor/0x0017880102952daf/update_state/config' with data '{"availability":[{"topic":"zigbee2mqtt/bridge/state"}],"device":{"identifiers":["zigbee2mqtt_0x0017880102952daf"],"manufacturer":"Philips","model":"Hue white A60 bulb E27/B22 (9290011370)","name":"kitchen Sink","sw_version":"1.50.2_r30933"},"enabled_by_default":false,"entity_category":"diagnostic","icon":"mdi:update","json_attributes_topic":"zigbee2mqtt/kitchen Sink","name":"kitchen Sink update state","state_topic":"zigbee2mqtt/kitchen Sink","unique_id":"0x0017880102952daf_update_state_zigbee2mqtt","value_template":"{{ value_json['update']['state'] }}"}'
Zigbee2MQTT:debug 2021-12-24 03:30:58: Received MQTT message on 'homeassistant/binary_sensor/0x0017880102952daf/update_available/config' with data '{"availability":[{"topic":"zigbee2mqtt/bridge/state"}],"device":{"identifiers":["zigbee2mqtt_0x0017880102952daf"],"manufacturer":"Philips","model":"Hue white A60 bulb E27/B22 (9290011370)","name":"kitchen Sink","sw_version":"1.50.2_r30933"},"device_class":"update","enabled_by_default":true,"entity_category":"diagnostic","json_attributes_topic":"zigbee2mqtt/kitchen Sink","name":"kitchen Sink update available","payload_off":false,"payload_on":true,"state_topic":"zigbee2mqtt/kitchen Sink","unique_id":"0x0017880102952daf_update_available_zigbee2mqtt","value_template":"{{ value_json['update']['state'] == \"available\" }}"}'
2021-12-24T03:31:36.034Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,11,69,200,71,122,35,27,206,254,255,114,2,92,1,97]
2021-12-24T03:31:36.034Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,11,69,200,71,122,35,27,206,254,255,114,2,92,1,97]
2021-12-24T03:31:36.034Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 11 - 2 - 5 - 200 - [71,122,35,27,206,254,255,114,2,92,1] - 97
2021-12-24T03:31:36.035Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - concentratorIndCb - {"srcaddr":31303,"extaddr":"0x5c0272fffece1b23","pktCost":1}
2021-12-24T03:31:36.035Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
Zigbee2MQTT:debug 2021-12-24 03:31:38: Saving state to file /data/state.json
2021-12-24T03:31:57.685Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,11,69,200,85,238,227,254,205,254,255,114,2,92,1,193]
2021-12-24T03:31:57.685Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,11,69,200,85,238,227,254,205,254,255,114,2,92,1,193]
2021-12-24T03:31:57.685Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 11 - 2 - 5 - 200 - [85,238,227,254,205,254,255,114,2,92,1] - 193
2021-12-24T03:31:57.686Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - concentratorIndCb - {"srcaddr":61013,"extaddr":"0x5c0272fffecdfee3","pktCost":1}
2021-12-24T03:31:57.686Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []
2021-12-24T03:32:38.281Z zigbee-herdsman:adapter:zStack:unpi:parser <-- [254,11,69,200,71,122,35,27,206,254,255,114,2,92,1,97]
2021-12-24T03:32:38.282Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext [254,11,69,200,71,122,35,27,206,254,255,114,2,92,1,97]
2021-12-24T03:32:38.283Z zigbee-herdsman:adapter:zStack:unpi:parser --> parsed 11 - 2 - 5 - 200 - [71,122,35,27,206,254,255,114,2,92,1] - 97
2021-12-24T03:32:38.283Z zigbee-herdsman:adapter:zStack:znp:AREQ <-- ZDO - concentratorIndCb - {"srcaddr":31303,"extaddr":"0x5c0272fffece1b23","pktCost":1}
2021-12-24T03:32:38.284Z zigbee-herdsman:adapter:zStack:unpi:parser --- parseNext []

