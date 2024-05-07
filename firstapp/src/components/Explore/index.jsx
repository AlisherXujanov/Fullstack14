import "./style.scss"
import Searchbar from "../common/Searchbar";


function Explore(props) {
    return (
        <div className="explore-wrapper">
            <h1>Discover Amazing NFT’s</h1>
            <div className="search-wrapper">
                <Searchbar />
            </div>
        </div>
    );
}

export default Explore;