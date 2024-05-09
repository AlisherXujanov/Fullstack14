import { globalReducer } from './helpers.js'
import { createContext } from 'react'
const context = createContext()

const initialState = {
    searchInput: '',

    input: "",
    textarea: "",
    color: 'black',
    input: "",
    range: 0,
}


export { initialState, globalReducer, context }