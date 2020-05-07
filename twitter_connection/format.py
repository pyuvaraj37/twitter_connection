def format_search_terms(search_terms):
    s=''
    q=[]
    if search_terms != None:
        for term in search_terms:
            q.append(term)
            q.append('%20')
        s= ''.join(q)
    return s

def format_from_user(from_user):
    s=''
    q=[]
    if from_user != None:
        q.append('from%3A')
        q.append(from_user)
        q.append('%20')
        s = ''.join(q)
    return s

def format_reply_to(reply_to):
    s=''
    q=[]
    if reply_to != None:
        q.append('to%3A')
        q.append(reply_to)
        q.append('%20')
        s = ''.join(q)
    return s

def format_not_including(not_including):
    s=''
    q=[]
    if not_including != None:
        q.append('%2D')
        q.append(not_including)
        q.append('%20')
        s = ''.join(q)
    return s

def format_phrases(phrases):
    s=''
    q=[]
    if phrases != None:
        for phrase in phrases:
            q.append('%22')
            q.append(phrase)
            q.append('%22')
            q.append('%20')
        s = ''.join(q)
    return s

def format_filter(filters):
    s=''
    q=[]
    if filters != None:
        for filter in filters:
            q.append('filter')
            q.append('%3A')
            q.append(filter)
            q.append('%20')
        s = ''.join(q)
    return s

def format_not_filter(filters):
    s=''
    q=[]
    if filters != None:
        for filter in filters:
            q.append('%2D')
            q.append('filter')
            q.append('%3A')
            q.append(filter)
            q.append('%20')
        s = ''.join(q)
    return s

def format_positive(positive):
    s=''
    if positive != None:
        if positive is True:
            s = '%3A%29%20' 
        else:
            s = '%3A%28%20'
    return s

def format_since(since):
    s=''
    q=[]
    if since != None:
        q.append('&')
        q.append('since=')
        q.append(since)
        q.append('%20')
        s = ''.join(q)
    return s

def format_until(since):
    s=''
    q=[]
    if since != None:
        q.append('until%A')
        q.append(since)
        q.append('%20')
        s = ''.join(q)
    return s

def format_geocode(geocode):
    s=''
    q=[]
    if geocode != None:
        q.append('&geocode=')
        q.append(geocode)
        s = ''.join(q)
    return s

def format_lang(lang):
    s=''
    q=[]
    if lang != None:
        q.append('&lang=')
        q.append(lang)
        s = ''.join(q)
    return s

def format_locale(locale):
    s=''
    q=[]
    if locale != None:
        q.append('&locale=')
        q.append(locale)
        s = ''.join(q)
    return s

def format_result_type(result_type):
    s=''
    q=[]
    if result_type != None:
        q.append('&result_type=')
        q.append(result_type)
        s = ''.join(q)
    return s

def format_count(count):
    s=''
    q=[]
    if count != None:
        q.append('&count=')
        q.append(count)
        s = ''.join(q)
    return s

def format_since_id(since_id):
    s=''
    q=[]
    if since_id != None:
        q.append('&since_id=')
        q.append(since_id)
        s = ''.join(q)
    return s

def format_max_id(max_id):
    s=''
    q=[]
    if max_id != None:
        q.append('&max_id=')
        q.append(max_id)
        s = ''.join(q)
    return s

def format_include_entities(include_entities):
    s=''
    q=[]
    if include_entities != None:
        q.append('&include_entities=')
        q.append(include_entities)
        s = ''.join(q)
    return s