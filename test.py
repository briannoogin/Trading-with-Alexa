from __future__ import absolute_import
import json
from watson_developer_cloud import ToneAnalyzerV3

#print (json.__file__)
tone_analyzer = ToneAnalyzerV3(
	version = "2018-11-16",
	iam_apikey = 'zysPjU3l5tlcf1vvL1eFnDP33H7vFNG0tFDId0qX6QOv',
	url = 'https://gateway.watsonplatform.net/tone-analyzer/api'
)

text = "Team, How in the world did you loose that match? "\
	"I am thoroughly dissapointed in you guys. I expected "\
	"quite a lot from you all" 

tone_analysis = tone_analyzer.tone(
	{'text': text},
	'application/json'
).get_result()
jsonVal = json.dumps(tone_analysis, indent=2)
jsonVal = json.loads(jsonVal)
print(jsonVal)
#print("Tone: "+jsonVal["document_tone"]["tones"][0]["tone_name"])
