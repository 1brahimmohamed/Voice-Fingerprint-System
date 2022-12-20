import React, {Component} from 'react';
import CanvasJSReact from './canvasjs.react';
import Door from "../Door/Door";

let CanvasJS = CanvasJSReact.CanvasJS;
let CanvasJSChart = CanvasJSReact.CanvasJSChart;


function PieChartCanvas(props) {

    let pieRenderedData = props.pieChartValues

    const options = {
        animationEnabled: true,
        exportEnabled: true,
        theme: "light1", // "light1", "dark1", "dark2"
        title: {
            text: "Results"
        },
        data: [{
            type: "pie",
            indexLabel: "{label}: {y}%",
            startAngle: -90,
            dataPoints: [
                {y: pieRenderedData[0], label: "Amr"},
                {y: pieRenderedData[1], label: "Ibrahim"},
                {y: pieRenderedData[2], label: "Mariam"},
                {y: pieRenderedData[3], label: "Mo'men"},
                {y: pieRenderedData[4], label: "Others"},
            ]
        }]
    }


    return (
        <div>
            <CanvasJSChart options={options}
                /* onRef={ref => this.chart = ref} */
            />
            {/*You can get reference to the chart instance as shown above using onRef. This allows you to access all chart properties and methods*/}
        </div>
    )
}

export default PieChartCanvas