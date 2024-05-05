import pfp from "../../../../assets/imgs/collections/imo1.png"
import "./style.scss"

function collectionCard(params) {
    return(
        <div className="card-wrapper">
            <img src={params.image} alt="" />
            <div className="card-right">
            <div className="profile">
            <img src={pfp} alt="" />
            Perperzon
            </div>
            <h1>ExBoot #{params.id}</h1>
            </div>
        </div>
    )
}

export default collectionCard