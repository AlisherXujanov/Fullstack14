import "./style.scss"
import Card from "../../common/Card"
import Salin1 from "../../../assets/imgs/Salin1.png"
import Person1 from "../../../assets/imgs/leaderboard/imo1.png"
function Explore(props){
    return(
        <div className="explore-wrapper">
            <h1>Explore</h1> 
            <select>
                <option value="1">Recently Added</option>
                <option value="2">Most Liked</option>
                <option value="3">Top Rated</option>
            </select>
            
            <div>
                <Card img={Salin1} name="ExBoot #1" author="Perperzon" profile={Person1}></Card>
            </div>
        </div>
    )
}

export default Explore;