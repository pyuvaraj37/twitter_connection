from requests_oauthlib import OAuth1Session
import json
import twitter_connection.urls as u
import twitter_connection.format as f


class twitter_connection():
    
    def __init__(self, consumer_api_key, consumer_api_secret_key, access_token, access_token_secret):
        self.consumer_api_key = consumer_api_key
        self.consumer_api_secret_key = consumer_api_secret_key
        self.access_token = access_token
        self.access_token_secret = access_token_secret

    def standard_search(self, 
                        search_terms=None, 
                        from_user=None, 
                        reply_to=None, 
                        not_including=None, 
                        phrases=None, 
                        filters=None, 
                        not_filters=None,
                        positive=None, 
                        since=None, 
                        until=None,
                        geocode=None,
                        lang=None,
                        locale=None,
                        result_type=None,
                        count=None,
                        since_id=None,
                        max_id=None,
                        include_entities=None):
        
        session = OAuth1Session(self.consumer_api_key,
                            client_secret=self.consumer_api_secret_key,
                            resource_owner_key=self.access_token,
                            resource_owner_secret=self.access_token_secret)
        
        q=['q=']
        q.append(f.format_search_terms(search_terms))
        q.append(f.format_from_user(from_user[1:]))
        q.append(f.format_reply_to(reply_to))
        q.append(f.format_not_including(not_including))
        q.append(f.format_phrases(phrases))
        q.append(f.format_filter(filters))
        q.append(f.format_not_filter(not_filters))
        q.append(f.format_positive(positive))
        q.append(f.format_since(since))
        q.append(f.format_until(until))
        q.append(f.format_geocode(geocode))
        q.append(f.format_lang(lang))
        q.append(f.format_locale(locale))
        q.append(f.format_result_type(result_type))
        q.append(f.format_count(count))
        q.append(f.format_since_id(since_id))
        q.append(f.format_max_id(max_id))
        q.append(f.format_include_entities(include_entities))
        
    
        url = u.search()
        search_query = ''.join(q)
        full_url = url + search_query
        #print(full_url)
        response = session.get(full_url + '&tweet_mode=extended')

        return(response.json())
    
