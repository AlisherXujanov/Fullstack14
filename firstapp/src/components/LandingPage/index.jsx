import Ownership from "./Ownership"
import TrendingArt from "./TrendingArt";
import Collections from "./Collections";
import Leaderboard from "./Leaderboard"


function LandingPage() {
    return (
        <>
            <Ownership />
            <TrendingArt/>
            <Collections/>
            <Leaderboard />
        </>
    );
}

export default LandingPage;