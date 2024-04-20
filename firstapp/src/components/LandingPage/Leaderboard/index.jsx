import Person1 from "../../../assets/imgs/leaderboard/imo1.png"
import Person2 from "../../../assets/imgs/leaderboard/imo2.png"
import Person3 from "../../../assets/imgs/leaderboard/imo3.png"
import Person4 from "../../../assets/imgs/leaderboard/imo4.png"
import Person5 from "../../../assets/imgs/leaderboard/imo5.png"

import User from "./User.jsx"
import "./style.scss"

function Leaderboard() {
    return (
        <section className="leaderboard">
            <h2>Leaderboard of the Week</h2>

            <div className="users">
                <User name={"Perperzon"}  number={1}   balance={9.421}   picture={Person1} />
                <User name={"Richard "}   number={2}   balance={8.421}   picture={Person2} />
                <User name={"Anderson"}   number={3}   balance={7.421}   picture={Person3} />
                <User name={"Michael"}    number={4}   balance={5.421}   picture={Person4} />
                <User name={"Antonson"}   number={5}   balance={3.421}   picture={Person5} />
            </div>
        </section>
    )
}

export default Leaderboard;