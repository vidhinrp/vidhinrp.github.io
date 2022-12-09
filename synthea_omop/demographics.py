import datetime
import math
from os import walk
from typing import Mapping, Sequence, Tuple

from pyspark import sql
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import col, datediff, lit, to_date, when

def numerical_column_selection(
    df: sql.DataFrame, column: str, values: Sequence[int]
) -> sql.DataFrame:

    if len(values) == 2:
        return df.filter((col(column) >= lit(values[0])) & (col(column) <= lit(values[-1])))
    else:
        return df.filter((col(column) == lit(values[0])))


def catagorical_column_selection(
    df: sql.DataFrame, column: str, values: Sequence[str]
) -> sql.DataFrame:
    return df.filter(col(column).isin(values))


def datetime_column_selection(
    df: sql.DataFrame, values: Sequence[datetime.datetime]
) -> sql.DataFrame:
    if len(values) == 2:
        return df.where(
            (df.visit_start_datetime >= lit(values[0]))
            & (df.visit_start_datetime <= lit(values[1]))
        )
    else:
        return df.where((df.visit_start_datetime == lit(values[0])))
        
def demographic_pull(
    spark: SparkSession,
    visit_occurrence: sql.DataFrame,
    person: sql.DataFrame,
    death: sql.DataFrame,
    age: Sequence[int] = [],
    visit_age: Sequence[int] = [],
    gender: Sequence[str] = [],
    race: Sequence[str] = [],
    ethnicity: Sequence[str] = [],
    visit_date: Sequence[datetime.datetime] = []

) -> sql.DataFrame:
    """Extracts demographics from OMOP dataset.

    Inputs a number of criteria for demographics columns (e.g. age, race) and outputs a pyspark DataFrames
    that contains the full patient dataset. 

    Also requires a SparkSession.

    Args:
        spark: SparkSession
        visit_occurrence: Pyspark frame of the visit_occurrence table
        person: Pyspark frame of the person table
        death: Pyspark frame of the death table
        location: Pyspark frame of the location table
        group_value: group by either visits (visit_occurrence_id) or person (person_id)
        age: filter by age range
        visit_age: filter by age range at visit
        gender: filter by gender list
        race: filter by race list
        ethnicity: filter by ethnicity list
        visit_date: filter by visit_date range
        visit_location: filter by visit location dict

    Returns:
        A tuple of the full data
    """

    visit_length_columns = [
        "person_id",
        "visit_occurrence_id",
        "visit_start_datetime",
        "visit_end_datetime"]

    visit_length = visit_occurrence.select([col for col in visit_length_columns])
    visit_length = visit_length.withColumn(
        "visit_length",
        col("visit_end_datetime").cast("long") - col("visit_start_datetime").cast("long"),
    )

    demo_columns = [
        "person_id",
        "gender_concept_id",
        "birth_datetime",
        "gender_source_value", 
        "race_source_value", 
        "ethnicity_source_value"]

    demo = person.select([col for col in demo_columns])
 
    death_columns = [
        "person_id",
        "death_date"]

    death_df = death.select([col for col in death_columns]).withColumn('death_date', death.death_date.cast('timestamp'))

    demo = demo.join(visit_length, on="person_id", how="outer")\
               .join(death_df, on="person_id", how="left")\

    now = datetime.datetime.now()
    demo = demo.withColumn("visit_age", (F.months_between(col('visit_start_datetime'), F.col('birth_datetime')) / 12).cast('int'))\
                .withColumn("age", when(col("death_date").isNull(),
                            (F.months_between(lit(now), F.col('birth_datetime')) / 12).cast('int'))\
                            .otherwise((F.months_between(col('death_date'), F.col('birth_datetime')) / 12).cast('int')))
    
    main_df = demo

    if age != []:
        main_df = numerical_column_selection(main_df, "age", age)

    if visit_age != []:
        main_df = numerical_column_selection(main_df, "visit_age", visit_age)

    if gender != []:
        main_df = catagorical_column_selection(main_df, "gender_source_value", gender)

    if race != []:
        main_df = catagorical_column_selection(main_df, "race_source_value", race)

    if ethnicity != []:
        main_df = catagorical_column_selection(main_df, "ethnicity_source_value", ethnicity)

    if visit_date != []:
        main_df = datetime_column_selection(main_df, visit_date)

    return main_df