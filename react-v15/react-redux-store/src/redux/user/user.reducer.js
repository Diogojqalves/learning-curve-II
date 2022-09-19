import { UserActionTypes } from "./user.types";

const INITIAL_STATE = { //default state = null
    currentUser: null
}

const userReducer = (state = INITIAL_STATE, action) => { //default state = null
    switch(action.type) {
        case UserActionTypes.SET_CURRENT_USER: //if action.type =
            return { //create new object
                ...state, //state we want to keep
                currentUser: action.payload //the state we want to change, the user value (payload)
            }
        default:
            return state;
    }
}

export default userReducer;