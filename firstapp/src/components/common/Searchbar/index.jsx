/* eslint-disable no-unused-vars */
import "./style.scss"

function Searchbar(props) {
    return (
        <div className="search-input">
            <div className="left">🔍</div>
            <div className="right">
                <input type="search" placeholder="Search" />
            </div>
        </div>
    );
}

export default Searchbar;