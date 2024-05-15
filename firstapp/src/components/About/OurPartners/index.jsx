import Partner1 from "../../../assets/icons/AboutPage/partner1.png"
import Partner2 from "../../../assets/icons/AboutPage/partner2.png"
import Partner3 from "../../../assets/icons/AboutPage/partner3.png"
import Partner4 from "../../../assets/icons/AboutPage/partner4.png"
import Partner5 from "../../../assets/icons/AboutPage/partner5.png"
import Partner6 from "../../../assets/icons/AboutPage/partner6.png"
import Partner7 from "../../../assets/icons/AboutPage/partner7.png"
import Partner8 from "../../../assets/icons/AboutPage/partner8.png"
import Partner9 from "../../../assets/icons/AboutPage/partner9.png"
import Partner10 from "../../../assets/icons/AboutPage/partner10.png"

import "./style.scss"
import "../../../assets/styles/_settings.scss"

function OurPartners() {
    return (
        <>
            <section className="partners">
                <h1>Our Partners</h1>
                <div className="partner">
                    <div>
                        <img src={Partner1} alt="" />
                    </div>
                    <div>
                        <img src={Partner2} alt="" />
                    </div>
                    <div>
                        <img src={Partner3} alt="" />
                    </div>
                    <div>
                        <img src={Partner4} alt="" />
                    </div>
                    <div>
                        <img src={Partner5} alt="" />
                    </div>
                    <div>
                        <img src={Partner6} alt="" />
                    </div>
                    <div>
                        <img src={Partner7} alt="" />
                    </div>
                    <div>
                        <img src={Partner8} alt="" />
                    </div>
                    <div>
                        <img src={Partner9} alt="" />
                    </div>
                    <div>
                        <img src={Partner10} alt="" />
                    </div>
                </div>
            </section>
        </>
    );
}

export default OurPartners;