import React from 'react'
import './Poster.css'
import Door from '../Door/Door'
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Record from '../Record/Record';


function Poster() {
  return (
    <>
    <div className='nav-poster'>Task 3</div>
    <div  className='columns-container'>
      <Row>
        <Col>
        <div className='intro'>intro</div>
        <div className='methods'>methods</div>
        </Col>
        <Col>
        <div className='door-container'>
        <Door/>
        <div className='record'>
        <Record/>
        </div>
        </div>
        <div className='results'>Results</div>
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