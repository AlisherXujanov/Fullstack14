import './style.scss'
import Searchbar from '../common/Searchbar'
import Accordion from '../common/Accordion'


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

            <section className='accordions'>
                
                <div className="accordion-placeholder">
                    <Accordion title="What is an NFT marketplace?" 
                        content="An NFT marketplace is a platform that allows users to buy, sell, and trade non-fungible tokens (NFTs). NFTs are unique digital assets that can represent anything from artwork and collectibles to in-game items and virtual real estate."
                    />
                </div>
                <div className="accordion-placeholder">
                    <Accordion title="How does buying an NFT work?"/>
                </div>
                <div className="accordion-placeholder">
                    <Accordion title="What are the benefits of owning an NFT?"/>
                </div>
                <div className="accordion-placeholder">
                    <Accordion title="Are there any risks associated with buying NFTs?"/>
                </div>

                <div className="main">
                    <p className='p-1'></p>


                </div>
            </section>

        </div>
    );
}

export default FAQ;