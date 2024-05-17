import AboutPic from "../../assets/imgs/about/pic.png"
import Music from "../../assets/icons/AboutPage/music.png"
import Player from "../../assets/icons/AboutPage/player.png"
import Paint from "../../assets/icons/AboutPage/paint.png"

function AboutCompany(props) {
    return (
        <div className="about-company">
            <div className="left">
                <p className="intro">NFT MARKETPLACE</p>
                <h1>About our Company NFT Distro</h1>
                <p>We are a cutting-edge company focused on the creation, promotion, and sale of non-fungible tokens (NFTs). Our marketplace offers a wide range of NFTs, from digital art and collectibles to gaming items and virtual real estate.</p>
            </div>
            <div className="right">
                <img className="about-pic" src={AboutPic} alt="About picture" />
                <img className="music-pic" src={Music}  />
                <img className="player-pic" src={Player}  />
                <img className="paint-pic" src={Paint}  />
            </div>
        </div>
    );
}

export default AboutCompany;