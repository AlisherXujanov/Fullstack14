import Salin from '../../../assets/imgs/Salin1.png'
import Ball1 from '../../../assets/imgs/Ball1.png'
import Ball2 from '../../../assets/imgs/Ball2.png'
import './style.scss'
import { context } from '../../../state'
import Modal from '../../common/Modal'
import { useContext } from 'react'
import { useTranslation } from "react-i18next";

function Ownership() {
    const state = useContext(context)
    const { t } = useTranslation()

    return (
        <div className="ownership-wrapper">
            <div className="left">
                <Modal>
                    <h2> {t("ownership.h2")} </h2>
                    <p> { t("ownership.subtitle") } </p>
                    <button className='red-btn'>{ t("ownership.connect-w") } A</button>
                    <button className='purple-btn'>{ t("ownership.connect-w") } B</button>
                    <button className='green-btn'>{ t("ownership.connect-w") } C</button>
                </Modal>

                <small> { t("ownership.intro") } {state.dateInput}</small>
                <h1>{ t("ownership.h1") } </h1>
                <p> { t("ownership.paragraph") }</p>
                <button className="red-btn"
                    style={state.checkboxInput ? { display: "none" } : { display: "flex" }}
                    onClick={() => { state.dispatch({ type: 'toggleModal', payload:!state.showModal }) }}
                >
                    <span>💳</span>
                    { t("ownership.connect-w") }
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