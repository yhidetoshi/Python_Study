import json

"""
Json形式 オブジェクト形式

{
	"name": "まつもと”,
	"birthday": "1991-06-15",
	"gender": "male",
	"hobby": "baseball"
}
"""

"""
Json形式 配列形式

{
	"Sports": [
		"野球",
		"サッカー",
		"テニス"
	]
}
"""


inputData = open('./SampleJson/sample3.json')
outputData = json.load(inputData)

print(outputData)
print(len(outputData["Sports"])) # 3
