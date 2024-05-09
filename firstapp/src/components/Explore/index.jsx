import "./style.scss"
import Searchbar from "../common/Searchbar";
import { context } from '../../state'
import { useContext } from 'react'


function Explore(props) {
    const state = useContext(context)

    return (
        <div className="explore-wrapper">
            <h1>Discover Amazing NFT’s</h1>
            <div className="search-wrapper">
                <Searchbar />
            </div>

            <div className="container">
                <p>{state.input}</p>
                <input type="text"
                    onChange={(e) => { state.dispatch({ type: "changeInput", payload: e.target.value }) }}
                    value={state.input}
                />

                <p>{state.textarea}</p>
                <textarea
                    onChange={(e) => { state.dispatch({ type: "changeTextarea", payload: e.target.value }) }}
                    value={state.textarea}
                ></textarea>

                <p>Color</p>
                <input type="color" style={{ height: '50px' }}
                    onChange={(e) => { state.dispatch({ type: "changeColor", payload: e.target.value }) }}
                    value={state.color}
                />
                <input type="text" style={{ height: '50px' }}
                onChange={(e) => { state.dispatch({ type: "changeInput", payload: e.target.value }) }}
                value={state.input} />
                <label htmlFor="range">{state.range}</label>
                <input id="range" type="range"  style={{ height: '50px' }} 
                onChange={(e) => { state.dispatch({ type: "changeRange", payload: e.target.value }) }}
                value={state.range}/>
                <input type="number" style={{ height: '50px' }}
                onChange={(e) => { state.dispatch({ type: "changeNumber", payload: e.target.value })}}
                value={state.input}/>
            </div>
        </div>
    );
}

export default Explore;