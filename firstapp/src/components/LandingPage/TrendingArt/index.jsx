import Card1 from "../../../assets/imgs/trendingart/Salin1.png"
import Card2 from "../../../assets/imgs/trendingart/Salin2.png"
import Card3 from "../../../assets/imgs/trendingart/Salin3.png"
import Card4 from "../../../assets/imgs/trendingart/Salin4.png"
import PerPic1 from "../../../assets/imgs/trendingart/imo1.png"
import PerPic2 from "../../../assets/imgs/trendingart/imo2.png"
import Galochka from "../../../assets/icons/trendingart/galochka.png"
import Eth from "../../../assets/icons/trendingart/crypto-sign.png"

import "./style.scss"

function TrendingArt() {
    return (
        <>
            <div className="top-part">
                 <h2>Trending Art 🔥</h2>
                 <p>Discover more</p>
             </div>
             <div className="cards">
                 <div className="card1">
                     <img src={Card1} />
                     <h4>ExBoot #1</h4>
                     <div className="bottom-part">
                         <div>
                             <img className="personPic" src={PerPic1} />
                             <img className="galochka" src={Galochka} />
                             <p>Perperzon</p>
                         </div>
                         <div>
                             <p>Curren Bid</p>
                             <div className="balance">
                                 <img src={Eth} />
                                 <p>3.421</p>
                             </div>
                         </div>
                     </div>
                 </div>

                 <div className="card2">
                     <img src={Card2} />
                     <h4>ExBoot #2</h4>
                     <div className="bottom-part">
                         <div>
                             <img className="personPic" src={PerPic2} />
                             <img className="galochka2" src={Galochka} />
                             <p>Richard</p>
                         </div>
                         <div>
                             <p>Curren Bid</p>
                             <div className="balance">
                                 <img src={Eth} />
                                 <p>3.421</p>
                             </div>
                         </div>
                     </div>
                 </div>

                 <div className="card3">
                     <img src={Card3} />
                     <h4>Future of Polygon X</h4>
                     <div className="bottom-part">
                         <div>
                             <img className="personPic" src={PerPic1} />
                             <img className="galochka3" src={Galochka} />
                             <p>Perperzon</p>
                         </div>
                         <div>
                             <p>Curren Bid</p>
                             <div className="balance">
                                 <img src={Eth} />
                                 <p>3.421</p>
                             </div>
                         </div>
                     </div>
                 </div>
                 <div className="card4">
                     <img src={Card4} />
                     <h4>Blue Wave #2</h4>
                     <div className="bottom-part">
                         <div>
                             <img className="personPic" src={PerPic2} />
                             <img className="galochka4" src={Galochka} />
                             <p>Richard</p>
                         </div>
                         <div>
                             <p>Curren Bid</p>
                             <div className="balance">
                                 <img src={Eth} />
                                 <p>3.421</p>
                             </div>
                         </div>
                     </div>
                 </div>
            </div>
        </>
    );
}

export default TrendingArt;