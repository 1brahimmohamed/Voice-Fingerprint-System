import React, { useState } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faMicrophone, faCircleStop } from '@fortawesome/free-solid-svg-icons'

function Record() {

    const [record , setRecord] = useState(true)

    const MicRecorder = require('mic-recorder-to-mp3');

    // New instance
    const recorder = new MicRecorder({
        bitRate: 128
    });

    // Start recording. Browser will request permission to use your microphone.
    const startRec = () => {
        recorder.start().then(() => {
            // something else
        }).catch((e) => {
            console.error(e);
        });
        setRecord(!record)
    }

    // Once you are done singing your best song, stop and get the mp3.
    const stopRec = () => {
        setRecord(!record)
        recorder
        .stop()
        .getMp3().then(([buffer, blob]) => {
            // do what ever you want with buffer and blob
            // Example: Create a mp3 file and play
            const file = new File(buffer, 'task3.mp3', {
                type: blob.type,
                lastModified: Date.now()
            });

            console.log(record)
            const player = new Audio(URL.createObjectURL(file));
            player.play();
            console.log(file)
            console.log(player)


        }).catch((e) => {
            alert('We could not retrieve your message');
            console.log(e);
        });
        
    }
    

    return (
        <div>
            { record ?  <FontAwesomeIcon icon={faMicrophone} onClick={startRec} size="lg"/> :
            <FontAwesomeIcon icon={faCircleStop} onClick={stopRec} size="lg"/> 
}
        </div>
    )
}

export default Record