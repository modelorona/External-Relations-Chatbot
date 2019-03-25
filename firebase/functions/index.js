const functions = require('firebase-functions');
const admin = require('firebase-admin');
const dialogflow = require('dialogflow');

admin.initializeApp({
    credential: admin.credential.applicationDefault()
});

admin.firestore().settings({
    timestampsInSnapshots: true
});

const projectId = 'version2-46721';
const sessionId = 'version-2-session';
const languageCode = 'en-US';
const sessionClient = new dialogflow.SessionsClient();
const sessionPath = sessionClient.sessionPath(projectId, sessionId);

exports.message = functions.https.onCall((data, context) => {
    let query = data.query;

    let request = {
        session: sessionPath,
        queryInput: {
            text: {
                text: query,
                languageCode: languageCode
            }
        }
    };

    return sessionClient.detectIntent(request).then(responses => {
        console.log('Detected Intent');
        const result = responses[0].queryResult;
        console.log(result.action);

        const intent = result.intent;
        const action = result.action;
        const intentName = intent.displayName;

        const text = result.fulfillmentText;
        let status = 500; // 500 is an error

        // const smallTalkHello = ['smalltalk.greetings.goodevening', 'smalltalk.greetings.goodmorning', 'input.welcome', 'smalltalk.greetings.how_are_you', 'smalltalk.greetings.nice_to_meet_you', 'smalltalk.greetings.nice_to_talk_to_you', 'smalltalk.greetings.whatsup'];
        const smallTalkBye = ['smalltalk.greetings.goodnight', 'smalltalk.greetings.bye'];

        if (smallTalkBye.indexOf(action) > -1) {
            // we need this to be able to know when we are done talking
            status = 300;
        } else if (smallTalkBye.indexOf(action) === -1 && action.startsWith('smalltalk')) {
            status = 200;
        } else if (intent) {
            // here we actually match an intent
            if (text.length !== 0) {
                status = 200;
            }
            if (intentName === 'Text-To-Speech ON') {
                status = 600;
            } else if (intentName === 'Text-To-Speech OFF') {
                status = 700;
            } else if (intentName === 'Send email to client') {
                status = 800;
            }

        }

        return {resp:text, status: status, intent: intentName};

    });

});
