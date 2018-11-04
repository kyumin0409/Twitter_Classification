import tweepy

def load_tweet_ids(filename):
	tweet_ids =[]
	with open(filename) as f_read:
		for line in f_read:
			tweet_ids.append(line.strip())
		f_read.close()
	return tweet_ids

def retrieve_tweets(tweet_ids,api):
	no_tweet_ids = len(tweet_ids)
	divisions = int(no_tweet_ids/100)
	if divisions*100 < no_tweet_ids:
		divisions = divisions+1
	request_arr = []
	counter = 0
	for d in range(divisions):
		for t in range(100):
			request_arr.append(tweet_ids[counter])
			counter=counter+1
		# print(request_arr)
		tweet_objs= api.statuses_lookup(request_arr)
		print("Made API call.."+","+str(d))
		write_to_file(tweet_objs)
		request_arr = []

def write_to_file(tweets):
	tweet_content_file = "app_data/ireland_tweets.txt"
	with open(tweet_content_file,"a") as f_write:
		for t in tweets:
			tweet_text = t.text
			f_write.write(tweet_text)
			f_write.write("\n")
	f_write.close()

def main():

	auth = tweepy.OAuthHandler("0jmX7pjlOm0IuIk7FB20tEUsN","WnYookGX1FC28ON9G84hIs0qycEoDH6fyTiZMXd6Cde4811ScF")
	auth.set_access_token("1058430781096427521-vfCDfgVv4O7kPdtUdMm5wfQI9D4lsK","U08p8iugJ5goq32qCulIURU4L0MKdHW9hIFsWo8OZsgMU")

	api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
	tweet_id_file = "app_data/ireland8th.txt"
	tweet_ids =load_tweet_ids(tweet_id_file)
	retrieve_tweets(tweet_ids,api)

if __name__ == "__main__":
	main()