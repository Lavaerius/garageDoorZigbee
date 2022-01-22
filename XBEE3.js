// https://www.nxp.com/docs/en/user-guide/JN-UG-3076.pdf

const fz = require('zigbee-herdsman-converters/converters/fromZigbee');
const tz = require('zigbee-herdsman-converters/converters/toZigbee');
const exposes = require('zigbee-herdsman-converters/lib/exposes');
const utils = require('zigbee-herdsman-converters/lib/utils');
const e = exposes.presets;
const ea = exposes.access;



const definition = {
    zigbeeModel: ['Digi GarageDoor'],
    model: 'Digi GarageDoor homemade',
    vendor: 'Digi NathaF',
    description: 'Garage door xbee unit',
    fromZigbee: [fz.on_off, fzlocal.moving_state, fzlocal.barrier_position, fzlocal.open_period, fzlocal.close_period],
    toZigbee: [tz.on_off, tzlocal.barrier_position, tzlocal.stop],
    meta: {disableDefaultResponse: true},
    exposes: [e.switch(),e.cover_position()],
    configure: async (device, coordinatorEndpoint, logger) => {
        const endpoint = device.getEndpoint(8);
        await reporting.bind(endpoint, coordinatorEndpoint, ['genOnOff']);
        await reporting.onOff(endpoint);
        await reporting.bind(endpoint,coordinatorEndpoint,['barrierControl']);
        await reporting.barrierPosition(endpoint);
    },
};

const fzLocal = {
    moving_state: {
        cluster: 'barrierControl',
        type: ['attributeReport', 'readResponse'],
        convert: (model, msg, publish, options, meta) => {
            const movingState = msg.data['movingState']
            const lookup = {
                0: 'Stopped',
                1: 'Closing',
                2: 'Opening',
            };
            return lookup[movingState];
        },
    },
    barrier_position: {
        cluster: 'barrierControl',
        type: ['attributeReport', 'readResponse'],
        convert: (model, msg, publish, options, meta) => {
        const barrierPosition = msg.data['barrierPosition']
        return barrierPosition;
        },
    open_period: {
        cluster: 'barrierControl',
        type: ['attributeReport', 'readResponse'],
        convert: (model, msg, publish, options, meta) => {
            const openPeriod = msg.data['openPeriod']
            return openPeriod
        },
    },
    close_period: {
        cluster: 'barrierControl',
        type: ['attributeReport', 'readResponse'],
        convert: (model, msg, publish, options, meta) => {
            const closePeriod = msg.data['closePeriod']
            return closePeriod
        },
    },
},
};

//entity is the end point object with a write function, first argument is the cluster
//I think it has a command function also, gonna try that, write is to write an attribute, command is for a command
//key is the value defined map of k:v for command
const tzlocal ={
    go_to_percent: {
    key: ['goToPercent'], 
     convertSet: async (entity, key, value, meta) => {

        await entity.command('barrierControl','goToPercent',0x64,utils.getOptions(meta.mapped, entity))
     },
    },
};
module.exports = definition; 
