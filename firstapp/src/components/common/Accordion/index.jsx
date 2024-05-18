import "./style.scss"
import { useState } from "react"

function Accordion(props) {
    const [isActive, setIsActive] = useState(false)

    function toggleAccordion() {
        setIsActive(!isActive)
    }

    return (
        <div className="accordion-wrapper">
            <div className="accordion-item">
                <div className="accordion-title" onClick={toggleAccordion}>
                    <p>{props.title}</p>
                    <p className="arrow"
                        style={isActive ? {transform: "rotate(90deg)"} : {transform: "rotate(0deg)"}}
                    >➡️</p>
                </div>
                <div className={ isActive ? "accordion-content-opened" : "accordion-content-closed"}>
                    <p>{props.content}</p>
                </div>
            </div>
        </div>
    );
}

export default Accordion;