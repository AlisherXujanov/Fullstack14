import AboutPic from "../../assets/imgs/Salin2.png"


function AboutCompany(props) {
    return (
        <div className="about-company">
            <div className="left">
                <p className="intro">NFT MARKETPLACE</p>
                <h1>About our Company NFT Distro</h1>
                <p>We are a cutting-edge company focused on the creation, promotion, and sale of non-fungible tokens (NFTs). Our marketplace offers a wide range of NFTs, from digital art and collectibles to gaming items and virtual real estate.</p>
            </div>
            <div className="right">
                <img src={AboutPic} alt="" />
            </div>
        </div>
    );
}

export default AboutCompany;