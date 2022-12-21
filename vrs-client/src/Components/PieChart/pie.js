import React, {Component} from 'react';
import CanvasJSReact from './canvasjs.react';
import Door from "../Door/Door";

let CanvasJS = CanvasJSReact.CanvasJS;
let CanvasJSChart = CanvasJSReact.CanvasJSChart;


function PieChartCanvas(props) {

    let pieRenderedData = props.pieChartValues
    const options = {
        animationEnabled: true,
        exportEnabled: false,
        theme: "light1", // "light1", "dark1", "dark2"
        title: {
            text: "Results"
        },
        data: [{
            type: "pie",
            indexLabel: "{label}: {y}%",
            startAngle: -90,
            dataPoints: [
                {y: pieRenderedData.length !== 0 ? pieRenderedData[0] : [0], label: "Amr"},
                {y: pieRenderedData.length !== 0 ? pieRenderedData[1] : [0], label: "Ibrahim"},
                {y: pieRenderedData.length !== 0 ? pieRenderedData[2] : [0], label: "Mariam"},
                {y: pieRenderedData.length !== 0 ? pieRenderedData[3] : [0], label: "Mo'men"},
                {y: pieRenderedData.length !== 0 ? pieRenderedData[4] : [0], label: "Others"},

            ]
        }]
    }


    return (
        <div>
            <CanvasJSChart options={options}/>
        </div>
    )
}

export default PieChartCanvas