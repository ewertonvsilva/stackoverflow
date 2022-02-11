### User a function to print a event result, so you can have a template of how is the event data:

```python
def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    print(event)
```

### Get the json result in the logs:

[![enter image description here][1]][1]




### Use the tests tab to resend the same json object when you want for test (logs result can take some time)
[![enter image description here][2]][2]

  [1]: https://i.stack.imgur.com/3nP0M.png
  [2]: https://i.stack.imgur.com/1FBK5.png
