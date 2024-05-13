import Card1 from "../../../assets/imgs/trendingart/Salin1.png"
import Card2 from "../../../assets/imgs/trendingart/Salin2.png"
import Card3 from "../../../assets/imgs/trendingart/Salin3.png"
import Card4 from "../../../assets/imgs/trendingart/Salin4.png"
import PerPic1 from "../../../assets/imgs/trendingart/imo1.png"
import PerPic2 from "../../../assets/imgs/trendingart/imo2.png"
import Galochka from "../../../assets/icons/trendingart/galochka.png"
import Eth from "../../../assets/icons/trendingart/crypto-sign.png"
import Card from '../../common/Card'
import "./style.scss"

function TrendingArt() {
    return (
        <div className="trending-art-wrapper">

            <div className="top-part">
                <h2>Trending Art 🔥</h2>
                <p>Discover more</p>
            </div>
            <div className="cards">
                <Card img={Card1} name="ExBoot #1" author="Perperzon" profile={PerPic1}></Card>
                <Card img={Card2} name="ExBoot #2" author="Richard" profile={PerPic2}></Card>
                <Card img={Card3} name="ExBoot #3" author="Perperzon" profile={PerPic1}></Card>
                <Card img={Card4} name="ExBoot #4" author="Richard" profile={PerPic2}></Card>
            </div>
        </div>

    );
}

export default TrendingArt;