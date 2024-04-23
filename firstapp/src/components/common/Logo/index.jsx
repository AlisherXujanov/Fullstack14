import Icon1 from "../../../assets/icons/logo1.jpg"
import Icon2 from "../../../assets/icons/logo2.jpg"
import Icon3 from "../../../assets/icons/logo3.jpg"

// JSX  => Java Script XML  
// {}   => Mustache

const imgStyle = {
    width: "25px",
    height: "25px",
    marginLeft: "5px"
}

function Logo() {
    return (
        <>
            <div>
                <img src={Icon1}  style={{...imgStyle, height: '30px', position:"relative", top:"3px"}}/>
                <img src={Icon2}  style={imgStyle}/>
                <img src={Icon3}  style={imgStyle}/>
            </div>
        </>
    );
}

export default Logo;