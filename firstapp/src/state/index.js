import { globalReducer } from './helpers.js'
import { createContext } from 'react'
const context = createContext()

const initialState = {
    searchInput: '',

    input: "",
    textarea: ""
}


export { initialState, globalReducer, context }