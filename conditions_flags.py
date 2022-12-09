import datetime
import math
from os import walk
from typing import Mapping, Sequence, Tuple

from pyspark import sql
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import col, datediff, lit, to_date, when

def condition_selection(
    df: sql.DataFrame, keywords: Sequence[str]=[], keycodes: Sequence[int]=[]
) -> sql.DataFrame:

    if keycodes == [] and keywords == []:
        raise BaseException("Must specify 1 or more keyword(s) or SNOMED code(s) for conditions to include")

    all_cols = []
    for word in keywords:
        df = df.withColumn(word, when(df["concept_name"].contains(word),1).otherwise(0))
        all_cols.append(word)

    for code in keycodes: 
        df = df.withColumn(str(code), when(df["concept_id"]==code,1).otherwise(0))
        all_cols.append(str(code))

    df = df.groupby('visit_occurrence_id').agg(*[F.max(col).alias(col) for col in all_cols])
    return df

def condition_pull(
    spark: SparkSession,
    concept: sql.DataFrame,
    condition: sql.DataFrame,
    conditions: Sequence[str] = [],
    codes: Sequence[int]=[]
) -> sql.DataFrame:

    """Creates flags for conditions from OMOP dataset.

        Inputs list of SNOMED codes and/or list of keywords for conditions and outputs a pyspark DataFrames 
        that contains the full patient dataset. 

        Also requires a SparkSession.

        Args:
            spark: SparkSession
            condition: Pyspark frame of the conditions table
            concept: Pyspark frame of the concept table
            conditions: create flags for conditions by condition name
            codes: create flags for conditions by IC10CM codes

        Returns:
            A tuple of the full data
        """

    concepts_columns = [
            "concept_name",
            "concept_id"]

    concepts_df = concept.select([col for col in concepts_columns])

    condition_columns = [
            "visit_occurrence_id",
            "condition_concept_id"]

    condition_df = condition.select([col for col in condition_columns])
    condition_df = condition_df.join(concepts_df, condition_df.condition_concept_id == concepts_df.concept_id)
    condition_df = condition_selection(condition_df, keywords=conditions, keycodes=codes)

    return condition_df

