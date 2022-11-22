import React from 'react'
import { useReactMediaRecorder } from "react-media-recorder";
import axios from 'axios'


function Record() {
    const { status, startRecording, stopRecording, mediaBlobUrl } =
        useReactMediaRecorder({ audio: true });
    console.log(mediaBlobUrl)
    // const handleSubmit = () => {
    //     const formData = new FormData();
    //     formData.append("file", mediaBlobUrl);
    //     axios.post('http://127.0.0.1:5000/audio_out/',
    //         formData
    //     ).then((response) => {
    //         console.log(response)
    //     }).catch((err) => {
    //         console.log(err)
    //     })
    // }

    return (
        <div>
            <p>{status}</p>
            <button onClick={startRecording}>Start Recording</button>
            <button onClick={stopRecording}>Stop Recording</button>
            {/* <button onClick={handleSubmit}>Stop Recording</button> */}
            <audio src={mediaBlobUrl} controls autoPlay />
        </div>
    )
}

export default Record