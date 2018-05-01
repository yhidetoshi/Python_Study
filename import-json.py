import json

inputData = open('./SampleJson/sample1.json')
outputData = json.load(inputData)

print(outputData)
print(outputData["スコア一覧"])
