#import print library
import logging

#import apache beam library
import apache_beam as beam

#import pipeline options.
from apache_beam.options.pipeline_options import  PipelineOptions

#Set log level to info
root = logging.getLogger()
root.setLevel(logging.INFO)

#Create a pipeline
p = beam.Pipeline(options=PipelineOptions())
#Create a PCollections from an in-memory list
lines = (
        p
        | 'Create Sample'
                >> beam.Create(
                        ['training exercise',
                        'simple exercise',
                        'good training'])
       )
#Count words using a pipeline and create a result PCollection
linecount = (
        lines
        | 'Count Lines'
                >> beam.CombineGlobally(beam.combiners.CountCombineFn())
    )
#Print
( linecount
    |  'Printing to log'
        >> beam.ParDo(lambda (c): logging.info('-*-*-*\n\n     Total Lines: %s \n____________________' , c)))
# Run the pipeline
result = p.run()
#  wait until pipeline processing is complete
result.wait_until_finish()
