
import requests
import json
import webbrowser


flickr_key = '84d44160ef70100a8b26965a9e64872a'

def get_flickr_data(tags_string):
    baseurl = "https://api.flickr.com/services/rest/"
    params_diction = {}
    params_diction["api_key"] = flickr_key 
    params_diction["tags"] = tags_string 
    params_diction["tag_mode"] = "all"
    params_diction["method"] = "flickr.photos.search"
    params_diction["per_page"] = 5
    params_diction["media"] = "photos"
    params_diction["format"] = "json"
    params_diction["nojsoncallback"] = 1
    flickr_resp = requests.get(baseurl, params = params_diction)
    print(flickr_resp.url) 
    return flickr_resp.json()

result_river_mts = get_flickr_data("river,mountains")
print(json.dumps(result_river_mts,indent=2))



photos = result_river_mts['photos']['photo']
for photo in photos:
    owner = photo['owner']
    photo_id = photo['id']
    url = 'https://www.flickr.com/photos/{}/{}'.format(owner, photo_id)
    print(url)
    webbrowser.open(url)
