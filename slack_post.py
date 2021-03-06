import urllib.request
import json

url = 'https://hooks.slack.com/services/XXXXX'


def post_slack(msg):
    set_fileds = [{
        "title": "TITLE",
        "value": msg,
        "short": False
    }]

    data = {
        'attachments':  [{
            #'color': '#FF0000',
            'color': 'danger',
            'fields': set_fileds
        }]
    }

    method = 'POST'
    request_headers = { 'Content-Type': 'application/json; charset=utf-8' }
    body = json.dumps(data).encode("utf-8")
    request = urllib.request.Request(
        url=url, 
        data=body, 
        method=method,
        headers=request_headers 
    )

    urllib.request.urlopen(request)

if __name__ == '__main__':
    msg = "My name is yhidetoshi"
    post_slack(msg)
