import { useState } from 'react'
import './themeSwitcher.scss'



function ThemeSwitcher() {
    const [theme, setTheme] = useState('light')
    const [counter, setCounter] = useState(0)


    function switcher(e) {
        if (theme === 'light') {
            setTheme('dark')
        } else {
            setTheme('light')
        }
    }

    function changeCounter(e) {
        const role = e.target.getAttribute('role')
        if (role == 'inc') {
            setCounter(counter + 1)
        } else if (role == 'dec') {
            setCounter(counter - 1)
        } else {
            console.log("Invalid role")
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


            <div className="container">
                <button onClick={changeCounter} role="dec">Decrement</button>
                <span>{counter}</span>
                <button onClick={changeCounter} role="inc">Increment</button>
            </div>
        </div>
    );
}

export default ThemeSwitcher;