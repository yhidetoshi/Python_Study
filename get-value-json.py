import json

inputData = open('./SampleJson/sample2.json')
outputData = json.load(inputData)

print(outputData)
print(outputData["form"]["action"])
