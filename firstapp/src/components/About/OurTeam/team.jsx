function Team(props) {
    return (
        <div className="team">
            <img className="picture" src={props.picture} alt="" />
            <div>
                <h3 className="name">{props.name}</h3>
                <p className="position">{props.position}</p>
            </div>
        </div>
    );
}

export default Team;