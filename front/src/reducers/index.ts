import {combineReducers} from "redux";
import ReducerDTO from "../DTO/ReducerDTO";
import Utils from './utils_reducer';

export default combineReducers<ReducerDTO>({
    Utils
});