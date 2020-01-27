import React, {Fragment} from 'react';
import {FaChevronRight} from "react-icons/all";
import {Link} from "react-router-dom";

const Register: React.FunctionComponent<any> = () => {
    return (
        <div>
            <Fragment>
                <div className="container">
                    <div className="jumbotron text-center">
                        <h1>SignUp</h1>
                        <div className="row">
                            <div className="col-6">
                                <input type="text" className="form-control text-center" placeholder="first-name"/>
                            </div>
                            <div className="col-6">
                                <input type="text" className="form-control text-center" placeholder="last-name"/>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-6">
                                <input type="text" className="form-control text-center" placeholder="username"/>
                            </div>
                            <div className="col-6">
                                <input type="password" className="form-control text-center" placeholder="password"/>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-6">
                                <input type="email" className="form-control text-center" placeholder="email"/>
                            </div>
                            <div className="col-6">
                                <select name="type" id="type" className="form-control text-center">
                                    <option value="">type</option>
                                    <option>student</option>
                                    <option>non-student</option>
                                </select>
                            </div>
                        </div>
                        <div className="row mb-2">
                            <div className="col-12">
                                <textarea className="form-control" placeholder="bio"/>
                            </div>
                        </div>
                    </div>
                    <div className="text-right">
                        <button className="btn btn-outline-primary">SignUp <FaChevronRight/></button>
                    </div>
                    <div className="text-right">
                        <Link to="/auth/login" className="btn btn-link">Already signed up? Login</Link>
                    </div>
                </div>
            </Fragment>
        </div>
    );
};

export default Register;