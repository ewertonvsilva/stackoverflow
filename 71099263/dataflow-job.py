import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import os
from datetime import datetime
import pytz

tz = pytz.timezone('US/Pacific')
tstmp = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

bucket_path = "gs://<bucket>"
input_file = f'{bucket_path}/inputFile.txt'
output = f'{bucket_path}/output_{tstmp}.txt'


p = beam.Pipeline(options=PipelineOptions())

( p | 'Read from a File' >> beam.io.ReadFromText(input_file, skip_header_lines=1)
    | beam.Map(lambda x:x.split(","))
     | beam.Map(lambda x:f'{x[0]},{x[1]}{x[2]}{x[3]},{x[4]}')
     | beam.io.WriteToText(output) )

p.run().wait_until_finish()
