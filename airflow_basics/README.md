# Airflow Basics

Sandbox for experimenting with Apache Airflow.

General Notes:
- [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/start.html).
- Airflow uses `~/airflow` as a home directory by default. However, in my case after install `echo $AIRFLOW_HOME` returned nothing so I had to then `export AIRFLOW_HOME=~/airflow`
- The command `airflow standalone` initializes the database, creates a user, and starts all components.
- Access the browser UI by visiting `localhost:8080` and logging in with the admin account details shown in the terminal. Be sure to disable any VPNs if you experience trouble connecting.
- To move a DAG into Airflow, copy the file into the Airflow directory by running `cp dummy_dag.py ~/airflow/dags` or `cp dummy_dag.py $AIRFLOW_HOME/dags`

Common Commands:
- `airflow dags list`
- `airflow tasks list dummy_dag` (replace dummy_dag with actual dag name and make sure .py extension is not tab-completed)