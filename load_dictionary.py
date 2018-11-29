def load_dict(politicians, broken_keywords, keyword_tweet_dict):
	for politician in politicians:
		print("Organizing "+politician+" tweets based on keywords...")
		filename = "app_data/user_timelines/"+politician+".txt" 
		file = open(filename,"r")
		broken_keywords_keys = broken_keywords.keys()
		for tweet in file:
			lower_tweet = tweet.lower()
			for keyword in broken_keywords_keys:
				for k in broken_keywords[keyword]:
					if k in lower_tweet:
						updated_tuple = keyword_tweet_dict[keyword]+(politician+":"+tweet,)
						keyword_tweet_dict[keyword] = updated_tuple
						break
	output_dict = keyword_tweet_dict
	return output_dict


def break_down(keywords):
	broken_keywords = {}
	for keyword in keywords: 
		splitted_keyword = keyword.lower().split()
		broken_keywords[keyword] = tuple(splitted_keyword)
	return broken_keywords

def init_dict(keywords):
	keyword_tweet_dict = {}
	for keyword in keywords:
		keyword_tweet_dict[keyword] = ()
	return keyword_tweet_dict

def print_dict(output_dict):
	keyword_keys = list(output_dict.keys())
	print("Keyword: "+keyword_keys[0])
	for tweet in output_dict[keyword_keys[0]]:
		print(tweet)
		print("\n")


def main():
	keywords = ["Travel Ban", "Obamacare Affordable care act", 
	"Marijuana", "Net Neutrality", "Gay Marriage", 
	"Affirmative Action", "DACA immigration" , 
	"Assisted Suicide", "Capital punishment", 
	"labor unions", "vaccines, concealed weapons", 
	"self-driving cars","Artificial intelligence", 
	"Donald Trump","Planned Parenthood", "Social Security", "NRA", 
	"Fracking", "Nuclear Energy", "NSA Surveillance", "Military Spending", 
	"Foreign Aid", "Dakota Access Pipeline", "Oil Drilling", "Paris Climate Agreement", 
	"Trans Pacific Partnership", "China Tariffs", "Labor Unions", 
	"Universal Basic Income", "Paid Sick Leave", "Safe Haven", "Medicaid", 
	"Edward Snowden", "Whistleblower Protection", "Armed Teachers", "Gun Control",
	"In-State Tuition", "Immigration Ban", "Border Wall, First Amendment", 
	"Confederate Flag", "Death Penalty", "Religious Freedom Act"]

	politicians = ["SenFeinstein","SenKamalaHarris","SenSanders" ,"HillaryClinton",
	"BarackObama","timkaine","JoeBiden","SenWarren","SenBooker","SenGillibrand","SenTedCruz",
	"SenatorHeitkamp","BobbyJindal","VP","GrahamBlog" ,"JeffFlake","senatemajldr","JohnCornyn",
	"MikeCrapo","marcorubio"]

	keyword_tweet_dict = init_dict(keywords)
	
	broken_keywords = break_down(keywords)

	output_dict = load_dict(politicians,broken_keywords,keyword_tweet_dict)

	print_dict(output_dict)


if __name__ == "__main__":
	main()
