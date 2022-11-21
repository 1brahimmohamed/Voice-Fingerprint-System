import React from 'react'
import './Door.css'

function Door() {
    return (
            <div className="door">
                <div className="door-front">
                    <div className="knob"></div>
                </div>
                <div className="door-back">
                    <div className="rack"></div>
                    <div className="hat"></div>
                    <div className="jacket"></div>
                </div>
                <div className="door-mat"></div>
            </div>
    )
}

export default Door