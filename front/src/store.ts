import {createStore, applyMiddleware} from "redux";
import {logger} from "redux-logger";
import rootReducer from './reducers';
import {composeWithDevTools} from "redux-devtools-extension";

const initState = {};
const middleware = [logger];

export default createStore(
    rootReducer,
    initState,
    composeWithDevTools(applyMiddleware(...middleware))
)