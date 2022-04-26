// https://www.nxp.com/docs/en/user-guide/JN-UG-3076.pdf

const fz = require('zigbee-herdsman-converters/converters/fromZigbee');
const tz = require('zigbee-herdsman-converters/converters/toZigbee');
const exposes = require('zigbee-herdsman-converters/lib/exposes');
const reporting = require('zigbee-herdsman-converters/lib/reporting');
const utils = require('zigbee-herdsman-converters/lib/utils');
const extend = require('zigbee-herdsman-converters/lib/extend');
const e = exposes.presets;
const ea = exposes.access;


const fzlocal1 = {
    moving_state: {
        cluster: 'barrierControl',
        type: ['attributeReport','readResponse'],
        convert: (model, msg, publish, options, meta) => {
            const movingState = msg.data['256'];
            const lookup = {
                0: 'Stopped',
                1: 'Closing',
                2: 'Opening',
            };
	    const action = lookup[movingState]
            return {'movingState': action}
        },
    },

    position: {
        cluster: 'barrierControl',
        type: ['attributeReport','readResponse'],
        convert: (model, msg, publish, options, meta) => {
        const barrierPosition = msg.data['2560'];
	const lookup = {
		0x00: 'Closed',
		0x32: 'ajar',
		0x64: 'Open',
	
	};
	const action = lookup[barrierPosition]
        return {'barrierPosition': action}
        },
    },
    open_period: {
        cluster: 'barrierControl',
        type: ['attributeReport', 'readResponse'],
        convert: (model, msg, publish, options, meta) => {
            const openPeriod = msg.data['openPeriod'];
            return openPeriod;
        },
    },
    close_period: {
        cluster: 'barrierControl',
        type: ['attributeReport', 'readResponse'],
        convert: (model, msg, publish, options, meta) => {
            const closePeriod = msg.data['closePeriod'];
            return closePeriod;
        },
    },
};

//entity is the end point object with a write function, first argument is the cluster
//I think it has a command function also, gonna try that, write is to write an attribute, command is for a command
//key is the value defined map of k:v for command
const tzlocal ={
    go_to_percent: {
    key: ['go_to_percent'], 
     convertSet: async (entity, key, value, meta) => {

        await entity.command('barrierControl','go_to_percent',0x64,utils.getOptions(meta.mapped, entity))
     },
    },
};

const definition = {
    zigbeeModel: ['Digi GarageDoor'],
    model: 'Digi GarageDoor homemade',
    vendor: 'Digi Nathan',
    description: 'Garage door xbee unit it begins',
    fromZigbee: [fz.on_off, fzlocal1.moving_state, fzlocal1.position],
    toZigbee: [tz.on_off,tzlocal.go_to_percent],// tzlocal.go_to_percent, tzlocal.stop],
    meta: {disableDefaultResponse: true},
    exposes: [],//, e.cover_position()],
    configure: async (device, coordinatorEndpoint, logger) => {
        const endpoint = device.getEndpoint(8);
    },
};

module.exports = definition; 
