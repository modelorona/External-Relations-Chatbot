import React, {Component} from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

class HandleEmailToClientComponent extends Component {
    constructor(props) {
        super(props);

        this.state = {
            query: '',
            email: '',
            name: ''
        };

        this.triggerNext = this.triggerNext.bind(this);
    }

    triggerNext(value, trigger) {
        this.setState({trigger: true}, () => {
            this.props.triggerNextStep(value ? {value, trigger} : {});
        });
    }

    handleFormSubmit(event) {
        event.preventDefault();

        const data = {
            type: 'email',
            email: this.state.email,
            query: this.state.query,
            name: this.state.name
        };

        axios.post('/webhook', data).then(resp => {
            if (resp.data.fulfillmentText === 'Email sent') {
                console.log('email sent');
                this.triggerNext('Email has been sent! Thank you.', 'emailConfirm');
            }
        }).catch(err => {
            console.log(err);
            this.triggerNext('An error occured and I could not send it! Please try again later.', 'emailConfirm')
        })

    }

    handleQueryChange(event) {
        this.setState({query: event.target.value});
    }

    handleEmailChange(event) {
        console.log(event);
        this.setState({email: event.target.value});
    }

    handleNameChange(event) {
        this.setState({name: event.target.value});
    }


    render() {
        return (
            <div className="handleemailtoclientcomponent">
                <form onSubmit={this.handleFormSubmit.bind(this)} className="ui form">
                    <div className="field">
                        <label>
                            Name
                            <input type="text" name="name" required={true} value={this.state.name}
                                   onChange={this.handleNameChange.bind(this)}/>
                        </label>
                    </div>
                    <div className="field">
                        <label>
                            Email
                            <input type="email" name="email" required={true} value={this.state.email}
                                   onChange={this.handleEmailChange.bind(this)}/>
                        </label>
                    </div>
                    <div className="field">
                        <label>
                            Query
                            <textarea value={this.state.query} rows="2" required={true}
                                      onChange={this.handleQueryChange.bind(this)}></textarea>
                        </label>
                    </div>
                    <input className="ui button" type="submit" value="Send email"/>
                </form>
            </div>
        );
    }
}

HandleEmailToClientComponent.propTypes = {
    steps: PropTypes.object,
    triggerNextStep: PropTypes.func
};

HandleEmailToClientComponent.defaultProps = {
    steps: undefined,
    triggerNextStep: undefined,
};

export default HandleEmailToClientComponent;