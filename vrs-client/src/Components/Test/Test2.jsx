import React from 'react'
import { useRecorder } from "react-recorder-voice";
import axios from 'axios'


function Test2() {
  const {
    audioURL,
    audioData, // you can use this for send audio to server
    timer,
    recordingStatus,
    cancleRecording,
    saveRecordedAudio,
    startRecording,
  } = useRecorder();

//   const handleSubmit = () => {
//     const formdata = new FormData()
//     formdata.append('file' , audioData)
//     axios.post('',
//      formdata
//      ).then((response) => {
//         console.log(response)
//      }).catch((err) => {
//         console.log(err)
//      })
//   }
  console.log(audioData)
  

  return (
    <div
      style={{
        display: "flex",
        alignItems: "center",
        marginTop: "50px",
        flexDirection: "column",
      }}
    >
      <div>
        <button onClick={startRecording}>Start</button>
        <button onClick={cancleRecording}>Cancle</button>
        <button onClick={saveRecordedAudio}>Stop and Save</button>
      </div>
      <div>
        <audio controls src={audioURL}></audio>
      </div>
      <h1>{timer}</h1>
    </div>
  );
}

export default Test2;