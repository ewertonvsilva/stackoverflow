As mentionated, you can use the AI Platform api to create a job via a `post`.
Following is an example using Java Script and request to trig a job. 
Some usefull tips:

-----

- [Jobs console](https://console.cloud.google.com/ai-platform/jobs?project=ewerton-project) to create a job **manually**, then use the api to list this job then you will have a perfect `json` example of how to trig it. 

- You can use the [`Try this API`](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.jobs/get) tool to get the json output of the manually created job. Use this path to get the job: `projects/<project name>/jobs/<job name>`.

- Get the authorization token using the [OAuth 2.0 Playground](https://developers.google.com/oauthplayground/) for tests purposes (*Step 2 -> Access token:*). Check the docs for a definitive way. 
-----
**Not all parameters are required on the json, thtas jus one example of the job that I have created and got the json using the steps above**.

JS Example:

```js
var request = require('request');

request({
  url: 'https://content-ml.googleapis.com/v1/projects/<project-name>/jobs?alt=json',
  method: 'POST',
  headers: {"authorization": "Bearer ya29.A0AR9999999999999999999999999"},
  json: {
    "jobId": "<job name>",
    "trainingInput": {
      "scaleTier": "CUSTOM",
      "masterType": "standard",
      "workerType": "cloud_tpu",
      "workerCount": "1",
      "args": [
        "--training_data_path=gs://<bucket>/*.jpg",
        "--validation_data_path=gs://<bucket>/*.jpg",
        "--num_classes=2",
        "--max_steps=2",
        "--train_batch_size=64",
        "--num_eval_images=10",
        "--model_type=efficientnet-b0",
        "--label_smoothing=0.1",
        "--weight_decay=0.0001",
        "--warmup_learning_rate=0.0001",
        "--initial_learning_rate=0.0001",
        "--learning_rate_decay_type=cosine",
        "--optimizer_type=momentum",
        "--optimizer_arguments=momentum=0.9"
      ],
      "region": "us-central1",
      "jobDir": "gs://<bucket>",
      "masterConfig": {
        "imageUri": "gcr.io/cloud-ml-algos/image_classification:latest"
      }
    },
    "trainingOutput": {
      "consumedMLUnits": 1.59,
      "isBuiltInAlgorithmJob": true,
      "builtInAlgorithmOutput": {
        "framework": "TENSORFLOW",
        "runtimeVersion": "1.15",
        "pythonVersion": "3.7"
      }
    }
  }
}, function(error, response, body){
  console.log(body);
});
```

Result:

```json
... 
{
 createTime: '2022-02-09T17:36:42Z',
  state: 'QUEUED',
  trainingOutput: {
    isBuiltInAlgorithmJob: true,
    builtInAlgorithmOutput: {
      framework: 'TENSORFLOW',
      runtimeVersion: '1.15',
      pythonVersion: '3.7'
    }
  },
  etag: '999999aaaac='
```
