
import json
import joblib
import numpy as np
import pandas as pd
from azureml.core.model import Model
from datetime import date, timedelta

def init():
  global model
  model_path = Model.get_model_path('model')
  model = joblib.load(model_path)

def prepare_data(df:pd.DataFrame) -> pd.DataFrame:
    df = df[['FirstName', 'ModifiedDate']].sort_values(by='ModifiedDate')
    df['FirstNameLen'] = df['FirstName'].str.len()
    df["ModifiedDate"] = pd.to_datetime(df["ModifiedDate"]) - pd.to_datetime(df["ModifiedDate"]).min()
    df["ModifiedDate"] = df["ModifiedDate"].dt.days
    
    return df[['FirstNameLen', 'ModifiedDate']].reset_index(drop=True)

def int_to_date(day_int: int, start_date: date = date(2005, 7, 1)) -> date:
    
    result=start_date + timedelta(days=day_int)
    result = result.strftime("%Y-%m-%d")
    return result

def run(raw_data):
  try: ## Try la predicción.
    data = json.loads(raw_data)['data'][0]
    data = pd.DataFrame(data)

    data = prepare_data(data)

    columns_model = ["FirstNameLen"]

    data_dummies = data[columns_model]

    result = model.predict(data_dummies).tolist()

    for i in range(len(result)):
      result[i] = int_to_date(result[i])
   

    return json.dumps(result)
  except Exception as e:
    return json.dumps(str(e))
