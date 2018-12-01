import tweepy

def search(keywords,api):
	max_tweets = 50000
	for keyword in keywords:
		print("Getting tweets with "+keyword)
		searched_tweets = []
		last_id = -1
		while len(searched_tweets) < max_tweets:
			count = max_tweets - len(searched_tweets)
			try:
				new_tweets = api.search(q=keyword.lower(), count=count, max_id=str(last_id - 1))
				if not new_tweets:
					break
				searched_tweets.extend(new_tweets)
				last_id = new_tweets[-1].id
			except tweepy.TweepError as e:
				break
		write_search_results(keyword,searched_tweets)
		searched_tweets = []


def write_search_results(keyword,search_result_list):
	filename = "app_data/tweets_by_keyword/"+keyword+".txt"
	file = open(filename, "w")
	print("Writing tweets to file now....")
	result_set = set()
	for tweet in search_result_list:
		result_set.add(tweet.full_text)
	for tweet_text in  result_set:
	 	file.write(tweet_text)
	 	file.write('\n')
	file.close()
	print(len(result_set))

def alternate_search(keywords,api):
	max_tweets = 18000
	for keyword in keywords:
		print("Getting tweets with "+keyword)
		searched_tweets = [status for status in tweepy.Cursor(api.search, q=keyword.lower(), count=100,tweet_mode='extended').items(max_tweets)]
		write_search_results(keyword,searched_tweets)
		searched_tweets = []

def create_files(keywords):
	for keyword in keywords:
		filename = "app_data/tweets_by_keyword/"+keyword+".txt"
		file = open(filename,"w+")
		file.close()

def main():
	
	auth = tweepy.OAuthHandler("0jmX7pjlOm0IuIk7FB20tEUsN","WnYookGX1FC28ON9G84hIs0qycEoDH6fyTiZMXd6Cde4811ScF")
	auth.set_access_token("1058430781096427521-vfCDfgVv4O7kPdtUdMm5wfQI9D4lsK","U08p8iugJ5goq32qCulIURU4L0MKdHW9hIFsWo8OZsgMU")

	api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
	#["Travel Ban", "Obamacare"," Affordable care act", "Marijuana", "Net Neutrality","Gay Marriage",
	keywords  = [  
	"Affirmative Action", "DACA immigration" , 
	"Assisted Suicide", "Capital punishment", 
	"labor unions", "vaccines", "concealed weapons", 
	"self-driving cars","Artificial intelligence", 
	"Donald Trump","Planned Parenthood", "Social Security", "NRA", 
	"Fracking", "Nuclear Energy", "NSA Surveillance", "Military Spending", 
	"Foreign Aid", "Dakota Access Pipeline", "Oil Drilling", "Paris Climate Agreement", 
	"Trans Pacific Partnership", "China Tariffs", "Labor Unions", 
	"Universal Basic Income", "Paid Sick Leave", "Safe Haven", "Medicaid", 
	"Edward Snowden", "Whistleblower Protection", "Armed Teachers", "Gun Control",
	"In-State Tuition", "Immigration Ban", "Border Wall", "First Amendment", 
	"Confederate Flag", "Death Penalty", "Religious Freedom Act"]

	selected_keywords = ["Travel Ban", "Obamacare"," Affordable care act"]

	# create_files(keywords)
	alternate_search(selected_keywords,api)


if __name__ == "__main__":
	main()