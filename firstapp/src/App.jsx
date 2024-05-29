import { BrowserRouter } from 'react-router-dom'
import AllComponents from "./components/AllComponents"
import { useReducer } from 'react'
import { initialState, globalReducer, context } from './state'

import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function App() {
  const [state, dispatch] = useReducer(globalReducer, initialState)
  state.dispatch = dispatch

  return (
    <context.Provider value={state}>
      <ToastContainer />
      <BrowserRouter>
        <AllComponents />
      </BrowserRouter>
    </context.Provider>
  )
}

export default App