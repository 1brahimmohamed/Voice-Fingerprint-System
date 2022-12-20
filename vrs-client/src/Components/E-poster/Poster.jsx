import React from 'react'
import './Poster.css'
import Door from '../Door/Door'
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
// import Container from 'react-bootstrap/Container';
import Record from '../Record/Record';
import PieChartCanvas from "../PieChart/pie";
import axios from "axios";


let pieData = [25,25,25,25,25]

function makeServerRequest(formdata){

    axios.post('http://127.0.0.1:8000/predictnew', formdata
    ).then((response) => {
        console.log(response.data.speaker)
        console.log(response.data.word)
        console.log(response.data.pieChart)
    }).catch((err) => {
        console.log(err);
    })

}

function Poster() {
    return (
        <>
            <div className='columns-container'>
                <Row>
                    <Col>
                        <div className='intro'>intro

                        </div>
                        <div className='methods'>methods</div>
                    </Col>
                    <Col>
                        <div className='record'><Record recordHandler = {makeServerRequest}/></div>
                        <div className='results'>
                            <PieChartCanvas pieChartValues={pieData}/>
                        </div>
                    </Col>
                    <Col>
                        <div className='data-analysis'>data-analysis</div>
                        <div className='conclusion'>conclusion</div>
                    </Col>
                </Row>
            </div>
        </>
    )
}

export default Poster