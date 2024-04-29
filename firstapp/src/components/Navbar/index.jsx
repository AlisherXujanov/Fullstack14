// npm run dev


// 1. Revert all changes => Отмена всех изменений
// 2. git pull  =>  Загрузка изменений с удаленного репозитория


import './style.scss'
import Logo from "../common/Logo"
import { Link } from "react-router-dom"
import Searchbar from "../common/Searchbar"


function Navbar() {

    function activateLink(e) {
        let slash = e.target.href.lastIndexOf("/")
        let href = e.target.href.slice(slash)
        console.log(href)
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
                    <Link onClick={activateLink} to="/about">About</Link>
                    <Link onClick={activateLink} to="/explore">Not explore</Link>
                    <Link onClick={activateLink} to="/trending">Trending🔥</Link>
                    <Link onClick={activateLink} to="/FAQ">FAQ</Link>
                </div>
            </nav>
        </header>
    )
}

export default Navbar;