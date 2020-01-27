import React, {Fragment} from 'react';
import {Switch, Route} from 'react-router-dom';
import RegisterRouter from "./registerRouter";

const MainRouter: React.FunctionComponent<any> = () => {
    return (
        <Fragment>
            <Switch>
                <Route path="/auth" component={RegisterRouter}/>
            </Switch>
        </Fragment>
    );
};

export default MainRouter;