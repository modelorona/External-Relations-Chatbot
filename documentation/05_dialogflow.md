# Dialogflow

Dialogflow is a Google natural language processing tool which basically takes text from the user and processes it so that it is understood by the computer.

To do that, the text is categorised by subject (Intents) and individual words are treated as labels (Entities). 

### Intents

To help the tool categorise text correctly, each intent has to be given some training phrases - example interactions. The more different training phrases, the more likely it is that the tool will pick up the correct intent.

### Entities

Entities are key word types that the tool can learn and use for categorisation as well as passing on parameters. They have entries which are all the words which fall under that label, each having tags which are all the synonyms to these entries. 

For example: Entity: Animals, Entry: dog - golden retriver, pug

These entities would be picked up in text and placed into a parameter ```Animals``` as value ```dog```

### Results

Intent names along with parameters containing all the possible entities for that intent are placed in a JSON file and can be used in further processing like searching for matching keys in a database.

### Responses

The default responses, which are written directly in the Dialogflow, in appropraie intents, are chosen randomly when an intent is caught. 

To enable creating reponses that match the parameters entered by the user there has to be a webhook which will connect the tool to back-end. This can be enabled at the bottom of each intent page.

Next the URL of the webhook needs to be specified by going to the Fulfillment tab, enabling webhooks there and inputting an active URL. We used ngrok to generate urls for local testing, and then when the chatbot was live, we used an actual domain url.

## Warning

```Remember to save after you make changes on any screen of Dialogflow as there is no automatic saving```

```Make sure that every intent has parameters 'number', 'number1' (unless it's asking for ID or credits), 'Credits' and/or 'Class_code', 'date' and 'date1' (unless it's asking for a date), 'Date_start' and/or 'Date_end'.```
