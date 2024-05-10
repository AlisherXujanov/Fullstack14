import "./style.scss"
import Searchbar from "../common/Searchbar";
import { context } from '../../state'
import { useContext } from 'react'


function Explore(props) {
    const state = useContext(context)

    function setImage(e) {
        const file = e.target.files[0]
        const reader = new FileReader()
        reader.readAsDataURL(file)
        reader.onload = function () {
            state.dispatch({ type: "changeFileInput", payload: reader.result })
        }
    }

    function activateRadio(e) {
        const text = e.target.getAttribute('data-lock')
        state.dispatch({ type: "changeRadioInput", payload: text })
    }

    return (
        <div className="explore-wrapper">
            <h1>Discover Amazing NFT’s</h1>
            <div className="search-wrapper">
                <Searchbar />
            </div>

            <div className="container">
                <p>{state.input}</p>
                <input id="text" type="text"
                    onChange={(e) => { state.dispatch({ type: "changeInput", payload: e.target.value }) }}
                    value={state.input}
                />

                <p>{state.textarea}</p>
                <textarea
                    onChange={(e) => { state.dispatch({ type: "changeTextarea", payload: e.target.value }) }}
                    value={state.textarea}
                ></textarea>

                <p>Color</p>
                <input id="color" type="color" style={{ height: '50px' }}
                    onChange={(e) => { state.dispatch({ type: "changeColor", payload: e.target.value }) }}
                    value={state.color}
                />
            </div>

            <table>
                <tr>
                    <td>
                        <label htmlFor="range">Range</label>
                        <input id="range" type="range" min={1} max={100}
                            onChange={(e) => { state.dispatch({ type: "changeRangeInput", payload: e.target.value }) }}
                            value={state.rangeInput}
                        />
                    </td>
                    <td>
                        <label htmlFor="date">Date</label>
                        <input id="date" type="date"
                            onChange={(e) => { state.dispatch({ type: "changeDateInput", payload: e.target.value }) }}
                            value={state.dateInput}
                        />
                    </td>
                </tr>
                <tr>
                    <td>
                        <label htmlFor="checkbox">Checkbox</label>
                        <input id="checkbox" type="checkbox"
                            onChange={(e) => { state.dispatch({ type: "changeCheckboxInput", payload: e.target.checked }) }}
                            checked={state.checkboxInput}
                        />
                    </td>
                    <td>
                        <label htmlFor="file">File</label>
                        <input id="file" type="file"
                            onChange={setImage}
                        />
                    </td>
                </tr>
            </table>


            <fieldset>
                <legend>Choose one of these: </legend>

                <b>Lock: </b> <input type="radio" name="locking" data-lock="Lock"
                    onClick={activateRadio}
                />
                <br />
                <b>Unlock: </b> <input type="radio" name="locking" data-lock="Unclock" defaultChecked
                    onClick={activateRadio}
                />
                <br />
                <b>Lorem: </b> <input type="radio" name="locking" data-lock="Lorem"
                    onClick={activateRadio}
                />
                <br />
            </fieldset>
        </div>
    );
}

export default Explore;