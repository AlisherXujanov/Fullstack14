function globalReducer(state, action) {
    // action = {type:"changeInput", payload:e.target.value}
    switch (action.type) {
        case 'changeSearchbar':
            return { ...state, searchInput: action.payload }
        case 'changeInput':
            return { ...state, input: action.payload }
        case 'changeTextarea':
            return { ...state, textarea: action.payload }
    }
}

export { globalReducer }