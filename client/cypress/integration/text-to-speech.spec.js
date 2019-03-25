describe('Text-to-speech is enabled and disabled correctly', function () {
    beforeEach(function () {
       cy.visit('http://localhost:3000');
       cy.get('.rsc-float-button').click();
    });

    it('Bot\'s text-to-speech is initially disabled', function () {
        cy.window().its('ttsOn').should('equal', false);
    });


    it('Bot recognises text-to-speech enabling prompt and acts accordingly', function () {
        cy.get('.rsc-input').type('Enable text-to-speech');
        cy.get('.rsc-submit-button').click();
        cy.window().its('ttsOn').should('equal', true);
    });

    it('Bot recognises text-to-speech disabling prompt and acts accordingly', function () {

        cy.get('.rsc-input').type('Enable text-to-speech');
        cy.get('.rsc-submit-button').click();
        cy.get('.rsc-input').type('Disable text-to-speech');
        cy.get('.rsc-submit-button').click();
        cy.window().its('ttsOn').should('equal', false);

    });

});