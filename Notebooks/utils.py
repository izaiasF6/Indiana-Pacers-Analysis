from typing import List
from pandas import DataFrame


def convert_to_int(dataframe: DataFrame, columns: List[str]) -> DataFrame:
    """Converte os tipos das colunas especificadas para integer

    Parâmetros:
        dataframe (DataFrame): DataFrame a ser modificado
        columns (list[str]): Lista com as colunas do dataframe que serão convertidas para inteiro

    Returns:
        dataframe: DataFrame com as colunas convertidas para o tipo inteiro
    """

    for col in columns:
        dataframe[col] = dataframe[col].astype(int)

    return dataframe


def convert_to_float(dataframe: DataFrame, columns: List[str]) -> DataFrame:
    """Converte os tipos das colunas especificadas para float

    Parâmetros:
        dataframe (DataFrame): DataFrame a ser modificado
        columns (list[str]): Lista com as colunas do dataframe que serão convertidas para float

    Retorno:
        Dataframe: DataFrame com as colunas convertidas para o tipo float
    """

    for col in columns:
        dataframe[col] = dataframe[col].astype(float)

    return dataframe


def percentage_transformation(dataframe, columns) -> DataFrame:
    """Converte dados em porcentagem decimal para porcentagem percentual

    Parâmetros:
        dataframe (DataFrame): DataFrame a ser modificado
        columns (list[str]): Lista de colunas do DataFrame a converter para porcentagem percentual

    Retorno:
        Dataframe: DataFrame com os dados das colunas convertidas para porcentagem percentual
    """

    for i in columns:
        dataframe[i] = dataframe[i] * 100

    return dataframe
