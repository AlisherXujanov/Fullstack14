import Logo from "../common/Logo"
import ThemeSwitcher from './ThemeSwitcher.jsx'
import "./style.scss"
import { useState } from 'react'

function Footer(props) {
    const [range, setRange] = useState(0);
    const [color, setColor] = useState("");
    const [translate, setTranslate] = useState(0);
    const [font, setFont] = useState({});


    function rangeHandler(event) {
        let fontStyle = {fontSize: "1.5rem", fontWeight: "bold"};

        if (parseInt(range) > parseInt(event.target.value)) {
            setColor("red")
            setFont({})
        } else {
            setColor("green")
            setFont(fontStyle)
        }
        setRange(event.target.value);
        setTranslate(event.target.value);
    }

    return (
        <footer>
            <div className="left">
                <Logo />
                <h1>NFT Distro</h1>
                <small>Experience the Revolutionary World of Non-Fungible Tokens on Our Exclusive NFT Marketplace</small>

                <ThemeSwitcher />

                <p>
                    <span>©️</span>
                    <small>Copyright NFT Distro 2023</small> 
                </p>
            </div>
            <div className="right">
                <p style={{color:color, transform:`translateX(${translate}px)`, ...font}}>{range}</p>
                <input type="range" onChange={rangeHandler} />
            </div>
        </footer>
    );
}

export default Footer;


    