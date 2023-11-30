#bin/bash
# please set variables
source Config.sh
curl --data "token  = $1 , text = $2 , amount = $3 , date = $4" http://localhost:8000/submit/income

# If you don't enter the date, the date will automatically go to now