/* eslint-disable no-unused-vars */
import './themeSwitcher.scss'
import { context } from '../../state'
import { useContext } from 'react'

function ThemeSwitcher() {
    const state = useContext(context)

    function switcher(e) {
        state.dispatch({type: 'changeTheme', payload: !state.darkTheme})
    }

    return (
        <div className="theme-switcher">
            <span className='icon'>☀️</span>

            <div onClick={switcher} className="switcher" >
                <input type="checkbox" />
                <span className='circle'></span>
            </div>

            <span className='icon'>🌙</span>
        </div>
    );
}

export default ThemeSwitcher;