import { useState } from 'react'
import './themeSwitcher.scss'


// eslint-disable-next-line no-unused-vars
function ThemeSwitcher() {
    const [theme, setTheme] = useState('light')


    function switcher(e) {
        if (theme === 'light') {
            setTheme('dark')
        } else {
            setTheme('light')
        }
    }


    return (
        <div className={theme}>
            <div className="theme-switcher">
                <span className='icon'>☀️</span>

                <div onClick={switcher} className="switcher" >
                    <input type="checkbox" />
                    <span className='circle'></span>
                </div>

                <span className='icon'>🌙</span>
            </div>
        </div>
    );
}

export default ThemeSwitcher;