/submit/expense/

POST, return a json

input : bought , amount , token , date (optional)

output : status: ok


/submit/income/

POST, return a json

input : text , amount , token , date (optional)

output : status:ok

/register/signup/

    step1:POST
    input : username , email , password
    output : status:ok

    <!-- step 2 : GET click on link with the code in the email     -->

    input : email , code
    output : status:ok (show the token)

/query/generalstat
POST , return a json

input : token

output : Count & sum income , expense

/query/incomestat/
POST , return json

input: username , password

output: Income

/query/expensestat/
POST , return json

input: username , password

output: Expense

/query/incomes/
POST , return json

input: token

output: incomes

/query/expenses/
POST , return json

input: token

output: expenses
