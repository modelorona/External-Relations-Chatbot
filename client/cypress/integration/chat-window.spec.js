
describe('Chat window functionality', function () {
    beforeEach(function () {
       cy.visit('http://localhost:3000');
       cy.get('.rsc-float-button').click();
    });

    it('Chat window opens when button is clicked', function () {
        cy.get('.rsc-content').should('be.visible');
    });

    it('Chat window closes when cross is clicked', function () {
        cy.get('.rsc-header-close-button').click();
        cy.get('.rsc-content').should('be.hidden');
    });

    it('Bot says hello when summoned', function () {
        cy.get(':nth-child(1) > .rsc-ts-bubble').contains('Hello there! I\'m Gilbert, the UoG external relations chatbot!');
    });

    it('User is able to send message', function () {
        cy.get('.rsc-input').type('Hello, World!');
        cy.get('.rsc-submit-button').click();
        cy.get('.rsc-ts-user > .rsc-ts-bubble').contains('Hello, World!');
    });

});