#!/bin/bash
curl -X POST https://api.twilio.com/2010-04-01/Accounts/$ACCOUNT_SID/Messages.json \
--data-urlencode "To=+18777804236" \
--data-urlencode "From=+17125666904" \
--data-urlencode "Body=Hello from Twilio!" \
-u $ACCOUNT_SID:$AUTH_TOKEN

curl -X GET https://api.twilio.com/2010-04-01/Accounts/$ACCOUNT_SID/Calls.json \
-u $ACCOUNT_SID:$AUTH_TOKEN
