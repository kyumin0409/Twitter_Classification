import tweepy

#load tweet ids from the tweet id file
def load_tweet_ids(filename, size):
	tweet_ids =[]
	if size =="big":
		line_counter = 0
	with open(filename) as f_read:
		if size == "big":
			for line in f_read:
				tweet_ids.append(line.strip())
				line_counter = line_counter + 1
				if line_counter == 610700:
					break
		elif size == "small":
			for line in f_read:
				tweet_ids.append(line.strip())
		f_read.close()
	return tweet_ids


#retrieves tweet content from tweet id using twitter api
def retrieve_tweets(tweet_ids,api):
	no_tweet_ids = len(tweet_ids)
	#calculate how many packets containing 100 tweet ids we need?
	#twitter allows getting 100 tweets from their ids at a time
	divisions = int(no_tweet_ids/100)
	if divisions*100 < no_tweet_ids:
		divisions = divisions+1
	fixed_divisions = 6107
	request_arr = []
	counter = 0
	for d in range(fixed_divisions):
		for t in range(100):
			#create a request id array having tweet ids
			request_arr.append(tweet_ids[counter])
			#keep index going till possibly all tweet ids are sent to the API
			counter=counter+1
		# print(request_arr)
		#API call
		tweet_objs= api.statuses_lookup(request_arr)
		print("Made API call.."+","+str(d))
		#write API response, i.e tweet content to output file
		write_to_file(tweet_objs)
		#empty req array to take the next 100 tweet ids
		request_arr = []

#write tweets to output file
def write_to_file(tweets):
	tweet_content_file = "app_data/travel_ban_tweets.txt"
	tweets_users_content_file = "app_data/ireland_tweets_with_users.txt"

	# with open(tweet_content_file,"a") as f_write
	with open(tweets_users_content_file,"a") as f_users_write:
		for t in tweets:
			#take text only from tweet object
			tweet_text = t.text
			# f_write.write(tweet_text)
			# f_write.write("\n")
			f_users_write.write("user: "+t.user.screen_name +" "+"tweet: "+tweet_text)
			f_users_write.write("\n")

	#f_write.close()
	f_users_write.close()

def count_tweets(filename):
	ct = 0
	with open(filename) as f_read:
		for line in f_read:
			ct = ct+1
	print("number of tweets for "+filename+" :"+ str(ct))

def main():

	auth = tweepy.OAuthHandler("0jmX7pjlOm0IuIk7FB20tEUsN","WnYookGX1FC28ON9G84hIs0qycEoDH6fyTiZMXd6Cde4811ScF")
	auth.set_access_token("1058430781096427521-vfCDfgVv4O7kPdtUdMm5wfQI9D4lsK","U08p8iugJ5goq32qCulIURU4L0MKdHW9hIFsWo8OZsgMU")

	api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
	#output file the contents of tweets should be written to
	tweet_id_file = "app_data/ireland8th.txt"
	# tweet_ids =load_tweet_ids(tweet_id_file,"big")
	# retrieve_tweets(tweet_ids,api)
	# print("Tweet retrieval done")
	count_tweets("app_data/brexit_tweetsCopy.txt")
	count_tweets("app_data/travel_ban_tweetsCopy.txt")
	# count_tweets("app_data/trump_tweetsCopy.txt")
	# count_tweets("app_data/ireland_tweetsEmoji.txt")

if __name__ == "__main__":
	main()