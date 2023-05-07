import pandas as pd

def convert_to_json(data):
    df = pd.read_csv(data)
    json_data = df.to_json(orient="records")
    return json_data
