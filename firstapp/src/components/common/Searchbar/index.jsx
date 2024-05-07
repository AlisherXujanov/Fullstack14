import "./style.scss"
import SearchIcon from '../../../assets/icons/search.png'
import { useContext } from 'react'
import { context } from "../../../state"

function Searchbar(props) {
    const state = useContext(context)

    function changeInput(e) {
        state.dispatch({
            type: "changeSearchbar",
            payload: e.target.value
        })
    }

    return (
        <div className="search-input">
            <div className="left">
                <img src={SearchIcon} alt="Search" />
            </div>
            <div className="right">
                <input type="search" placeholder="Search"
                    value={state.searchInput}
                    onChange={changeInput}
                />
            </div>
        </div>
    );
}

export default Searchbar;