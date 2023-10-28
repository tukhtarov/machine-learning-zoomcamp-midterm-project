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