import React, {Component} from 'react';
import CanvasJSReact from '../../Packages/CanvasJS/canvasjs.react';
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
                {y: pieRenderedData.length !== 0 ? Math.round(pieRenderedData[0] * 10) / 10 : [0], label: "Amr"},
                {y: pieRenderedData.length !== 0 ? Math.round(pieRenderedData[1] * 10) / 10 : [0], label: "Ibrahim"},
                {y: pieRenderedData.length !== 0 ? Math.round(pieRenderedData[2] * 10) / 10 : [0], label: "Mariam"},
                {y: pieRenderedData.length !== 0 ? Math.round(pieRenderedData[3] * 10) / 10 : [0], label: "Mo'men"},
                {y: pieRenderedData.length !== 0 ? Math.round(pieRenderedData[4] * 10) / 10 : [0], label: "Others"},

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