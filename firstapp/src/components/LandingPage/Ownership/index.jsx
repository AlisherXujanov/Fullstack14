import Salin from '../../../assets/imgs/Salin1.png'
import Ball1 from '../../../assets/imgs/Ball1.png'
import Ball2 from '../../../assets/imgs/Ball2.png'
import './style.scss'
import { context } from '../../../state'
import Modal from '../../common/Modal'
import { useContext } from 'react'


function Ownership() {
    const state = useContext(context)

    return (
        <div className="ownership-wrapper">
            <div className="left">
                <Modal>
                    <h2>Sign with your wallet!</h2>
                    <p>Sign Wallet NFT, the secure digital storage for unique assets, take a step towards the future</p>
                    <button className='red-btn'>Connect Wallet A</button>
                    <button className='purple-btn'>Connect Wallet B</button>
                    <button className='green-btn'>Connect Wallet C</button>
                </Modal>

                <small>WEB {state.dateInput} NON-FUNGIBLE TOKENS</small>
                <h1>{state.radioInput} <span style={{ color: state.color, fontSize: state.rangeInput + 'px' }}>Unique</span> Digital Ownership with NFTs</h1>
                <p>Experience the Revolutionary World of Non-Fungible Tokens on Our Exclusive NFT Marketplace</p>
                <button className="red-btn"
                    style={state.checkboxInput ? { display: "none" } : { display: "flex" }}
                    onClick={() => { state.dispatch({ type: 'toggleModal', payload:!state.showModal }) }}
                >
                    <span>💳</span>
                    Connect Wallet
                </button>
            </div>
            <div className="right">
                <div>
                    <img src={state.fileInput ? state.fileInput : Salin} className='Salin' width={"410px"} height={"450px"} />
                    <img src={Ball1} className='ball small' />
                    <img src={Ball2} className='ball big' />
                </div>
            </div>
        </div>
    );
}

export default Ownership;