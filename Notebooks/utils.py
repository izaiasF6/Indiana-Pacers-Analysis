from pandas import DataFrame, Series
from typing import List

def convert_to_int(dataframe: DataFrame, columns: List[str]) -> DataFrame:
    """Converte os tipos das colunas especificadas para integer

    Parâmetros:
        dataframe (DataFrame): O dataframe a ser modificado
        columns (list[str]): Lista com o nome das colunas do dataframe que serão convertidas para int

    Returns:
        Dataframe: Dataframe com as colunas convertidas para o tipo inteiro
    """
    for col in columns:
        dataframe[col] = dataframe[col].astype(int)

    return dataframe


def convert_to_float(dataframe: DataFrame, columns: List[str]) -> DataFrame:
    """Converte os tipos das colunas especificadas para float

    Parâmetros:
        dataframe (DataFrame): O dataframe a ser modificado
        columns (list[str]): Lista com o nome das colunas do dataframe que serão convertidas para float

    Retorno:
        Dataframe: Dataframe com as colunas convertidas para o tipo float
    """
    
    for col in columns:
        dataframe[col] = dataframe[col].astype(float)

    return dataframe


def percentage_transformation(dataframe, columns):
    """Converte dados em porcentagem decimal para porcentagem percentual

    Parâmetros:
        dataframe (DataFrame): O dataframe a ser modificado
        columns (list[str]): Lista com o nome das colunas do dataframe que serão convertidas para porcentagem percentual

    Retorno:
        Dataframe: Dataframe com os dados das colunas convertidas para porcentagem percentual
    """
    for i in columns:
        dataframe[i] = dataframe[i] * 100

    return dataframe


def media(dataframe: DataFrame, dataframe_2: DataFrame, column: str, position: str, stats: List[str]) -> List[float]:  
    total_stats = dataframe.loc[dataframe_2[column] == position, stats].mean()
    
    if isinstance(total_stats, Series):
        return total_stats.tolist()
    else:
        return [total_stats]