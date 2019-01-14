
#import print library
import logging

#import apache beam library
import apache_beam as beam
from apache_beam import window

#import pipeline options.
from apache_beam.options.pipeline_options import  PipelineOptions

#Set log level to info
root = logging.getLogger()
root.setLevel(logging.INFO)

#Create a pipeline,
plOps = beam.Pipeline(options=PipelineOptions())


transactions= ( plOps 
                | 'Read from pubsub'  
                  >>  beam.io.ReadFromPubSub(subscription='projects/universal-code-210021/subscriptions/test-subscription')
                | 'Create Window'
                 >> beam.WindowInto(window.FixedWindows(5))
                | 'Counting Lines ' 
                 >> beam.CombineGlobally(beam.combiners.CountCombineFn()).without_defaults()
                )

( transactions | 'Print transactions'
                >> beam.ParDo( lambda(s): logging.info('Transactions in window = %s' ,s))
                )
# Run the pipeline
result = plOps.run()
#  wait until pipeline processing is complete
result.wait_until_finish()
