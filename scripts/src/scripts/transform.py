import click

import pandas as pd
import tentaclio as tio


def _important_op(df: pd.DataFrame) -> pd.DataFrame:
    df["values"] = df["values"] * 2
    return df


def _transform(reader: tio.Reader, writer: tio.Writer):
    # Load the dataframe
    df = pd.read_csv(reader)
    # Transform
    df_tranformed = _important_op(df)
    # Store
    df_tranformed.to_csv(writer, index=False)


@click.command()
@click.option("--input-url", help="input data", required=True)
@click.option("--output-url", help="where to store the results", required=True)
def transform(input_url: str, output_url: str):
    print(f"transforming: input_url {input_url}  output_url {output_url}")
    # Data access layer
    with tio.open(input_url) as reader, tio.open(output_url, mode="w") as writer:
        _transform(reader, writer)

    print("done")


# Cli main entry point
@click.group()
def main():
    pass


main.add_command(transform)
