import React from 'react'

function Test3() {

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
    }

    // Once you are done singing your best song, stop and get the mp3.
    const stopRec = () => {
        recorder
        .stop()
        .getMp3().then(([buffer, blob]) => {
            // do what ever you want with buffer and blob
            // Example: Create a mp3 file and play
            const file = new File(buffer, 'tamer.mp3', {
                type: blob.type,
                lastModified: Date.now()
            });

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
            <button onClick={startRec}>Start Recording</button>
            <button onClick={stopRec}>Stop Recorder</button>
        </div>
    )
}

export default Test3