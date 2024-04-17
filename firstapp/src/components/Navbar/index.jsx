// npm run dev
import './style.scss'

function Navbar() {
    return (
        <header>
            <nav>
                <div className="left-nav">
                    <a href="#logo">Logo</a>

                    <div className="search-input">
                        <div className="left">🔍</div>
                        <div className="right">
                            <input type="search" placeholder="Search" />
                        </div>
                    </div>
                </div>
                <div className="right-nav">
                    <a href="#explore">Explore</a>
                    <a href="#trending">Trending🔥</a>
                    <a href="#FAQ">FAQ</a>
                </div>
            </nav>
        </header>
    )
}

export default Navbar;