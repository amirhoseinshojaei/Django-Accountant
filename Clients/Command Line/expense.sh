#bin/bash
source Config.sh

curl --data "token  = $1 , bought = $2 , amount = $3 , date = $4" http:localhost:8000/submit/expense/

# If you don't enter the date, the date will automatically go to now