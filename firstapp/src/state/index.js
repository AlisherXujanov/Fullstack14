import { globalReducer } from './helpers.js'
import { createContext } from 'react'
const context = createContext()

const initialState = {
    searchInput: '',
}


export { initialState, globalReducer, context }