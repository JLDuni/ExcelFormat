import pandas as pd


def process_contracts(df, start_id):
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

    df["num_fatura"] = ""

    columns_keep = ["num_fatura", "objeto", "matricula", "data_inicio", "data_fim"]

    df["objeto"] = range(start_id + 1, start_id + 1 + len(df))

    return df[columns_keep].to_csv(index=False).encode('utf-8')
