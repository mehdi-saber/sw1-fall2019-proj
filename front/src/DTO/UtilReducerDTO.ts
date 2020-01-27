import AlertDTO from "./AlertDTO";

export default interface UtilReducerDTO {
    loader: string[];
    alert: AlertDTO | null;
}