import Navbar from '../Navbar'
import Footer from '../Footer'
import { Outlet } from 'react-router-dom'
import './style.scss'
import { context } from '../../state'
import { useContext } from 'react'

function Layout(props) {
    const state = useContext(context)

    return (
        <div className="layout">
            <div className={state.darkTheme ? "wave-effect dark" : "wave-effect"}></div>

            <Navbar />

            <div id='outlet'>
                <Outlet />
            </div>

            <Footer />
        </div>
    );
}

export default Layout;