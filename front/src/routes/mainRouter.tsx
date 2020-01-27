import React, {Fragment} from 'react';
import {Switch, Route} from 'react-router-dom';
import RegisterRouter from "./registerRouter";
import AppRouter from "./appRouter";

const MainRouter: React.FunctionComponent<any> = (props) => {

    return (
        <Fragment>
            <Switch>
                <Route path="/auth" component={RegisterRouter}/>
                <Route path="/" component={AppRouter}/>
            </Switch>
        </Fragment>
    );
};

export default MainRouter;