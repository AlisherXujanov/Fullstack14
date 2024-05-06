import Card1 from "../../../assets/imgs/collections/Salin2.png"
import Card2 from "../../../assets/imgs/collections/Salin1.png"
import PerPic1 from "../../../assets/imgs/collections/imo1.png"
import Galochka from "../../../assets/icons/trendingart/galochka.png"
import Eth from "../../../assets/icons/trendingart/crypto-sign.png"
import Card from "./card"

import "./style.scss"

function Collections() {
    return (
        <section className="collections-wrapper">
            <Card id="1" image={Card1}></Card>
            <Card id="2" image={Card2}></Card>
        </section>
    );
}

export default Collections;