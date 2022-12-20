import React from 'react';
import Plot from 'react-plotly.js';


function Plot3D(props) {
    let myWidth = 500;

    return (
        <Plot
            data={
                [
                    {
                        name: 'Amr',
                        x: props.plot3D.length ? props.plot3D[0][0] : [0],
                        y: props.plot3D.length ? props.plot3D[0][1] : [0],
                        z: props.plot3D.length ? props.plot3D[0][2] : [0],
                        type: 'scatter3d',
                        mode: 'markers',
                        marker: {
                            color: 'red'
                        },
                    },
                    {
                        name: 'Ibrahim',
                        mode: 'markers',
                        type: 'scatter3d',
                        x: props.plot3D.length ? props.plot3D[1][0] : [0],
                        y: props.plot3D.length ? props.plot3D[1][1] : [0],
                        z: props.plot3D.length ? props.plot3D[1][2] : [0],
                        marker: {
                            color: 'blue'
                        },
                    },

                    {
                        name: 'Mariam',
                        mode: 'markers',
                        type: 'scatter3d',
                        x: props.plot3D.length ? props.plot3D[2][0] : [0],
                        y: props.plot3D.length ? props.plot3D[2][1] : [0],
                        z: props.plot3D.length ? props.plot3D[2][2] : [0],
                        marker: {
                            color: 'green'
                        },
                    },
                    {
                        name: "Mo'men",
                        mode: 'markers',
                        type: 'scatter3d',
                        x: props.plot3D.length ? props.plot3D[3][0] : [0],
                        y: props.plot3D.length ? props.plot3D[3][1] : [0],
                        z: props.plot3D.length ? props.plot3D[3][2] : [0],
                        marker: {
                            color: 'yellow'
                        },
                    },
                    {
                        name: 'Prediction',
                        mode: 'markers',
                        type: 'scatter3d',
                        x: props.blackPoint.length ? [props.blackPoint[0]] : [0],
                        y: props.blackPoint.length ? [props.blackPoint[1]] : [0],
                        z: props.blackPoint.length ? [props.blackPoint[2]] : [0],
                        marker: {
                            color: 'black'
                        },
                    },
                ]
            }

            config={
                {
                    displayModeBar: false,
                    displaylogo: false
                }
            }
            layout={
                {
                    width: myWidth,
                    height: myWidth * (2 / 3),
                    margin: {
                        l: 0,
                        r: 0,
                        b: 0,
                        t: 0
                    },
                    scene: {
                        xaxis: {title: 'MFCC 5'},
                        yaxis: {title: 'MFCC 6'},
                        zaxis: {title: 'MFCC 7'}
                    }

                }
            }

        />
    );
}

export default Plot3D
