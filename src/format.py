import pandas as pd


def process_contracts(df):
    df = df.rename(
        columns={
            "Matrícula": "matricula",
            "Data de início": "data_inicio",
            "Data de fim": "data_fim",
        }
    )

    df["data_inicio"] = df["data_inicio"].str.replace(",", " ").str.replace("H", ":00")
    df["data_fim"] = df["data_fim"].str.replace(",", " ").str.replace("H", ":00")

    df["matricula"] = df["matricula"].str.replace(
        r"^([A-Z0-9]{2})-([A-Z0-9]{2})-([A-Z0-9]{2})$", r"\1\3-\2", regex=True
    )

    columns_keep = ["matricula", "data_inicio", "data_fim"]
    df_formated = df[columns_keep]

    return df[columns_keep].to_csv(index=False).encode('utf-8')
