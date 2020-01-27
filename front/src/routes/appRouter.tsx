import React, {Fragment, useEffect} from 'react';
import { Switch } from 'react-router-dom';

const AppRouter: React.FunctionComponent<any> = (props) => {

    const authCheck = () => {
        if(!localStorage.getItem("access")){
            props.history.push("/auth/login")
        }
    };

    useEffect(
        () => {
            authCheck()
        }, []
    );

    return (
        <Fragment>
            <Switch>

            </Switch>
        </Fragment>
    );
};

export default AppRouter;