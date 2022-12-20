import React from 'react';
import Plot from 'react-plotly.js';


function Plot3D() {
    let myWidth = 500;

    return (
        <Plot
            data={
                [
                    {
                        x: [4, 2, 3],
                        y: [2, 6, 3],
                        z: [5, 4, 8],
                        type: 'scatter3d',
                        mode: 'markers',
                        marker: {
                            color: 'red'
                        },
                    },
                    {
                        mode: 'markers',
                        type: 'scatter3d',
                        x: [1, 2, 3],
                        y: [2, 5, 3],
                        z: [5, 4, 5],
                        marker: {
                            color: 'blue'
                        },
                    },

                    {
                        mode: 'markers',
                        type: 'scatter3d',
                        x: [1, 2, 3],
                        y: [2, 3, 7],
                        z: [3, 4, 5],
                        marker: {
                            color: 'green'
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
                    }
                }
            }

        />
    );
}

export default Plot3D
