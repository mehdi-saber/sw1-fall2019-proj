import React, {Fragment} from 'react';
import {Spinner} from "react-bootstrap";
import {useSelector} from "react-redux";
import ReducerDTO from "../DTO/ReducerDTO";

const LoaderContainer: React.FunctionComponent<any> = () => {

    const {loader} = useSelector((state: ReducerDTO) => state.Utils);

    return (
        <Fragment>
            {loader.length !== 0 ? (
                <div className="loader-container">
                    <Spinner animation="grow" variant="primary"/>
                </div>
            ) : null}
        </Fragment>
    );
};

export default LoaderContainer;