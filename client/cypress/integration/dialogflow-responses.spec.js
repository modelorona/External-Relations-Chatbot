import firebase from 'firebase/app';
import 'firebase/functions';

const config = {
    apiKey: "AIzaSyC3BzP11sojespxpUlIkmodmt6zTsl0Ouw",
    authDomain: "version2-46721.firebaseapp.com",
    databaseURL: "https://version2-46721.firebaseio.com",
    projectId: "version2-46721",
    storageBucket: "version2-46721.appspot.com",
    messagingSenderId: "861385964505"
};
firebase.initializeApp(config);

let makeQuery = (query) => {
    return new Cypress.Promise((resolve, reject) => {
        let message = firebase.functions().httpsCallable('message');
        message({
            query: query
        }).then((result) => {
            return resolve(result);
        });
    });
}


describe('Dialogflow detects the correct intent fromt the following queries:', function () {
    beforeEach(function () {
        let intent = "";
     });
    it('short courses list', function () {
        cy.wrap(null).then(() => {
            return makeQuery('short courses list').then((response) => {
                expect(response.data.intent).to.equal('Available Courses');
            });
        });
    });

    it('Which course starts on the 17th of January and ends on the 21st of March? What is it\'s ID?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('Which course starts on the 17th of January and ends on the 21st of March? What is it\'s ID?').then((response) => {
                expect(response.data.intent).to.equal('FindClassCode');
            });
        });
    });

    it('How much do you have to pay for Ancient Egypt and the Bible which starts on 17th of January', function () {

        cy.wrap(null).then(() => {
            return makeQuery('How much do you have to pay for Ancient Egypt and the Bible which starts on 17th of January').then((response) => {
                expect(response.data.intent).to.equal('FindCost');
            });
        });
    });

    it('How many credits does class code 9248 provide?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('How many credits does class code 9248 provide?').then((response) => {
                expect(response.data.intent).to.equal('FindCredits');
            });
        });
    });

    it('Description of Ancient Egypt and the Bible', function () {

        cy.wrap(null).then(() => {
            return makeQuery('Description of Ancient Egypt and the Bible').then((response) => {
                expect(response.data.intent).to.equal('FindDescription');
            });
        });
    });


    it('What is the duration of class id 9248 ?', function () {
 
        cy.wrap(null).then(() => {
            return makeQuery('What is the duration of class id 9248 ?').then((response) => {
                expect(response.data.intent).to.equal('FindDuration');
            });
        });
    });


    it('Can you give me the end date for the course Ancient Egypt and the Bible?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('Can you give me the end date for the course Ancient Egypt and the Bible?').then((response) => {
                expect(response.data.intent).to.equal('FindEndDate');
            });
        });
    });

    it('Who is the lecturer for the short course Ancient Egypt and the Bible', function () {

        cy.wrap(null).then(() => {
            return makeQuery('Who is the lecturer for the short course Ancient Egypt and the Bible').then((response) => {
                expect(response.data.intent).to.equal('FindLecturer');
            });
        });
    });


    it('When does the course Ancient Egypt and the Bible start?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('When does the course Ancient Egypt and the Bible start?').then((response) => {
                expect(response.data.intent).to.equal('FindStartDate');
            });
        });
    });


    it('What is the subject area of the course Ancient Egypt and the Bible?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('What is the subject area of the course Ancient Egypt and the Bible?').then((response) => {
                expect(response.data.intent).to.equal('FindSubjectArea');
            });
        });
    });

    it('what is the course with id 9248, start date 17th of January, end date 21st of March, duration 64 days, offering 10 credits and costs 125 pounds', function () {

        cy.wrap(null).then(() => {
            return makeQuery('what is the course with id 9248, start date 17th of January, end date 21st of March, duration 64 days, offering 10 credits and costs 125 pounds').then((response) => {
                expect(response.data.intent).to.equal('FindTitle');
            });
        });
    });


    it('Where is the course Ancient Egypt and the Bible taking place?', function () {

        cy.wrap(null).then(() => {
            return makeQuery('Where is the course Ancient Egypt and the Bible taking place?').then((response) => {
                expect(response.data.intent).to.equal('FindVenue');
            });
        });
    });

    it('subject areas', function () {

        cy.wrap(null).then(() => {
            return makeQuery('subject areas').then((response) => {
                expect(response.data.intent).to.equal('Subject Areas');
            });
        });
    });

    // it('What is the venue of course with ID 2580?', function () {
    //
    //     cy.wrap(null).then(() => {
    //         return makeQuery('What is the venue of course with ID 2580?').then((response) => {
    //             expect(response.data.intent).to.equal('ID -> Venue');
    //         });
    //     });
    // });
    //
    // it('Which courses begin on the twenty fourth of november?', function () {
    //
    //     cy.wrap(null).then(() => {
    //         return makeQuery('Which courses begin on the twenty fourth of november?').then((response) => {
    //             expect(response.data.intent).to.equal('Start date -> Title');
    //         });
    //     });
    // });
    //
    // it('Are there any classes about Archaeology Classical Studies and Egyptology?', function () {
    //
    //     cy.wrap(null).then(() => {
    //         return makeQuery('Are there any classes about Archaeology Classical Studies and Egyptology?').then((response) => {
    //             expect(response.data.intent).to.equal('Subject area -> Title');
    //         });
    //     });
    // });
    //
    // it('What subject areas are there?', function () {
    //
    //     cy.wrap(null).then(() => {
    //         return makeQuery('What subject areas are there?').then((response) => {
    //             expect(response.data.intent).to.equal('Subject Areas');
    //         });
    //     });
    // });
    //
    //
    // it('What is the id of Cleopatra: Queen of Egypt?', function () {
    //
    //     cy.wrap(null).then(() => {
    //         return makeQuery('What is the id of Cleopatra: Queen of Egypt?').then((response) => {
    //             expect(response.data.intent).to.equal('Title -> Class Code');
    //         });
    //     });
    // });
    //
    //
    // it('Give me the Cleopatra: Queen of Egypt cost', function () {
    //
    //     cy.wrap(null).then(() => {
    //         return makeQuery('Give me the Cleopatra: Queen of Egypt cost').then((response) => {
    //             expect(response.data.intent).to.equal('Title -> Cost');
    //         });
    //     });
    // });
    //
    //
    //
    // it('I\'d like to know how many credits does Cleopatra: Queen of Egypt gives', function () {
    //
    //     cy.wrap(null).then(() => {
    //         return makeQuery('I\'d like to know how many credits does Cleopatra: Queen of Egypt gives').then((response) => {
    //             expect(response.data.intent).to.equal('Title -> Credits');
    //         });
    //     });
    // });
    //
    //
    // it('What is Cleopatra: Queen of Egypt\'s description?', function () {
    //
    //     cy.wrap(null).then(() => {
    //         return makeQuery('What is Cleopatra: Queen of Egypt\'s description?').then((response) => {
    //             expect(response.data.intent).to.equal('Title -> Description');
    //         });
    //     });
    // });
    //
    // it('What is the length of Cleopatra: Queen of Egypt?', function () {
    //
    //     cy.wrap(null).then(() => {
    //         return makeQuery('What is the length of Cleopatra: Queen of Egypt?').then((response) => {
    //             expect(response.data.intent).to.equal('Title -> Duration');
    //         });
    //     });
    // });
    //
    //
    // it('What is the end date of Cleopatra: Queen of Egypt?', function () {
    //
    //     cy.wrap(null).then(() => {
    //         return makeQuery('What is the end date of Cleopatra: Queen of Egypt?').then((response) => {
    //             expect(response.data.intent).to.equal('Title -> End Date');
    //         });
    //     });
    // });
    //
    // it('What is the start date of Cleopatra: Queen of Egypt?', function () {
    //
    //     cy.wrap(null).then(() => {
    //         return makeQuery('What is the start date of Cleopatra: Queen of Egypt?').then((response) => {
    //             expect(response.data.intent).to.equal('Title -> Start Date');
    //         });
    //     });
    // });
    //
    // it('Can you tell me the subject area of Cleopatra: Queen of Egypt?', function () {
    //
    //     cy.wrap(null).then(() => {
    //         return makeQuery('Can you tell me the subject area of Cleopatra: Queen of Egypt?').then((response) => {
    //             expect(response.data.intent).to.equal('Title -> Subject Area');
    //         });
    //     });
    // });
    //
    // it('Who teaches Cleopatra: Queen of Egypt', function () {
    //
    //     cy.wrap(null).then(() => {
    //         return makeQuery('Who teaches Cleopatra: Queen of Egypt').then((response) => {
    //             expect(response.data.intent).to.equal('Title -> Tutor');
    //         });
    //     });
    // });
    //
    // it('What is the venue for Cleopatra: Queen of Egypt?', function () {
    //
    //     cy.wrap(null).then(() => {
    //         return makeQuery('What is the venue for Cleopatra: Queen of Egypt?').then((response) => {
    //             expect(response.data.intent).to.equal('Title -> Venue');
    //         });
    //     });
    // });
    //
    // it('What are the courses taught by Jane Draycott?', function () {
    //
    //     cy.wrap(null).then(() => {
    //         return makeQuery('What are the courses taught by Jane Draycott?').then((response) => {
    //             expect(response.data.intent).to.equal('Tutor -> Title');
    //         });
    //     });
    // });
    //
    //
    // it('What are the courses in the main building?', function () {
    //
    //     cy.wrap(null).then(() => {
    //         return makeQuery('What are the courses in the main building').then((response) => {
    //             expect(response.data.intent).to.equal('Venue -> Title');
    //         });
    //     });
    // });








    

    

    
});