describe('Email to client form gets a proper response', function () {
    beforeEach(function () {
        cy.visit('http://localhost:3000');
        cy.get('.rsc-float-button').click();
    });

    it('When user submits name, email, and query, the form sends an email and gets a response', function () {
        cy.get('.rsc-input').type('send email');
        cy.get('.rsc-submit-button').click();
        cy.get('.rsc-cs').children().should('have', '.form');
        cy.get(':nth-child(1) > label > input').type('Cypress Test User');
        cy.get(':nth-child(2) > label > input').type('CypressTestUser@gmail.com');
        cy.get('textarea').type('Cypress Test Works');
        cy.get('.form > .ui').click();
        cy.get(':nth-child(8) > .rsc-ts-bubble').contains('Email has been sent! Thank you.');
    });


});