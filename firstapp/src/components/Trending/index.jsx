/* eslint-disable no-unused-vars */
import './style.scss'
import { useState } from 'react'
import Test from './Test.jsx'

function Trending(props) {
    const [counter, setCounter] = useState(0)

    return (
        <main className='trending-page-wrapper'>
            <h1>Trending</h1>

            <button onClick={(e) => { setCounter(counter - 1) }} className='btn dec'>Decrement</button>
            {counter}
            <button onClick={(e) => { setCounter(counter + 1) }} className='btn inc'>Increment</button>

            <hr />

            <Test />
        </main>
    )
}

export default Trending;