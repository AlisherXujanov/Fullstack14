import Navbar from '../Navbar'
import Footer from '../Footer'
import { Outlet } from 'react-router-dom'

// eslint-disable-next-line no-unused-vars
function Layout(props) {
    return (
        <>
            <Navbar />

            <Outlet />

            <Footer />
        </>
    );
}

export default Layout;