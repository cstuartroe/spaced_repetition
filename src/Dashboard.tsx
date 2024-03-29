import React, { Component } from "react";
import {Link, Navigate} from "react-router-dom";

type Props = {
    is_superuser: boolean,
}

type State = {
}

export default class Dashboard extends Component<Props, State> {
    constructor(props: Props) {
        super(props);
        this.state = {
        };
    }

    componentDidMount() {
        fetch("/api/playing_lemmas")
    }


    render() {
        return (
            <div className="col-12 col-md-6 offset-md-3">
                <div className="row">
                    <div className="col-6">
                        <Link to="/documents">
                            <div className="big button">
                                See documents
                            </div>
                        </Link>
                    </div>
                </div>
            </div>
        );
    }
}
