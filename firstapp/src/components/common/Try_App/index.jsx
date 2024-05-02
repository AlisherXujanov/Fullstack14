import Phone from "../../../assets/imgs/Phone.png"
import Ball from "../../../assets/imgs/Ball2.png"
import download from "../../../assets/imgs/download.png"
import "./style.scss"

function TryApp(params) {
    return(
        <div className="TryApp">
            <img src={Ball} className="ball" alt="Ball" />
            <img src={Phone} className="phone" alt="Phone" />
            <h1 className="text">Try our App Mobile NFT</h1>
            <button><img src={download} alt="mm" />Download Now</button>
        </div>        
    )
}

export default TryApp