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
                    onChange={(e) => { state.dispatch({type:"changeInput", payload:e.target.value}) }}
                    value={state.input}
                />

                <p>{state.textarea}</p>
                <textarea
                    onChange={(e) => { state.dispatch({type:"changeTextarea", payload:e.target.value}) }}
                    value={state.textarea}
                ></textarea>
            </div>
        </div>
    );
}

export default Explore;