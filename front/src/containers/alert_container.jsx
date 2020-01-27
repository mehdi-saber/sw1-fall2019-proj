import React, {Fragment, useEffect} from 'react';
import ReactNotification, {store} from 'react-notifications-component';
import 'react-notifications-component/dist/theme.css';
import {useSelector} from "react-redux";

const AlertContainer = () => {

    const {alert} = useSelector(state => state.Utils);

    useEffect(
        () => {
            if (alert)
                store.addNotification({
                    title: alert.title,
                    message: alert.text,
                    type: alert.type,
                    insert: "top",
                    container: "top-right",
                    animationIn: ["animated", "fadeIn"],
                    animationOut: ["animated", "fadeOut"],
                    dismiss: {
                        duration: 5000,
                        onScreen: true
                    }
                });
        }, [alert]
    );

    return (
        <Fragment>
            <ReactNotification/>
        </Fragment>
    );
};

export default AlertContainer;