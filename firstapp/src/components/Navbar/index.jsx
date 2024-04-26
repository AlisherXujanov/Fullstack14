// npm run dev


// 1. Revert all changes => Отмена всех изменений
// 2. git pull  =>  Загрузка изменений с удаленного репозитория


import './style.scss'
import Logo from "../common/Logo"
import { Link } from "react-router-dom"
import Searchbar from "../common/Searchbar"

function Navbar() {
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
                    <Link to="/about">About</Link>
                    <Link to="/explore">Explore</Link>
                    <a href="#trending">Trending🔥</a>
                    <a href="#FAQ">FAQ</a>
                </div>
            </nav>
        </header>
    )
}

export default Navbar;