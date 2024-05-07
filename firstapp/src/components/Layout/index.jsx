import Navbar from '../Navbar'
import Footer from '../Footer'
import { Outlet } from 'react-router-dom'
import './style.scss'

function Layout(props) {
    return (
        <div className='layout'>
            <div className="wave-effect"></div>

            <Navbar />

            <div id='outlet'>
                <Outlet />
            </div>

            <Footer />
        </div>
    );
}

export default Layout;