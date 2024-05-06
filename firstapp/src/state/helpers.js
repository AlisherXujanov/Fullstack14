function globalReducer(state, action) {
    // {type: "...", payload: "..."}
    switch (action.type) {
        case 'changeSearchbar':
            return { ...state, searchInput: action.payload }
    }
}

export { globalReducer }