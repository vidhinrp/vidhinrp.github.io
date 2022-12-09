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
    By default, vitals included are body weight, body temperature, heart rate, diastolic blood pressure, 
    systolic blood pressure and respiratory rate. For numerical measurements, min, max and mean values 
    are included for each visit. 

    Also requires a SparkSession.

    Args:
        spark: SparkSession
        conditions: Pyspark frame of the conditions table
        concept: Pyspark frame of the concept table
        codes: list of ICD10CM codes for vitals and other measurements to include in addition to default

    Returns:
        A tuple of the full data
    """
    
    measure_columns = [
            "visit_occurrence_id", 
            "measurement_concept_id", 
            "measurement_source_value",
            "value_source_value",
            "value_as_number"]

    measure = measurement.select([col for col in measure_columns])
    measure= measure.join(concept, measure.measurement_concept_id == concept.concept_id)

    icd10 = [3025315, 3020891, 3027018, 3012888, 3004249, 3024171]
    # Body weight,  Body temperature, Heart rate, Diastolic blood pressure,
    #Systolic blood pressure, RR  
    
    if codes != []:
        icd10.extend(codes)
    
    measure = measure.filter(col('concept_id').isin(icd10))
    measure = measure.withColumn("value_as_category", when(F.col("value_source_value").cast("int").isNotNull()==False, col("value_source_value")).otherwise(None))
    measure_df = measure.groupby("visit_occurrence_id", "measurement_concept_id", "measurement_source_value").agg(F.max("value_as_number").alias("max_value"),\
                                                                  F.min("value_as_number").alias("min_value"),\
                                                                  F.mean("value_as_number").alias("mean_value"),\
                                                                  F.collect_list("value_as_category").alias("categorical_value"))

    return measure_df


