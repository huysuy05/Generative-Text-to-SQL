import json
from pyspark.sql import SparkSession 
import os

if __name__ == "__main__":
    spark = SparkSession.builder \
                        .appName("GetMetadata") \
                        .config("hive.metastore.uris", "thrift://hive-metastore:9083") \
                        .enableHiveSupport() \
                        .getOrCreate()
    spark.sql("USE vdt;")
    tables = spark.sql("SHOW TABLES").collect()
    print(tables)
    metadata_dict = {}
    for table in tables:
        table_name = table['tableName'] # Lấy tên bảng
        metadata_dict[table_name] = {}

    # Lấy schema cho từng bảng
        schema = spark.sql(f"DESCRIBE {table_name}")
        df = schema.collect()
        metadata_dict[table_name]['schema'] = [
                {'column': row['col_name'],
                'data_type': row['data_type'],
                'comment': row['comment']}
                for row in df
        ]

    output_file_path = "/opt/bitnami/meta/metadata.jsonl"
    with open(output_file_path, "w") as file:
        json.dump(metadata_dict, file, indent=4)
    spark.stop() 
