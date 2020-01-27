import {AlertChoices} from "../Choices/AlertChoices";

export default interface AlertDTO{
    type: AlertChoices;
    title: string;
    text: string;
}