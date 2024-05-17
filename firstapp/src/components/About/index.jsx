import "./style.scss"
import AboutCompany from './AboutCompany.jsx'
import RepresentNFT from "./RepresentNFT/index.jsx";
import DistroNFT from "./DistroNFT/index.jsx";
import OurPartners from "./OurPartners/index.jsx"
import OurTeam from "./OurTeam/index.jsx";
import Joining from "./Joining/index.jsx";

function About() {
    return (
        <div className='about-page'>
            <section>
                <AboutCompany />
                <RepresentNFT />
                <DistroNFT />
                <OurPartners />
                <OurTeam/>
                <Joining />
            </section>
        </div>
    );
}

export default About;