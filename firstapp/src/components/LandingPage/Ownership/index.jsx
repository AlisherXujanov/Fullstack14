import Salin from '../../../assets/imgs/Salin1.png'
import Ball1 from '../../../assets/imgs/Ball1.png'
import Ball2 from '../../../assets/imgs/Ball2.png'

import './style.scss'

function Ownership() {
    return (
        <div className="ownership-wrapper">
            <div className="left">
                <small>WEB 3 NON-FUNGIBLE TOKENS</small>
                <h1>Unlock Unique Digital Ownership with NFTs</h1>
                <p>Experience the Revolutionary World of Non-Fungible Tokens on Our Exclusive NFT Marketplace</p>
                <button className="red-btn">
                    <span>💳</span>
                    Connect Wallet
                </button>
            </div>
            <div className="right">
                <div>
                    <img src={Salin} className='Salin' width={"410px"} height={"450px"} />
                    <img src={Ball1} className='ball small' />
                    <img src={Ball2} className='ball big' />
                </div>
            </div>
        </div>
    );
}

export default Ownership;