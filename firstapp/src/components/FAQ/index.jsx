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

            <div className='main-1'>
                <div className="div-p">
                    <p>What is an NFT marketplace? </p>
                    <p className='lefts'>⬇️</p>
                </div>
                <div className="main">
                    <p className='p-1'>An NFT marketplace is a platform that allows users to buy, sell, and trade non-fungible tokens (NFTs). NFTs are unique digital assets that can represent anything from artwork and collectibles to in-game items and virtual real estate.</p>

                    <div className="div-p">
                        <p>How does buying an NFT work?</p>
                        <p className='rights'>➡️</p>
                    </div>
                    <div className="div-p">
                        <p>What are the benefits of owning an NFT?</p>
                        <p className='rights'>➡️</p>
                    </div>
                    <div className="div-p">
                        <p>Are there any risks associated with buying NFTs?</p>
                        <p className='rights'>➡️</p>
                    </div>

                </div>
            </div>

        </div>
    );
}

export default FAQ;