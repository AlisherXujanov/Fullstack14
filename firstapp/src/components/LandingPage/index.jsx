import Ownership from "./Ownership"
import TrendingArt from "./TrendingArt";
import Collections from "./Collections";
import Leaderboard from "./Leaderboard"
import Explore from "./Explore"
import TryApp from "../common/Try_App"
import "./style.scss";

function LandingPage() {
    return (
        <main className="landing-page-wrapper">
            <Ownership />
            <TrendingArt/>
            <Collections/>
            <Leaderboard />
            <Explore/>
            <TryApp/>
        </main>
    );
}

export default LandingPage;