from utilities import api_key, headers, Website

# Check the API key
if not api_key:
    print("No API key was found!")
else:
    print(f"API key loaded: {api_key[:8]}...")

# Let's try one out. 
site = Website("https://www.cnn.com")
print(site.title)
print(site.text)


