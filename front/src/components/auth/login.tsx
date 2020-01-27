import React, {Fragment} from 'react';

const Login: React.FunctionComponent<any> = () => {
    return (
        <Fragment>
            <div className="container">
                <div className="jumbotron text-center">
                    <h1>Login</h1>
                    <div className="row mb-2">
                        <label htmlFor="username" className="col-4">username:</label>
                        <div className="col-8">
                            <input type="text" className="form-control" placeholder="username..."/>
                        </div>
                    </div>
                    <div className="row mb-2">
                        <label htmlFor="password" className="col-4">password:</label>
                        <div className="col-8">
                            <input type="password" className="form-control" placeholder="password..."/>
                        </div>
                    </div>
                </div>
            </div>
        </Fragment>
    );
};

export default Login;