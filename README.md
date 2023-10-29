## Description of the problem

This is a classification task. The problem is to predict if the client will subscribe a term deposit (variable y). For this project I used the data of direct marketing campaigns (phone calls) of a Portuguese banking institution.

Data source - https://www.openml.org/search?type=data&sort=runs&status=active&id=1461

The data is in a .arff format so I used the loadarff function from scipy.io.arff to create a dataframe from it.

The feature names were changed to be more readable:
* "v1": "age",
* "v2": "job",
* "v3": "marital_status",
* "v4": "education",
* "v5": "credit_in_default",
* "v6": "average_balance",
* "v7": "has_housing_loan",
* "v8": "has_personal_loan",
* "v9": "contact_type",
* "v10": "day",
* "v11": "month",
* "v12": "duration",
* "v13": "number_contacts",
* "v14": "pdays",
* "v15": "number_contacts_before",
* "v16": "previous_outcome",
* "class": "target"

"target" is a variable "y"

This is a detailed explanation of each feature:

1. age (numeric)
2. job : type of job (categorical: "admin.","unknown","unemployed","management","housemaid","entrepreneur", "student","blue-collar","self-employed","retired","technician","services") 
3. marital : marital status (categorical: "married","divorced","single"; note: "divorced" means divorced or widowed)
4. education (categorical: "unknown","secondary","primary","tertiary")
5. default: has credit in default? (binary: "yes","no")
6. balance: average yearly balance, in euros (numeric) 
7. housing: has housing loan? (binary: "yes","no")
8. loan: has personal loan? (binary: "yes","no") related with the last contact of the current campaign:
9. contact: contact communication type (categorical: "unknown","telephone","cellular") 
10. day: last contact day of the month (numeric)
11. month: last contact month of year (categorical: "jan", "feb", "mar", ..., "nov", "dec")
12. duration: last contact duration, in seconds (numeric) other attributes:
13. campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)
14. pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric, -1 means client was not previously contacted)
15. previous: number of contacts performed before this campaign and for this client (numeric)
16. poutcome: outcome of the previous marketing campaign (categorical: "unknown","other","failure","success")

The target variable was in the (binary: "1","2") format. I changed its format to be (binary: 0, 1) where 0 means the client did not subscribe a term deposit and 1 means the client subscribed.

## How to run the project

You need to have docker installed on your machine.

1. Clone the project
2. cd into the project directory
3. Run `docker build -t tukhtarov-zoomcamp-midterm-project .`
4. Run `docker run -it --rm -p 9696:9696 tukhtarov-zoomcamp-midterm-project`

Now you can make POST requests to http://0.0.0.0:9696/predict

## Cloud deployment

I deployed the service to https://render.com/ using this guide - https://render.com/docs/deploy-an-image

Here are the url and client JSON object for testing:

https://tukhtarov-zoomcamp-midterm-project.onrender.com/predict

```json
{'age': 59.0,
 'job': 'admin.',
 'marital_status': 'married',
 'education': 'secondary',
 'credit_in_default': 'no',
 'average_balance': 2343.0,
 'has_housing_loan': 'yes',
 'has_personal_loan': 'no',
 'contact_type': 'unknown',
 'day': 5.0,
 'month': 'may',
 'duration': 1042.0,
 'number_contacts': 1.0,
 'pdays': -1.0,
 'number_contacts_before': 0.0,
 'previous_outcome': 'unknown'}
```
You can try changing the values of the client object keys.