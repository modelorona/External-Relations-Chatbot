# External Relations Chatbot

Developed to deal with redundant queries about University of Glasgow short courses.

The chatbot can be accessed live and running [here.](https://anguel.co.uk/)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Prerequisites

Please ensure all dependancies for both client and server are fully installed in order to run the project.

#### Installing client dependancies

```bash
$ npm install
```

#### Installing server dependancies

Make sure to run
```bash
$ pip install -r requirements.txt
```

or if you are not using a virtual environment,
```bash
$ pip3 install -r requirements.txt
```

when in the folder with that file. It is recommended to run the server in a virtual environment.


## Installing

The following commands for running the client and server must be ran simoultaneously in different terminals in order to run the full project.

### Running the client

Simply run

```bash
$ npm run dev
```

### Running the server

The server needs some environmental variables to be set in order to run properly. You can look in [.env.example](server/externalrelations/.env.example)
to see the environmental variables that are currently required. Their values can currently be found in the Wiki. Once you have them, within the same folder
as the example, create a new file called ```.env``` and paste them in there. Be careful not to commit it.

To run the server itself, in the folder where ```manage.py``` exists, run
```bash
$ python manage.py runserver 5000
```

or if you are not using a virtual environment,
```bash
$ python3 manage.py runserver 5000
```

## Testing

### Snapshot and Dialogflow intents tests

These tests have been developed using the Cypress testing framework.

First navigate to the `client` directory

To install cypress run the following command
```bash
$ npm install cypress
```
To run the tests:

```bash
$ npm run cypress:open
```

### Server tests

Within the folder that contains ```manage.py```, run

```bash
$ python manage.py test
```

or if you are not using a virtual environment,
```bash
$ python3 manage.py test
```

## Deployment

### Building

Within the `client` directory

```bash
$ npm run build
```

Will create a `dist` directory containing your compiled code.

Depending on your needs, you might want to do more optimization to the production build.

### Webpack Bundle Analyzer


Run in development

```bash
$ npm run dev:bundleanalyzer
```

Run on the production optimized build

```bash
$ npm run build:bundleanalyzer
```


## Built With

- [DialogFlow](https://dialogflow.com/) - Chatbot
- [Firebase](https://firebase.google.com/) - Communication between client and DialogFlow
- [ReactJS](https://reactjs.org/) - The actual frontend that the user sees
- [React-Simple-Chatbot](https://lucasbassetti.com.br/react-simple-chatbot/) - The client framework
- [Cypress](https://www.cypress.io/) - For testing the frontend
- [ResponsiveVoiceJS](https://responsivevoice.org/api/) - For text to speech capabilities
- [Django](https://www.djangoproject.com/) - For the backend server
- [SendGrid](https://sendgrid.com/) - To send email to the clients
- [AWS](https://aws.amazon.com) - To host the database and server
- [MySQL](https://www.mysql.com/) - The database
- [TypeForm](https://www.typeform.com/) - The feedback form that appears at the end

## Contributors

Please read [Contributors.md](Contributors.md) for our contact details.


## Authors

- **Anguel Hristozov**
- **Justyna Toporkiewicz**
- **Hannah Mehravari**
- **Odysseas Polycarpou**
- **Martin Manov**


## License

MIT

See [LICENSE](LICENCE) for entire license information.

## Acknowledgments

* [Dr. Jeff Dalton](http://www.dcs.gla.ac.uk/~jeff/) - for his incredible help and guidance throughout the entire project lifecycle
* [React Simple Chatbot](https://lucasbassetti.com.br/react-simple-chatbot/) - Base React component used for frontend

