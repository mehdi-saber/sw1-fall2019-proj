import React, {Fragment} from 'react';
import "bootstrap/dist/css/bootstrap.min.css";
import "./styles/main.css";
import LoaderContainer from "./containers/loader_container";
import AlertContainer from "./containers/alert_container";
import "animate.css";
import {BrowserRouter} from "react-router-dom";
import MainRouter from "./routes/mainRouter";

const App = () => {

    return (
        <Fragment>
            <LoaderContainer/>
            <AlertContainer/>
            <BrowserRouter>
                <MainRouter/>
            </BrowserRouter>
        </Fragment>
    );
};

export default App;