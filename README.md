# sensiboAlert

This script will connect to the Sensibo API and pull down current temperature and device status.  It will generate an alert via email if the device is offline or temperature falls below a specified threshhold.  Email is sent via SendGrid, which allows 100 free emails per day.  Can be added to cron/scheduler to alert you if the device goes offline or temperature exceeds a desired threshhold.

**Instructions**

* `pip install requests sendgrid`
* Add your Sensibo API key to sensibo_apiKey
* Add SendGrid API key to sg_apiKey
* Add email address to sendTo

