import Astronaut from "../../../assets/imgs/about/astronaut.png"
import Rocket from "../../../assets/icons/AboutPage/rocket.png"
import Collection from "../../../assets/icons/AboutPage/collections.png"
import Creators from "../../../assets/icons/AboutPage/creators.png"
import Volurme from "../../../assets/icons/AboutPage/volume.png"

import './style.scss'
import '../../../assets/styles/_settings.scss'
import Collections from "./colections.jsx"

function RepresentNFT() {
    return (
        <section className="represent">
            <div className="represent-NFT">
                <div>
                    <img src={Astronaut} alt="" />
                </div>
                <div>
                    <h1>NFT Represent the future</h1>
                    <p>We believe that NFTs represent the future of digital ownership and are excited to provide our customers with access to this revolutionary new market. Our platform is user-friendly and easy to navigate, making it simple for creators to upload and sell their NFTs and for buyers to discover and purchase unique digital assets.</p>
                </div>
            </div>
            <div className="collections">
                <Collections name={"NFT's"} number={"23.400"} picture={Rocket} />
                <Collections name={"Collections"} number={"8.000"} picture={Collection} />
                <Collections name={"Creators"} number={"3.400"} picture={Creators} />
                <Collections name={"Volurme"} number={"$21B+"} picture={Volurme} />
            </div>
        </section>
    );
}

export default RepresentNFT;