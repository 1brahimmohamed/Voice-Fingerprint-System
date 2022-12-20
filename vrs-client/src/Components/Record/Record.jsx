import React, {useState} from 'react'
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import {faMicrophone, faCircleStop} from '@fortawesome/free-solid-svg-icons'
import axios from 'axios'
import './Record.css'
import imgRecording from '../../assets/icons8-audio-wave.gif'

function Record(props) {

    // const [record, setRecord] = useState(true)
    const [recordingStatus, setRecordingStatus] = useState(null);

    const MicRecorder = require('mic-recorder-to-mp3');

    // New instance
    const recorder = new MicRecorder({
        bitRate: 128
    });

    // Start recording. Browser will request permission to use your microphone.
    const startRec = () => {
        setRecordingStatus(true)
        recorder.start().then(() => {
            // something else
        }).catch((e) => {
            console.error(e);
        });

        setTimeout(function () {
            stopRec();
        }, 3000);
        // setRecord(!record)
    }

    // Once you are done singing your best song, stop and get the mp3.
    const stopRec = () => {
        // setRecord(!record)
        setRecordingStatus(false)
        recorder
            .stop()
            .getMp3().then(([buffer, blob]) => {
            // do what ever you want with buffer and blob
            // Example: Create a mp3 file and play
            const file = new File(buffer, 'task3.mp3', {
                type: blob.type,
                lastModified: Date.now()
            });

            const formdata = new FormData()
            formdata.append("file", file)

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
        <>
        <div className='mic-container'>
            <img onClick={startRec} src="https://img.icons8.com/external-filled-outline-icons-pause-08/64/null/external-microphone-phone-filled-outline-icons-pause-08.png"/>
            {recordingStatus ? <div><img className='recording-img' src={imgRecording} alt="" /></div> : <div><img src="https://img.icons8.com/ios-glyphs/30/null/dashed-line.png"/></div>}
        </div>
        </>
    )
}

export default Record