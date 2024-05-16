import './style.scss'
import Searchbar from '../common/Searchbar'

function FAQ() {
    return (
        <div className="faq-wrapper">
            <p className="intro">FAQ</p>
            <h1>Frequently asked questions</h1>
            <p className='subtitle'>Here, you will find answers to the most commonly asked questions about our products, services, and policies.</p>

            <div className='searchbar-wrapper'>
                <Searchbar placeholder="Search your ask" />
            </div>

            <div className="buttons">
                <button className='btn active'>General</button>
                <button className='btn'>NFT Product</button>
                <button className='btn'>Payment</button>
            </div>
        </div>
    );
}

export default FAQ;