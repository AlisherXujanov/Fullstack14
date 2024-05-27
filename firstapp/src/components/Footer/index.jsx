import Logo from "../common/Logo"
import ThemeSwitcher from './ThemeSwitcher.jsx'
import "./style.scss"
import EmailForm from "../common/Email"

function Footer(props) {
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
                <EmailForm />
            </div>
        </footer>
    );
}

export default Footer;


    