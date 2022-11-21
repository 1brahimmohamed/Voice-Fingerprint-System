import React from 'react'
import { useReactMediaRecorder } from "react-media-recorder";


function Record() {
    const { status, startRecording, stopRecording, mediaBlobUrl } =
    useReactMediaRecorder({ audio: true });
    console.log(mediaBlobUrl)
  return (
    <div>
    <p>{status}</p>
    <button onClick={startRecording}>Start Recording</button>
    <button onClick={stopRecording}>Stop Recording</button>
    <audio src={mediaBlobUrl} controls autoPlay />
  </div>
  )
}

export default Record