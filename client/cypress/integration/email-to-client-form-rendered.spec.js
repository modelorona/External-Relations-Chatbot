describe('Email to client form renders correctly', function () {
    beforeEach(function () {
        cy.visit('http://localhost:3000');
        cy.get('.rsc-float-button').click();
    });

    it('When user says \"send email\" a feedback form is presented', function () {

        cy.get('.rsc-input').type('send email');
        cy.get('.rsc-submit-button').click();
        cy.get('.rsc-cs').children().should('have', '.form');

    });


});