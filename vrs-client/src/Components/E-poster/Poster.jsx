import React, {useState} from 'react'
import './Poster.css'
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Record from '../Record/Record';
import PieChartCanvas from "../PieChart/pie";
import axios from "axios";
import ScatterPlotCanvas from "../ScatterPlot/scatter";
import gif from "../../assets/work flow.gif"
import Plot3D from "../3DPlot/3DPlot";
import deltaImg from "../../assets/outputfinal2.png"

function Poster() {

    const [speaker, setSpeaker] = useState('');
    const [word, setWord] = useState('');
    const [pieChart, setPieChart] = useState([]);
    const [scatterChart, setScatterChart] = useState([]);
    const [plot3D, setPlot3D] = useState([]);
    const [blackPoint, setBlackPoint] = useState([])

    const makeServerRequest = (formdata) => {

        axios.post('http://127.0.0.1:8000/predictnew', formdata
        ).then((response) => {
            setSpeaker(response.data.speaker)
            setWord(response.data.word)
            setPieChart(response.data.pieChart)
            setScatterChart(response.data.scatterChart)
            setPlot3D(response.data.plot3D)
            setBlackPoint(response.data.prePoint)
        }).catch((err) => {
            console.log(err);
        })

    }

    return (
        <>
            <div className='columns-container'>
                <Row>
                    <Col>
                        <div className='intro'>
                            <Plot3D plot3D={plot3D} blackPoint={blackPoint}/>
                        </div>
                        <div className='methods'>
                            <img src={deltaImg} style={{width: '500px'}}/>
                        </div>
                    </Col>
                    <Col>
                        <div className='record'>
                            <Record speaker={speaker} word={word} recordHandler={makeServerRequest}/>
                        </div>
                        <div className='results'>
                            <img className='gif' src={gif} style={{width: '530px', height: '460px', paddingTop: '60px'}}/>
                        </div>
                    </Col>
                    <Col>
                        <div className='data-analysis'>
                            <ScatterPlotCanvas data={scatterChart}/>
                        </div>
                        <div className='conclusion'>
                            <PieChartCanvas pieChartValues={pieChart}/>
                        </div>
                    </Col>
                </Row>
            </div>
        </>
    )
}

export default Poster