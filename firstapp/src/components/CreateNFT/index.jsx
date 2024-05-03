/* eslint-disable no-unused-vars */
import Salin5 from "../../assets/imgs/Salin5.jpg"
import Sali from "../../assets/icons/Sali.png"
import "./style.scss"
import AddImage from '../../assets/icons/addImage.png'
import bottomVector from '../../assets/icons/bottom.png'
import { useState } from "react"

function CreateNFT(props) {
    const [option, setOption] = useState("ExBoot Collection")
    const [showOption, setShowOption] = useState(false)
    const [nftImage, setNFTImage] = useState(Salin5)


    function activateOption(e) {
        setOption(e.target.textContent)
    }
    function activateShowOption(e) {
        setShowOption(!showOption)
    }

    function setNFTImageFn(e) {
        const file = e.target.files[0]
        const reader = new FileReader()
        reader.readAsDataURL(file)
        reader.onload = function () {
            setNFTImage(reader.result)
        }
    }


    return (
        <div className="nft-form-wrapper">
            <h1>Create new NFT</h1>

            <div className="form">
                <form>
                    <div className="form-control">
                        <label htmlFor="nft-image">Upload your NFT</label>
                        <small>File types supported: JPG, PNG, GIF, SVG, MP4</small>
                        <div className="nft-image-wrapper">
                            <input id="nft-image" type="file" placeholder="Upload or drag here" onChange={setNFTImageFn} />
                            <img src={AddImage} alt="" />
                            <small>Upload or drag here</small>
                        </div>
                    </div>
                    <div className="form-control">
                        <label htmlFor="name-nft">Name NFT</label>
                        <input id="name-nft" type="text" placeholder="Name NFT" />
                    </div>
                    <div className="form-control">
                        <label htmlFor="description-nft">Description</label>
                        <textarea placeholder="Description"></textarea>
                    </div>
                    <div className="form-control">
                        <label htmlFor="collections">Collections</label>

                        <div className="options-wrapper" onClick={activateShowOption}
                            style={showOption ? { boxShadow: '-2px -2px 16px lightgray' } : { boxShadow: '0 0' }}
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
                                <div onClick={activateOption}>ExBoot Collection 2</div>
                                <div onClick={activateOption}>ExBoot Collection 3</div>
                            </div>
                        </div>
                    </div>
                </form>
                <div className="demonstration">
                    <div className="container">
                        <img src={nftImage} alt="NFT image" />
                    </div>
                </div>
            </div>
        </div>
    );
}

export default CreateNFT;