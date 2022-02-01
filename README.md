## Project description
Small and simple package to connect to the PSAT (Proofpoint Security Awareness Traning) result API.

## Proofpoint Result API

See the [REST API full documentation](https://proofpoint.securityeducation.com/api/reporting/documentation/#api-Introduction) for more information.

## Installation
```
pip install psat-result-api
```

## Example
```python
from psat import ResultApi

p = ResultApi("insert-api-token-here")

# Return training assignments data
training = p.get_training() 

# Return users data with some parameters
users = p.get_users(
        params={
            "user_tag_enable": "FALSE",
            "filter[_useremailaddress]": "[user@domain.com]",
        }
    )

```

## Supported endpoints
* CyberStrength ( *get_users()* )
* PhishAlarm ( *get_cyberstrength()* )
* Phishing ( *get_phishalarm()* )
* Training ( *get_phishing()* )
* Users ( *get_training()* )
* TrainingEnrollments ( *get_trainingenrollments()* )