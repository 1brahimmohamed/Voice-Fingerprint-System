import React, {Component, useEffect} from 'react';
import CanvasJSReact from '../../Packages/CanvasJS/canvasjs.react';
import Door from "../Door/Door";

let CanvasJS = CanvasJSReact.CanvasJS;
let CanvasJSChart = CanvasJSReact.CanvasJSChart;


function ScatterPlotCanvas(props) {
	let dataObjects = []

    for(let i = 0; i < props.data.length; i++){
        dataObjects.push({x: i+1, y: (10**16)*props.data[i]})
    }



    const options = {
        theme: "light1",
        animationEnabled: true,
        zoomEnabled: true,
        title: {
            text: "MFCC Features"
        },
        axisX: {
            title: "Feature",
            suffix: "",
            crosshair: {
                enabled: true,
                snapToDataPoint: true
            }
        },
        axisY: {
            title: "Value",
            crosshair: {
                enabled: true,
                snapToDataPoint: true
            }
        },
        data: [{
            type: "scatter",
            markerSize: 15,
            toolTipContent: `Feature: {x} Value: {y}`,
            dataPoints: dataObjects
        }]
    }
    return (
        <div>
            <CanvasJSChart options={options}/>
        </div>
    );
}

export default ScatterPlotCanvas