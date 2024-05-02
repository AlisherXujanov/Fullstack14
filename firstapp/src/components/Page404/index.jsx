import './styles.scss'
import NotFoundImage from '../../assets/404.png'

const Page404 = () => {
    const btnSize = { "width": '150px', "height": '40px' }
    return (
        <div className='page-not-found-wrapper'>
            <div>
                <h1>404 Not Found</h1>
                <p>Home.Pages. <span className='not-found-text'>404 Not Found</span></p>
            </div>
            <img
                src={NotFoundImage} alt="Not Found"
                width={600} height={500}
            />
            <a style={btnSize} className='danger-btn' href="/">
                Back To Home
            </a>
        </div>
    )
};

export default Page404;