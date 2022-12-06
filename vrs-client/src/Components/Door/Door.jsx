import React, { useState } from 'react'
import './Door.css'

function Door() {
    const [openDoor , setOpenDoor] = useState(false)
    const handleClick = () => {
        setOpenDoor(!openDoor)
    }
    return (
            <div className="door">
                <div className="door-front" style={openDoor ? {transform: "rotateY(-140deg)" } : null}>
                    <div className="knob"></div>
                </div>
                <div className="door-back">
                    <div className="rack"></div>
                    <div className="hat"></div>
                    <div className="jacket"></div>
                </div>
                {/* <div className="door-mat"></div> */}
                <button onClick={handleClick}>Click</button>
            </div>
    )
}

export default Door