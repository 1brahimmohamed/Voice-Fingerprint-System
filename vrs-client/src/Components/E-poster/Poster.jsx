import React, {useState} from 'react'
import './Poster.css'
import Door from '../Door/Door'
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Record from '../Record/Record';
import PieChartCanvas from "../PieChart/pie";
import axios from "axios";
import ScatterPlotCanvas from "../PieChart/scatter";
import gif from "../../assets/work flow.gif"
import Plot3D from "../3DPlot";

function Poster() {

    const [speaker, setSpeaker] = useState('');
    const [word, setWord] = useState('');
    const [pieChart, setPieChart] = useState([]);
    const [scatterChart, setScatterChart] = useState([]);

    const makeServerRequest = (formdata) => {

        axios.post('http://127.0.0.1:8000/predictnew', formdata
        ).then((response) => {
            setSpeaker(response.data.speaker)
            setWord(response.data.word)
            setPieChart(response.data.pieChart)
            setScatterChart(response.data.scatterChart)
            console.log(response.data.speaker)
            console.log(response.data.word)
            console.log(response.data.pieChart)
            console.log(response.data.scatterChart)
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
                            <Plot3D/>
                        </div>
                        <div className='methods'><img src={gif}/>
                        </div>
                    </Col>
                    <Col>
                        <div className='record'>
                            <Record speaker={speaker} word={word} recordHandler={makeServerRequest}/>
                        </div>
                        <div className='results'>

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