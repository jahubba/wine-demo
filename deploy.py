# Databricks notebook source
# MAGIC %md ### Deploy latest mlFlow registry Model to Azure ML

# COMMAND ----------

# MAGIC %md ###Get Name of Model

# COMMAND ----------

dbutils.widgets.text(name = "model_name", defaultValue = "jah-wine-model", label = "Model Name")
dbutils.widgets.text(name = "model_version", defaultValue = "2", label = "Model Version")
dbutils.widgets.text(name = "stage", defaultValue = "staging", label = "Stage")

# COMMAND ----------

model_name = dbutils.widgets.get("model_name")
model_version = dbutils.widgets.get("model_version")
stage = dbutils.widgets.get("stage")

# COMMAND ----------

# MAGIC %md ### Get the latest version of the model that was put into the current stage

# COMMAND ----------

import mlflow
import mlflow.sklearn

client = mlflow.tracking.MlflowClient()
#latest_model = client.get_latest_versions(name = model_name, stages=[stage])[0]
latest_model = client.get_model_version(name = model_name, version = model_version)
#print(latest_model[0])

# COMMAND ----------

model_uri="runs:/{}/model".format(latest_model.run_id)
latest_sk_model = mlflow.sklearn.load_model(model_uri)

# COMMAND ----------

from mlflow.tracking.client import MlflowClient

client = MlflowClient()
client.update_registered_model(
  name=model_name,
  description="This model forecasts the wine quality based on the characteristics."
)

client.update_model_version(
  name=model_name,
  version=model_version,
  description="This model version was built using sklearn."
)

# COMMAND ----------

client.transition_model_version_stage(
  name=model_name,
  version=model_version,
  stage=stage,
  archive_existing_versions=True
)

model_version_details = client.get_model_version(
  name=model_name,
  version=model_version,
)
print("The current model stage is: '{stage}'".format(stage=model_version_details.current_stage))

latest_version_info = client.get_latest_versions(model_name, stages=[stage])
latest_production_version = latest_version_info[0].version
print("The latest production version of the model '%s' is '%s'." % (model_name, latest_production_version))

# COMMAND ----------

dbutils.notebook.exit()