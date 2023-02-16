'''
You may also find that running simpler computations might take longer than expected. 
That's because all the optimizations that Spark has under its hood are designed for complicated operations with big data sets. 
That means that for simple or small problems Spark may actually perform worse than some other solutions!
'''
# Verify SparkContext
print(sc)

# Print Spark version
print(sc.version)
'''
RDDs are hard to work with directly
Spark DataFrame abstraction built on top of RDDs in this course
When using RDDs, it's up to the data scientist to figure out the right way to optimize the query, 
but the DataFrame implementation has much of this optimization built in!
'''

'''
To start working with Spark DataFrames, you first have to create a SparkSession object from your SparkContext. 
You can think of the SparkContext as your connection to the cluster and 
the SparkSession as your interface with that connection.
'''
# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession

# Create my_spark
my_spark = SparkSession.builder.getOrCreate()

# Print my_spark
print(my_spark)
'''
Your SparkSession has an attribute called catalog which lists all the data inside the cluster. 
This attribute has a few methods for extracting different pieces of information.
One of the most useful is the .listTables() method, which returns the names of all the tables in your cluster as a list.
'''
