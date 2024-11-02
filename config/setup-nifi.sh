docker cp ./jars/mysql-connector-j-8.4.0.jar nifi:/opt/nifi/nifi-current/lib/mysql-connector-j-8.4.0.jar
docker cp ./nifi-config/core-site.xml nifi:/opt/nifi/nifi-current/conf/
docker cp ./nifi-config/hdfs-site.xml nifi:/opt/nifi/nifi-current/conf/