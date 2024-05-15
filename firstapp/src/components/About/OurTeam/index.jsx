import Member1 from "../../../assets/imgs/about/team-member1.png"
import Member2 from "../../../assets/imgs/about/team-member2.png"
import Member3 from "../../../assets/imgs/about/team-member3.png"
import Member4 from "../../../assets/imgs/about/team-member4.png"
import Member5 from "../../../assets/imgs/about/team-member5.png"

import './style.scss'
import '../../../assets/styles/_settings.scss'
import Team from "./team.jsx"

function OurTeam() {
    return (
        <section className="our-team">
            <h1>Our Team</h1>
            <div className="teams">
                <Team name={"Floyd Miles"} position={"Founder"} picture={Member1} />
                <Team name={"Eleanor Pena"} position={"UI UX Designer"} picture={Member2} />
                <Team name={"Kiss Dorka"} position={"UX Architect"} picture={Member3} />
                <Team name={"Nagy Timea"} position={"Project Manager"} picture={Member4} />
                <Team name={"William Loko"} position={"Software Developer"} picture={Member5} />
            </div>
        </section>
    );
}

export default OurTeam;