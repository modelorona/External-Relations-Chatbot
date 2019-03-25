import React, {Component} from 'react';
import PropTypes from 'prop-types';
import parse from 'html-react-parser';

class HandleFeedbackComponent extends Component {
    constructor(props) {
        super(props);

        this.triggerNext = this.triggerNext.bind(this);
    }

    triggerNext(value, trigger) {
        this.setState({trigger: true}, () => {
            this.props.triggerNextStep(value ? {value, trigger} : {});
        });
    }


    render() {
        let styles = {
            height: '340px',
            width: '100%'
        };
        return (
            <div className="handlefeedbackcomponent" style={styles}>
                {parse('<iframe id="typeform-full" width="100%" height="100%" frameborder="0" src="https://externalrelations3.typeform.com/to/fAkmQs"></iframe> <script type="text/javascript" src="https://embed.typeform.com/embed.js"></script>')}
            </div>
        );
    }
}

HandleFeedbackComponent.propTypes = {
    steps: PropTypes.object,
    triggerNextStep: PropTypes.func
};

HandleFeedbackComponent.defaultProps = {
    steps: undefined,
    triggerNextStep: undefined,
};

export default HandleFeedbackComponent;