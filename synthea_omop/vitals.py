from pyspark.sql import SparkSession
from pyspark import sql
from pyspark.sql import functions as F
from pyspark.sql.functions import col, when
from typing import Mapping, Sequence, Tuple

from pyspark.sql.types import *

def vitals_pull(
    spark: SparkSession, 
    measurement: sql.DataFrame,
    concept: sql.DataFrame,
    codes: Sequence[int] = [],
) -> Tuple[sql.DataFrame, sql.DataFrame]:
    """Extracts ED Vitals from OMOP dataset.

    Inputs a number of criteria for measurements and outputs pyspark DataFrames that contains the full patient dataset.
    Vitals included are body weight, body temperature, heart rate, diastolic blood pressure, 
    systolic blood pressure and respiratory rate. For each  measurement, the min, max and mean values 
    are included for each visit. 

    Also requires a SparkSession.

    Args:
        spark: SparkSession
        conditions: Pyspark frame of the conditions table
        concept: Pyspark frame of the concept table
        codes: list of ICD10CM codes for vitals

    Returns:
        A tuple of the full data
    """
    
    measure_columns = [
                "visit_occurrence_id", 
                "measurement_concept_id",
                "value_as_number"]

    concept_columns = [
                "concept_id",
                "concept_name"
    ]
    measure = measurement.select([col for col in measure_columns])
    measure= measure.join(concept, measure.measurement_concept_id == concept.concept_id)

    icd10 = [3025315, 3020891, 3027018, 3012888, 3004249, 3024171]
    # Body weight,  Body temperature, Heart rate, Diastolic blood pressure,
    #Systolic blood pressure, RR  

    measure = measure.filter(col('concept_id').isin(icd10))
    measuredf = measure.groupby("visit_occurrence_id").pivot("concept_name").agg(F.max("value_as_number").alias("max"),\
                                                                    F.min("value_as_number").alias("min"),\
                                                                    F.mean("value_as_number").alias("mean"))

    measuredf = measuredf.select([F.col(col).alias(col.replace(' ', '_').lower()) for col in measuredf.columns])
    return measuredf



