# SonarQube metrics exporter to InfluxDB

Simple script that ships all project metrics from SonarQube to InfluxDB.

## Requirements

- Python >= 3
- InfluxDB python module
- Python Requests

Python requirements can be installed with ```pip```

    pip install -r requirements.txt
    
## Usage

Secrets such users and passwords are handles via environment variables for simplicity. 

Required ones are: 

```
USER = os.environ['SONAR_USER']
PASSWORD = os.environ['SONAR_PASSWORD']
INFLUX_USER = os.environ['INFLUX_USER']
INFLUX_PASSWORD = os.environ['INFLUX_PASSWORD']
INFLUX_DB = os.environ['INFLUX_DB']
```

You can simply execute it like:

    $ SONAR_USER=user SONAR_PASSWORD=passwd INFLUX_USER=user INFLUX_PASSWORD=passwd INFLUX_DB=db python sonar-client.py
    
This will export all the metrics in the following ```json```

```
[
    {
        "fields": {
            "value": "75"
        },
        "measurement": "coverage",
        "tags": {
            "id": "somekey",
            "key": "org.sonarqube:example-generic-coverage-sonar-scanner"
        },
        "time": "2017-05-17T13:02:43.597894"
    }
]
```


----------
Author: Pedro Diaz <pedro.diaz@tieto.com>