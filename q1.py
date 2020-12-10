## 1.	Given a list, url = [www.annauniv.edu, www.google.com, www.ndtv.com, www.website.org, www.bis.org.in, www.rbi.org.in];
#  Sort the list based on the top level domain (edu, com, org, in) using custom sorting


url= ["www.annauniv.edu", "www.google.com", "www.ndtv.com", "www.website.org", "www.bis.org.in", "www.rbi.org.in"]

url.sort(key = lambda x: x.split('.')[2]==["edu","com","org","in"]) 
print(url)