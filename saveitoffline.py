import json
import requests
import subprocess

def download_vid(vid_link):
	query_link = "https://www.saveitoffline.com/process/?url="+vid_link+"&type=json";
	
	try:
		saveit_resp = requests.get(query_link)
		saveit_json = json.loads(saveit_resp.text)
		print("Video: ",saveit_json["title"])
		
		for item in range(len(saveit_json['urls'])):
			print(item,")  ",saveit_json['urls'][item]['label'],saveit_json['urls'][item]['size'])
		download_item = int(input("Select The video to download: "))
		subprocess.run(['aria2c','-x2',saveit_json['urls'][download_item]['id']])
	
	except Exception as e:
		print("Exception",e,"Occoured! Retrying....")

if __name__ == "__main__":
	print("Starting Saveitoffline, ctrl-C to exit.");
	while True:
		try:
			vid_link = input("Enter Youtube link: ")
			download_vid(vid_link)
		except Exception as e:
			print("Exception",e,"Occoured! Please retry.")