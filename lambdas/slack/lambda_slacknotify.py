import json



SLACK_URL = "https://hooks.slack.com/services/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"


def lambda_handler(event, context):
    from urllib import request, parse
    print(event)
    service_name = event['service_name']
    cluster_name = event['cluster_name']
    jsondata = "Rollback : {} \n" \
               "service_name: {} \n" \
               "cluster_name: {} \n" \
               "".format(True, service_name,cluster_name)
    post = {"text": "{}".format(jsondata)
    }
    try:
        json_data = json.dumps(post)
        req = request.Request("https://hooks.slack.com/services/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",
                              data=json_data.encode('ascii'), headers={'Content-Type': 'application/json'})
        resp = request.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))
        
lambda_handler