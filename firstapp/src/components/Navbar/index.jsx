import './style.scss'
import Logo from "../common/Logo"
import { Link } from "react-router-dom"
import Searchbar from "../common/Searchbar"
import { context } from "../../state/index"
import { useContext } from "react"
import { useTranslation } from "react-i18next"

function Navbar() {
    const state = useContext(context)
    const { t, i18n: { changeLanguage, language } } = useTranslation()
    // t                =>   translate
    //     t('key')     =>   translate key
    // changeLanguage   =>   globally change in settings 
    // language         =>   current language


    function activateLink(e) {
        let slash = e.target.href.lastIndexOf("/")
        let href = e.target.href.slice(slash)
        console.log(href)
    }

    const handleChangeLanguage = () => {
        const newLanguage = language === "en" ? "ru" : "en"
        state.dispatch({ type: "changeLanguage", payload: newLanguage })
        changeLanguage(newLanguage)
    }

    return (
        <header>
            <nav>
                <div className="left-nav">
                    <Link to="/">
                        <Logo />
                    </Link>

                    <Searchbar />
                </div>
                <div className="right-nav">
                    <Link onClick={activateLink} to="/create-nft">{t('navbar.create')}</Link>
                    <Link onClick={activateLink} to="/about">{t('navbar.about')}</Link>
                    <Link onClick={activateLink} to="/explore">{t('navbar.explore')}</Link>
                    <Link onClick={activateLink} to="/trending">{t('navbar.trending')}🔥</Link>
                    <Link onClick={activateLink} to="/FAQ">{t('navbar.faq')}</Link>
                    <a href="#" onClick={handleChangeLanguage}>
                        {t('language_name')}
                    </a>
                </div>
            </nav>
        </header>
    )
}

export default Navbar;