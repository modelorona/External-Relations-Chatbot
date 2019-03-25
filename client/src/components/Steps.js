import React from 'react';
import HandleInput from './HandleInputComponent';
import HandleFeedback from './HandleFeedbackComponent';
import HandleEmailToClient from './HandleEmailToClientComponent';

const steps = [
    {
        id: 'start',
        message: 'Hello there! I\'m Gilbert, the UoG external relations chatbot!',
        trigger: '2',
    },
    {
        id: '2',
        message: 'What can I help you with today?',
        trigger: '3',
    },
    {
        id: '3',
        message: 'You can enable text to speech by asking me!',
        trigger: '4'
    },
    {
        id: '4',
        message: 'And if I can\'t answer your query, just ask me to send an email on your behalf to my human colleagues!',
        trigger: 'input'
    },
    {
        id: 'input',
        user: true,
        trigger: 'handleInput',
    },
    {
        id: 'handleInput',
        component: (< HandleInput />),
        trigger: 'input',
        asMessage: true,
        waitAction: true,
    },
    {
        id: 'emailToClient',
        component: (< HandleEmailToClient/>),
        trigger: 'emailConfirm',
        waitAction: true
    },
    {
        id: 'emailConfirm',
        trigger: 'end',
        message: '{previousValue}',
    },
    {
        id: 'feedback',
        component: (< HandleFeedback />),
        trigger: 'end',
        waitAction: true
    },
    {
        id: 'end',
        end: true,
        message: 'Glad we could help! Have a nice day.'
    }
];


export default steps;

