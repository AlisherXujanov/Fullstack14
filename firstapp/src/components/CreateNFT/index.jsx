import Salin5 from "../../assets/imgs/Salin5.jpg"
import Sali from "../../assets/icons/Sali.png"
import AddImage from '../../assets/icons/addImage.png'
import bottomVector from '../../assets/icons/bottom.png'
import AuthDefaultImg from "../../assets/icons/authors/default.png"
import EtheriumImg from "../../assets/icons/trendingart/crypto-sign.png"

import { useState } from "react"
import "./style.scss"

// RULES of Hooks!
// 1. Always import them from "react" at the top of the file
// RU: Всегда импортируйте их из "react" в начале файла
// ---------------------------------------------------------
// 2. Always use them at the top of the function component
// RU: Всегда используйте их в начале функционального компонента
// ---------------------------------------------------------
// 3. Never use them in loops, conditions, or nested functions
// RU: Никогда не используйте их в циклах, условиях или вложенных функциях


function CreateNFT(props) {
    const [showOption, setShowOption] = useState(false)

    const [form, setForm] = useState({
        image: Salin5,
        option: "ExBoot Collection",
        name: "ExBoot",
        description: "",
        price: 0,
        author: "Antonson"
    })

    function updateForm(e) {
        const inputName = e.target.name
        let dataOption = e.target.getAttribute('data-option')

        if (inputName == 'image') {
            const file = e.target.files[0]
            const reader = new FileReader()
            reader.readAsDataURL(file)
            reader.onload = function () {
                setForm({ ...form, [inputName]: reader.result })
            }
        } else if (dataOption == 'option') {
            setForm({ ...form, [dataOption]: e.target.innerText })
        } else {
            setForm({ ...form, [inputName]: e.target.value })
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
                            <input id="nft-image" type="file" placeholder="Upload or drag here"
                                onChange={updateForm} name='image'
                            />
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
                                onChange={updateForm}
                                name='name'
                            />
                        </div>
                        <div>
                            <label htmlFor="cost-nft">Price</label>
                            <input
                                id="cost-nft" type="number"
                                placeholder="Price"
                                onChange={updateForm}
                                name="price"
                            />
                        </div>
                    </div>
                    <div className="form-control">
                        <label htmlFor="description-nft">Description</label>
                        <textarea placeholder="Description"
                            onChange={updateForm}
                            name="description"
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
                                {form.option}
                                <img
                                    style={showOption ? { transform: 'rotate(180deg)' } : { transform: 'rotate(0)' }}
                                    src={bottomVector} alt="vector-image"
                                />
                            </div>
                            <div style={showOption ? { display: 'block' } : { display: 'none' }} className="drp-content">
                                <div onClick={updateForm} data-option='option'>ExBoot Collection</div>
                                <div onClick={updateForm} data-option='option'>Etherium Collection</div>
                                <div onClick={updateForm} data-option='option'>Bitcoin Collection</div>
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
                        <img src={form.image} alt="NFT image" width={"100%"} height={450} />
                    </div>
                    <div className="content">
                        <div className="left">
                            <b>{form.name}</b>
                            <h2 className="author-info">
                                <img src={AuthDefaultImg} alt="Auth Default Img" />
                                {form.author}
                            </h2>
                        </div>
                        <div className="right">
                            <p>Current Bid</p>
                            <div>
                                <img src={EtheriumImg} alt="Etherium Img" />
                                {form.price}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default CreateNFT;