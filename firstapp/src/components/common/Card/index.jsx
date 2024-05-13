import Galochka from "../../../assets/icons/trendingart/galochka.png"
import EtheriumImg from "../../../assets/icons/trendingart/crypto-sign.png"
import "./style.scss"
import { context } from '../../../state'
import { useContext } from 'react'


function Card(props) {
    const state = useContext(context)

    return (
        <div className={state.darkTheme ? "card-wrapper-explore dark" : "card-wrapper-explore"}>
            <img src={props.img} alt={props.img} />
            <h3>{props.name}</h3>
            <div className="card-bottom">
                <div className="left">
                    <img src={props.profile} alt={props.profile} />
                    <img src={Galochka} alt={Galochka} />
                    <div className="left-name">{props.author}</div>
                </div>
                <div className="right">
                    <h6 className="right-name">Current Bid</h6>
                    <div className="right-price">
                        <img src={EtheriumImg} alt={EtheriumImg} />
                        <p>3,421</p>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Card