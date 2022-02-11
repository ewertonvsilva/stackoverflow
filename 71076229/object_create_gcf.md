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
You have to format the json before use because you have to use `"` insteade of `'`. Use [this site](https://jsonformatter.curiousconcept.com/#)

[![enter image description here][2]][2]

----
Json example:

```json
{
   "bucket":"<bucket name>",
   "contentType":"image/png",
   "crc32c":"a1/tEw==",
   "etag":"9999999999999999/UCEAE=",
   "generation":"9999999999999999",
   "id":"<bucket name>/<file name>",
   "kind":"storage#object",
   "md5Hash":"9999999999999999==",
   "mediaLink":"https://www.googleapis.com/download/storage/v1/b/<bucket name>/o/<file name>?generation=9999999999999999&alt=media",
   "metageneration":"1",
   "name":"Screenshot 2022-02-10 6.09.37 PM.png",
   "selfLink":"https://www.googleapis.com/storage/v1/b/<bucket name>/o/<file name>",
   "size":"452941",
   "storageClass":"STANDARD",
   "timeCreated":"2022-02-11T10:22:01.919Z",
   "timeStorageClassUpdated":"2022-02-11T10:22:01.919Z",
   "updated":"2022-02-11T10:22:01.919Z"
}
```



  [1]: https://i.stack.imgur.com/3nP0M.png
  [2]: https://i.stack.imgur.com/1FBK5.png


