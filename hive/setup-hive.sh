# Copy file setup lên container
docker cp ./hive/setup.sql hive-server:/
# Chạy file setup
docker exec -it hive-server /opt/hive/bin/hive -f /setup.sql
# Check kết quả tạo bảng
docker exec -it hive-server bash -c "/opt/hive/bin/beeline -u jdbc:hive2://localhost:10000 -e 'USE vdt; SHOW TABLES;'"
