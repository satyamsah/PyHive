from pyhive import hive
import contextlib
def thrift_http_auth_none():
    with contextlib.closing(
            hive.connect(host="144.25.105.229", port="80", thrift_transport_protocol="http", auth='OCI_AUTH')
    ) as connection:
        with contextlib.closing(connection.cursor()) as cursor:
            #cursor.execute("show databases")
            cursor.execute("create EXTERNAL table t1109889(key STRING, value INT) LOCATION 'oci://bucket1@idfoaqwbw7ew/t1109889'");
            cursor.execute("insert into t1109889 values('k11',110988)")
            cursor.execute("select * from t1109889")
            print(cursor.fetchall());
thrift_http_auth_none()