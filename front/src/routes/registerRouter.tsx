import React from 'react';
import {Switch, Route} from 'react-router-dom';
import Login from "../components/auth/login";
import Register from "../components/auth/register";

const RegisterRouter = () => {
    return (
        <Switch>
            <Route path="/auth/login" component={Login}/>
            <Route path="/auth/register" component={Register}/>
        </Switch>
    );
};

export default RegisterRouter;