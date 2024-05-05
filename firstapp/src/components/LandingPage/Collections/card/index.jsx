import pfp from "../../../../assets/imgs/collections/imo1.png"
import Galochka from "../../../../assets/icons/trendingart/galochka.png"
import Eth from "../../../../assets/icons/trendingart/crypto-sign.png"
import "./style.scss"

function collectionCard(params) {
    return(
        <div className="card-wrapper">
            <img src={params.image} alt="" />
            <div className="card-right">
            <div className="profile">
            <img src={pfp} alt="" />
            <img src={Galochka} alt="" />
            Perperzon
            </div>
            <h1>ExBoot #{params.id}</h1>
            <div className="description">Description</div>
            <div className="We">We would like to present you The Exboot 3D - Watching you~</div>
            <div className="PriceTime">
            <div className="price">
                <div className="Bid">
                    Current Bid
                </div>
                <img src={Eth} alt="" />
                3.421
            </div>
            <div className="time">
            <div className="end">End in</div>
            <div className="time1">1h 13m 14s</div>
            </div>
            </div>
            <button>💸    Place Bid</button>
            </div>
            </div>
    )
}

export default collectionCard