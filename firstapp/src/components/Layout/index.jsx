import Navbar from '../Navbar'
import Footer from '../Footer'
import { Outlet } from 'react-router-dom'
import './style.scss'

// eslint-disable-next-line no-unused-vars
function Layout(props) {
    return (
        <div className='layout'>
            <Navbar />

            <div id='outlet'>
                <Outlet />
            </div>

            <Footer />
        </div>
    );
}

export default Layout;