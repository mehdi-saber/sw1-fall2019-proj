import UtilReducerDTO from "../DTO/UtilReducerDTO";
import ActionDTO from "../DTO/ActionDTO";

export default (
    state: UtilReducerDTO = {
        loader: [],
        alert: null
    },
    action: ActionDTO
) => {
    switch (action.type) {
        case 'loader_set':
            return{
                ...state, loader: [action.payload, ...state.loader]
            };
        case 'loader_remove':
            return {
                ...state, loader: state.loader.filter(item => item !== action.payload)
            };
        case 'alert':
            return {
                ...state, alert: action.payload
            };
        default:
            return state;
    }
}