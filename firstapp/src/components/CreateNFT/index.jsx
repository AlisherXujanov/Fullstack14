/* eslint-disable no-unused-vars */
import Salin5 from "../../assets/imgs/Salin5.jpg"
import Sali from "../../assets/icons/Sali.png"
import AddImage from '../../assets/icons/addImage.png'
import bottomVector from '../../assets/icons/bottom.png'
import AuthDefaultImg from "../../assets/icons/authors/default.png"
import EtheriumImg from "../../assets/icons/trendingart/crypto-sign.png"

import { useState } from "react"
import "./style.scss"

function CreateNFT(props) {
    const [showOption, setShowOption] = useState(false)

    const [nftImage, setNFTImage] = useState(Salin5)
    const [option, setOption] = useState("ExBoot Collection")
    const [name, setName] = useState("ExBoot")
    const [description, setDescription] = useState("")
    const [price, setPrice] = useState(0)
    const [author, setAuthor] = useState("Antonson")


    function activateOption(e) {
        setOption(e.target.textContent)
    }

    function setNFTImageFn(e) {
        const file = e.target.files[0]
        const reader = new FileReader()
        reader.readAsDataURL(file)
        reader.onload = function () {
            setNFTImage(reader.result)
        }
    }
    function submit(e) {
        e.preventDefault()
        console.log("Submitted")
    }


    return (
        <div className="nft-form-wrapper">
            <h1>Create new NFT</h1>

            <div className="form">
                <form onSubmit={submit}>
                    <div className="form-control">
                        <label htmlFor="nft-image">Upload your NFT</label>
                        <small>File types supported: JPG, PNG, GIF, SVG, MP4</small>
                        <div className="nft-image-wrapper">
                            <input id="nft-image" type="file" placeholder="Upload or drag here" onChange={setNFTImageFn} />
                            <img src={AddImage} alt="" />
                            <small>Upload or drag here</small>
                        </div>
                    </div>
                    <div className="form-control name-and-cost">
                        <div>
                            <label htmlFor="name-nft">Name NFT</label>
                            <input
                                id="name-nft" type="text"
                                placeholder="Name NFT"
                                onChange={(e) => { setName(e.target.value) }}
                            />
                        </div>
                        <div>
                            <label htmlFor="cost-nft">Price</label>
                            <input
                                id="cost-nft" type="number" 
                                placeholder="Price"
                                onChange={(e) => { setPrice(e.target.value) }}
                            />
                        </div>
                    </div>
                    <div className="form-control">
                        <label htmlFor="description-nft">Description</label>
                        <textarea placeholder="Description"
                            onChange={(e) => { setDescription(e.target.value) }}
                        ></textarea>
                    </div>
                    <div className="form-control">
                        <label htmlFor="collections">Collections</label>

                        <div className="options-wrapper" 
                            style={showOption ? { boxShadow: '-2px -2px 16px lightgray' } : { boxShadow: '0 0' }}
                            onClick={(e) => { setShowOption(!showOption) }}
                        >
                            <div className="option-image">
                                <img src={Sali} alt="Collection-image" />
                            </div>
                            <div className="option-value">
                                {option}
                                <img
                                    style={showOption ? { transform: 'rotate(180deg)' } : { transform: 'rotate(0)' }}
                                    src={bottomVector} alt="vector-image"
                                />
                            </div>
                            <div style={showOption ? { display: 'block' } : { display: 'none' }} className="drp-content">
                                <div onClick={activateOption}>ExBoot Collection</div>
                                <div onClick={activateOption}>Etherium Collection</div>
                                <div onClick={activateOption}>Bitcoin Collection</div>
                            </div>
                        </div>
                    </div>
                    <div className="form-control">
                        <button type="submit" className="red-btn">
                            Create
                        </button>
                    </div>
                </form>
                <div className="demonstration">
                    <h2>Preview</h2>
                    <div className="container">
                        <img src={nftImage} alt="NFT image" width={"100%"} height={450} />
                    </div>
                    <div className="content">
                        <div className="left">
                            <b>{name}</b>
                            <h2 className="author-info">
                                <img src={AuthDefaultImg} alt="Auth Default Img" />
                                {author}
                            </h2>
                        </div>
                        <div className="right">
                            <p>Current Bid</p>
                            <div>
                                <img src={EtheriumImg} alt="Etherium Img" />
                                {price}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default CreateNFT;