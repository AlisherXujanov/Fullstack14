/* eslint-disable no-unused-vars */
import "./style.scss"
import Searchbar from "../common/Searchbar";
import { context } from '../../state'
import { useContext, useEffect, useState } from 'react'


const NFTsUrl = "https://jsonplaceholder.typicode.com/photos"

function Explore(props) {
    const state = useContext(context)
    const [NFTs, setNFTs] = useState([])

    // useEffect(callback, dependencies)
    useEffect(() => {
        fetch(NFTsUrl)
            .then(каробка => каробка.json())
            .then(товар => { setNFTs(товар) })
    }, [])


    return (
        <div className="explore-wrapper">
            <h1>Discover Amazing NFT’s</h1>
            <div className="search-wrapper">
                <Searchbar />
            </div>

                <div className="all-nfts">
                    {NFTs.map((nft, index) => {
                        return (
                            <div className="nft-wrapper" key={index}>
                                <h3>{nft.title}</h3>
                                <img src={nft.thumbnailUrl} width={"100%"} height={100} />
                            </div>
                        )
                    })}
                </div>
        </div>
    );
}

export default Explore;