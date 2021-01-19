# Databricks notebook source
# MAGIC %md ### Train, Deploy, Score

# COMMAND ----------

dbutils.widgets.text(name = "model_name", defaultValue = "jah-wine-model", label = "Model Name")
dbutils.widgets.text(name = "stage", defaultValue = "staging", label = "Stage")

# COMMAND ----------

model_name = dbutils.widgets.get("model_name")
stage = dbutils.widgets.get("stage")

# COMMAND ----------

try:
  dbutils.notebook.run("./prep_data", 600)
except Exception as e:
  raise e

# COMMAND ----------

try:
  dbutils.notebook.run("./train_model", 600, {"model_name": model_name, "stage": stage})
except Exception as e:
  raise e

# COMMAND ----------

try:
  dbutils.notebook.run("./deploy", 600, {"model_name": model_name, "stage": stage})
except Exception as e:
  raise e

# COMMAND ----------

try:
  dbutils.notebook.run("./predict", 600, {"model_name": model_name, "stage": stage})
except Exception as e:
  raise e