function globalReducer(state, action) {
    // action = {type:"changeInput", payload:e.target.value}
    switch (action.type) {
        case 'changeSearchbar':
            return { ...state, searchInput: action.payload }
        case 'changeInput':
            return { ...state, input: action.payload }
        case 'changeTextarea':
            return { ...state, textarea: action.payload }
        case 'changeColor':
            return { ...state, color: action.payload }
        // -----------------------------------------------
        // -----------------------------------------------
        case 'changeRangeInput':
            return { ...state, rangeInput: action.payload }
        case 'changeDateInput':
            return { ...state, dateInput: action.payload }
        case 'changeCheckboxInput':
            console.log(action.payload)
            return { ...state, checkboxInput: action.payload }
        case 'changeFileInput':
            return { ...state, fileInput: action.payload }
            // -----------------------------------------------
            // -----------------------------------------------
        case 'changeRadioInput':
            return { ...state, radioInput: action.payload }
    }
}

export { globalReducer }