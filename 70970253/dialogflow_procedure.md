#### Install dependencies:

```
pip3 install google-cloud-dialogflow
```

#### Get code:

```
curl https://raw.githubusercontent.com/googleapis/python-dialogflow/74a54c6fd9d6e03741206ff1e95939123362cab9/samples/snippets/intent_management.py > intent_management.py
```

#### Authenticate *(if you are not using a service acccount)* (open the ulr, copy the code and paste on terminal):

```
gcloud auth application-default login
```

#### Create intent example:
```
python3 intent_management.py --project-id PROJECT_ID create "room.cancellation - yes"  --training-phrases-parts "cancel" "cancellation" --message-texts "Are you sure you want to cancel?" "Cancelled."
```
**Result:**

```
Intent created: name: "projects/project-id-<00000000000>/agent/intents/idufc-nfhf-ncsoonw-cwnb-fakeintentidhere"
display_name: "room.cancellation - yes"
priority: 500000
messages {
  text {
    text: "Are you sure you want to cancel?"
    text: "Cancelled."
  }
}
```

#### Create followup intent function - Edit the create_intent function `intent_management.py` with the following code to use :

**After edit run with this line:**
```
python3 intent_management.py --project-id PROJECT_ID create "room.cancellation - Followup"  --training-phrases-parts "cancel" "cancellation" --message-texts "Are you sure you want to cancel?" "Cancelled."
```


```python
def create_intent(project_id, parent_intent, display_name, training_phrases_parts, message_texts):
    """Create an intent of the given intent type."""
    from google.cloud import dialogflow

    intents_client = dialogflow.IntentsClient()
    
    parent_intent="projects/project-id-<project id data>/agent/intents/792d58b1-30fc-49cd-be2b-<parent intent id>"
    parent = dialogflow.AgentsClient.agent_path(project_id)

    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message],
        parent_followup_intent_name=parent_intent
    )

    
    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    print("Intent created: {}".format(response))
```
