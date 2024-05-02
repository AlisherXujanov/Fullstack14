/* eslint-disable no-unused-vars */
import "./style.scss"
import SearchIcon from '../../../assets/icons/search.png'

function Searchbar(props) {
    return (
        <div className="search-input">
            <div className="left">
                <img src={SearchIcon} alt="Search" />
            </div>
            <div className="right">
                <input type="search" placeholder="Search" />
            </div>
        </div>
    );
}

export default Searchbar;