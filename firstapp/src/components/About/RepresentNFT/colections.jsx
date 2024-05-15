function Collections(props) {
    return (
        <div className="collection">
            <img className="picture" src={props.picture} alt="" />
            <div>
                <h3 className="number">{props.number}</h3>
                <p className="name">{props.name}</p>
            </div>
        </div>
    );
}

export default Collections;