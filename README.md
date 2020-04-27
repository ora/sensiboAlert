# sensiboAlert

This script will connect to the Sensibo API and pull down current temperature and device status.  It will generate an alert via email if the device is offline or temperature falls below a specified threshhold.  Email is sent via SendGrid, which allows 100 free emails per day.
Just add a Sensibo API key, SendGrid API key, and email address to send the email to.
