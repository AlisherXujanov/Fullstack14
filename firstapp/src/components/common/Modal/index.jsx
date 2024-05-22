import { useContext } from 'react';
import { context } from '../../../state';
import "./style.scss";

function Modal(props) {
    const state = useContext(context)

    return (
        <div id="modal-wrapper"
            style={state.showModal ? { display: 'flex' } : { display: 'none' }}
        >
            <div className="modal-content">
                <p className='close-model'
                    onClick={() => { state.dispatch({ type: 'toggleModal', payload:!state.showModal }) }}
                >&times;</p>
                {props.children}
            </div>
        </div>
    );
}

export default Modal;