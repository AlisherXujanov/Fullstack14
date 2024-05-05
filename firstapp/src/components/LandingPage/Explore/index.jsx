import "./style.scss"
import Card from "../../common/Card"
import Card1 from "../../../assets/imgs/explore/card1.png"
import Card2 from "../../../assets/imgs/explore/card2.png"
import Card3 from "../../../assets/imgs/explore/card3.png"
import Card4 from "../../../assets/imgs/explore/card4.png"
import Card5 from "../../../assets/imgs/explore/card5.png"
import Card6 from "../../../assets/imgs/explore/card6.png"
import Card7 from "../../../assets/imgs/explore/card7.png"
import Card8 from "../../../assets/imgs/explore/card8.png"
import Card9 from "../../../assets/imgs/explore/card9.png"
import Card10 from "../../../assets/imgs/explore/card10.png"
import Card11 from "../../../assets/imgs/explore/card11.png"
import Card12 from "../../../assets/imgs/explore/card12.png"
import Person1 from "../../../assets/imgs/leaderboard/imo1.png"
import Person2 from "../../../assets/imgs/leaderboard/imo2.png"
import Person3 from "../../../assets/imgs/leaderboard/imo3.png"
import Person4 from "../../../assets/imgs/leaderboard/imo4.png"

function Explore(props){
    return(
        <div className="explore-wrapper">
            <h1>Explore</h1> 
            <select>
                <option value="1">Recently Added</option>
                <option value="2">Most Liked</option>
                <option value="3">Top Rated</option>
            </select>
            
            <div className="cards">
                <Card img={Card1} name="ExBoot #1" author="Perperzon" profile={Person1}></Card>
                <Card img={Card2} name="ExBoot #1" author="Perperzon" profile={Person1}></Card>
                <Card img={Card3} name="ExBoot #1" author="Perperzon" profile={Person1}></Card>
                <Card img={Card4} name="ExBoot #1" author="Perperzon" profile={Person1}></Card>
                <Card img={Card5} name="ExBoot #1" author="Perperzon" profile={Person1}></Card>
                <Card img={Card6} name="ExBoot #1" author="Perperzon" profile={Person1}></Card>
                <Card img={Card7} name="ExBoot #1" author="Perperzon" profile={Person1}></Card>
                <Card img={Card8} name="ExBoot #1" author="Perperzon" profile={Person1}></Card>
                <Card img={Card9} name="ExBoot #1" author="Perperzon" profile={Person1}></Card>
                <Card img={Card10} name="ExBoot #1" author="Perperzon" profile={Person1}></Card>
                <Card img={Card11} name="ExBoot #1" author="Perperzon" profile={Person1}></Card>
                <Card img={Card12} name="ExBoot #1" author="Perperzon" profile={Person1}></Card>
            </div>
        </div>
    )
}

export default Explore;