import Ownership from "../../LandingPage/Ownership"
import Navbar from "../../Navbar"
import VideoPlayer from "../../../assets/icons/AboutPage/video-player.png"

import "./style.scss"

function DistroNFT() {
    return (  
        <>
            <section className="distro-nft">
                <h1 className="distro">NFT Distro</h1>
                <div className="video-player">
                    <Navbar />
                    <Ownership />
                    <img className="player-sign" src={VideoPlayer} alt="" />
                </div>
            </section>
        </>
    );
}

export default DistroNFT;