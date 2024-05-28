import { BrowserRouter } from 'react-router-dom'
import AllComponents from "./components/AllComponents"
import { useReducer } from 'react'
import { initialState, globalReducer, context } from './state'

function App() {
  const [state, dispatch] = useReducer(globalReducer, initialState)
  state.dispatch = dispatch

  return (
    <context.Provider value={state}>
      <BrowserRouter>
        <AllComponents />
      </BrowserRouter>
    </context.Provider>
  )
}

export default App