import React from 'react';
import ChatBot from 'react-simple-chatbot';
import {ThemeProvider} from 'styled-components';
import theme from './Theme';
import steps from './Steps';
import botAvatar from '../assets/icon.png';


class App extends React.Component {

    render() {
        return (
            <div>
                <ThemeProvider theme={theme}>
                    <ChatBot steps={steps} botAvatar={botAvatar} floating={true} headerTitle='Gilbert'
                             hideUserAvatar='true'/>
                </ThemeProvider>
            </div>
        );
    }
}

export default App;
