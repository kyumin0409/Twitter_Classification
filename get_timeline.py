import twitter

def get_user_tweets(screen_name):
	twitter_api_key = "0jmX7pjlOm0IuIk7FB20tEUsN"
	twitter_secret_api_key = "WnYookGX1FC28ON9G84hIs0qycEoDH6fyTiZMXd6Cde4811ScF"
	twitter_access_token = "1058430781096427521-vfCDfgVv4O7kPdtUdMm5wfQI9D4lsK"
	twitter_access_token_secret = "U08p8iugJ5goq32qCulIURU4L0MKdHW9hIFsWo8OZsgMU"
	api = twitter.Api(twitter_api_key, twitter_secret_api_key, twitter_access_token, twitter_access_token_secret, tweet_mode='extended',sleep_on_rate_limit=True)
	timeline_tweets = []
	timeline_tweets = api.GetUserTimeline(screen_name=screen_name, count=1500)
	last_index = timeline_tweets[-1].id
	for i in range(900):
		next_tweet_batch = api.GetUserTimeline(screen_name=screen_name, max_id=last_index-1)
		if len(next_tweet_batch) > 0 :
			timeline_tweets.extend(next_tweet_batch)
			last_index = next_tweet_batch[-1].id
		else:
			break
	return timeline_tweets

def get_all_timelines(politicians):
	for politician in politicians:
		print("Fetching timeline for "+ politician+ ".....")
		user_timeline = get_user_tweets(politician)
		write_timeline_to_file(politician, user_timeline)

def write_timeline_to_file(politician, timeline_tweets):
	filename = "app_data/user_timelines/"+politician+".txt"
	f = open(filename,"w")
	for tweet in timeline_tweets:
		tweet_text = tweet.full_text
		if "RT" not in tweet_text:
			f.write(tweet.full_text)
			f.write('\n')
	f.close()


def create_files(politicians):
	for politician in politicians:
		filename = "app_data/user_timelines/"+politician+".txt"
		file = open(filename,"w+")
		file.close()

def main():
	politicians = ["SenFeinstein","SenKamalaHarris","SenSanders" ,"HillaryClinton",
	"BarackObama","timkaine","JoeBiden","SenWarren","SenBooker","SenGillibrand","SenTedCruz",
	"SenatorHeitkamp","BobbyJindal","VP","GrahamBlog" ,"JeffFlake","senatemajldr","JohnCornyn",
	"MikeCrapo","marcorubio"]
	create_files(politicians)

	get_all_timelines(politicians)
	
if __name__ == "__main__":
	main()

