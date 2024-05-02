import Ownership from "./Ownership"
import Leaderboard from "./Leaderboard"
import TryApp from "../common/Try_App"

function LandingPage() {
    return (
        <>
            <Ownership />   
            <Leaderboard />
            <TryApp/>
        </>
    );
}

export default LandingPage;