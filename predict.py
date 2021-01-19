# Databricks notebook source
# MAGIC %md ## Predict Model with UDF

# COMMAND ----------

# MAGIC %md ###Get Name of Model

# COMMAND ----------

dbutils.widgets.text(name = "model_name", defaultValue = "jah-wine-model", label = "Model Name")
dbutils.widgets.text(name = "stage", defaultValue = "staging", label = "Stage")

# COMMAND ----------

model_name = dbutils.widgets.get("model_name")
stage = dbutils.widgets.get("stage")

# COMMAND ----------

# MAGIC %md ### Read data

# COMMAND ----------

df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").option("delimiter", ";").load("/FileStore/tables/winequality_red-42ff5.csv")

# COMMAND ----------

df.columns

# COMMAND ----------

# MAGIC %md ### Predict
# MAGIC 
# MAGIC Let's now register our Keras model as a Spark UDF to apply to rows in parallel.

# COMMAND ----------

# MAGIC %md #### DataFrame UDF

# COMMAND ----------

import pandas as pd
import mlflow.pyfunc

model_uri = "models:/{model_name}/{stage}".format(model_name=model_name, stage=stage)
print("Loading registered model version from URI: '{model_uri}'".format(model_uri=model_uri))
model_udf = mlflow.pyfunc.spark_udf(spark, model_uri)

predictions = df.withColumn("prediction", model_udf('fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'))
display(predictions)

# COMMAND ----------

# MAGIC %md #### SQL UDF

# COMMAND ----------

spark.udf.register("predictUDF", model_udf)
df.createOrReplaceGlobalTempView("data")

# COMMAND ----------

# MAGIC %sql
# MAGIC select *, predictUDF('fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol') as prediction from global_temp.data