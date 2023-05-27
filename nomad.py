import requests

websites = (
    'google.com',
    'https://airbnb.com',
    'https://twitter.com',
    'tatoo.com',
    'facebook.com',
    'clare.com'
)

results = {}

for website in websites:
  if not website.startswith('https://'):
    website = "https://" + website
  response = requests.get(website)
  if response.status_code >= 100 and response.status_code < 200:
    results[website] = 'Informational'
  elif response.status_code >= 200 and response.status_code < 300:
    results[website] = 'Success'
  elif response.status_code >= 300 and response.status_code < 400:
    results[website] = 'Redirection'
  elif response.status_code >= 400 and response.status_code < 500:
    results[website] = 'Client error'
  else:
    results[website] = 'Server error'
print(results)  
