import Galochka from "../../../assets/icons/trendingart/galochka.png"
import EtheriumImg from "../../../assets/icons/trendingart/crypto-sign.png"
import "./style.scss"

function Card(props) {
    return (
        <div className="card-wrapper">
            <img src={props.img} alt="" />
            <h3>{props.name}</h3>
            <div className="card-bottom">
            <div className="left">
                <img src={props.profile} alt="" />
                <img src={Galochka} alt="" />
                <div className="left-name">{props.author}</div>
            </div>
            <div className="right">
            <h6 className="right-name">Current Bid</h6>
            <div className="right-price">
                <img src={EtheriumImg} alt="" />
                <p>3,421</p>
            </div>
            </div>
            </div>
        </div>
    )
}

export default Card