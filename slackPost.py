import slackweb

slack = slackweb.Slack(url="https://hooks.slack.com/services/XXXXXXXXXXXX")
slack.notify(text="Post Test by Python")
