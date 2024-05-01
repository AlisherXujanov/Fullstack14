/* eslint-disable no-unused-vars */
import Salin5 from "../../assets/imgs/Salin5.jpg"
import "./style.scss"
import AddImage from '../../assets/icons/addImage.png'

function CreateNFT(props) {
    return (
        <div className="nft-form-wrapper">
            <h1>Create new NFT</h1>

            <div className="form">
                <form>
                    <div className="form-control">
                        <label htmlFor="nft-image">Upload your NFT</label>
                        <small>File types supported: JPG, PNG, GIF, SVG, MP4</small>
                        <div className="nft-image-wrapper">
                            <input id="nft-image" type="file" placeholder="Upload or drag here"/>
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

                        <div className="options-wrapper">
                            <div className="option-image">
                                <img src={Salin5} alt="Collection-image" />
                            </div>
                            <select>
                                <option value="1">ExBoot Collection</option>
                                <option value="2">ExBoot Collection 2</option>
                                <option value="3">ExBoot Collection 3</option>
                            </select>
                        </div>
                    </div>
                </form>
                <div className="demonstration">

                </div>
            </div>
        </div>
    );
}

export default CreateNFT;