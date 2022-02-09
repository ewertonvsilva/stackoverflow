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
