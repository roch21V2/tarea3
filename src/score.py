import json
import typing as t
from datetime import date, timedelta

import joblib
import pandas as pd
from azureml.core.model import Model


def init():
    """
    This function is called when initializing the serving endpint.
    """

    global model
    model_path = Model.get_model_path("model")
    model = joblib.load(model_path)


def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepares the data for prediction.

    Args:
        df (pd.DataFrame): The input DataFrame containing the data.

    Returns:
        pd.DataFrame: The prepared DataFrame with the necessary features.
    """

    df = df[["FirstName", "ModifiedDate"]].sort_values(by="ModifiedDate")
    df["FirstNameLen"] = df["FirstName"].str.len()
    df["ModifiedDate"] = (
        pd.to_datetime(df["ModifiedDate"]) - pd.to_datetime(df["ModifiedDate"]).min()
    )
    df["ModifiedDate"] = df["ModifiedDate"].dt.days

    return df[["FirstNameLen", "ModifiedDate"]].reset_index(drop=True)


def int_to_date(day_int: int, start_date: t.Optional[date] = None) -> str:
    """
    Convert an integer to a date string in the format YYYY-MM-DD.

    This function is specifically designed to this dataset
    """

    if start_date is None:
        start_date = date(2005, 7, 1)

    result = start_date + timedelta(days=day_int)
    result = result.strftime("%Y-%m-%d")
    return result


def run(raw_data: str) -> str:
    """
    This function is called when the model is invoked through the endpoint.

    raw_data: str
        The input data in JSON format. It should contain a list of dictionaries
        with the keys "FirstName" and "ModifiedDate".

    Returns:
        str: A JSON string containing the predicted dates
    """

    try:
        data = json.loads(raw_data)["data"][0]
        data = pd.DataFrame(data)

        data = prepare_data(data)

        columns_model = ["FirstNameLen"]

        data_dummies = data[columns_model]

        result = model.predict(data_dummies).tolist()

        for i in range(len(result)):
            result[i] = int_to_date(result[i])

        return json.dumps(result)
    except Exception as e:
        return json.dumps({"error": str(e)})
