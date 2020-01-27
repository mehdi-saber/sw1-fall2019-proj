import axios from 'axios';
import AlertDTO from "../DTO/AlertDTO";
import {AlertChoices} from "../Choices/AlertChoices";

interface Config {
    dispatch: any;
    url: string;
    data: any;
    loader: boolean;
    alert: boolean;
    token: boolean;
    action: string | null;
}

class Service<T> {
    private _response: T | undefined;
    private readonly host = "http://37.152.178.178:8000";

    constructor(private readonly conf: Config) {
    }

    get response() {
        return this._response
    }

    catchData = () => new Promise(
        async (resolve, reject) => {
            const conf: Config = this.conf;
            if (conf.loader) {
                conf.dispatch({
                    type: "loader_set",
                    payload: conf.url
                })
            }
            const data = !!conf.data ? JSON.stringify(conf.data) : undefined;
            let checker: boolean = true;
            while (checker) {
                const config = {
                    headers: {
                        "Content-Type": "application/json",
                        token: localStorage.getItem("access")
                    }
                };
                try {
                    const response = await axios.post(this.host + conf.url, data, config);
                    if (conf.loader) {
                        conf.dispatch({
                            type: "loader_remove",
                            payload: conf.url
                        });
                    }
                    if (conf.action) {
                        conf.dispatch({
                            type: conf.action,
                            payload: response.data
                        })
                    }
                    this._response = response.data;
                    resolve(response.data)
                } catch (e) {
                    if (conf.loader) {
                        conf.dispatch({
                            type: "loader_remove",
                            payload: conf.url
                        });
                    }
                    if (conf.alert) {
                        const alert: AlertDTO = {
                            type: AlertChoices.DANGER,
                            title: "Error!",
                            text: "Something went wrong"
                        };
                        conf.dispatch({
                            type: "alert",
                            payload: alert
                        });
                        resolve(null)
                    } else {
                        reject(e)
                    }
                }
            }
        }
    )
}

export default Service;