###############################
# CodeX Learn python          #
# Assignment 8                #
# Using APIs                  #
# 10/6/2024                   #
###############################
import requests as rqt
import json as js


#############################
# Get wiki summary
#
#############################
def get_wiki_summary(topic):
  
  # Construct URL to fetch wiki summary
  url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
  
  # Make a gert request to fetch data
  response = rqt.get(url)
  
  # Check request data
  if response.status_code == 200:
    data = response.json()
    
    # Extract the Summary request from JSON
    summary = data["extract"]
    
    # Extract URL fo thumbnail if available
    image_url = data.get("thumbnail", {}).get("source")
    
    # Return the summary text and image URL
    return summary, image_url
  
  else:
    # Return an error message if fetching information has failed
    return "Failed to fetch information. Please try again later", None
  
#############################
# Save image from URL
#
#############################
def save_img_from_url(image_url, filename):
  # Gets the image URL
  response = rqt.get(image_url)
  
  # If success open a file and write the image to it
  if response.status_code == 200:
    with open(filename, "wb") as f:
      f.write(response.content)
    
    print(f"Image saved successfully as {filename}")
  else:
    print("Failed to fetch image")

#############################
# Save Summary from response
#
#############################
def save_summary(summary, filename):

  # If success open a file and write the image to it
  with open(filename, "w") as file:
    file.write(f"{summary}\n")
    print(f"Summary saved successfully as {filename}")


#############################
# Main()
#
#
#############################
def main():
  # Banner Text
  print("Weclome to the Wikipedia summary engine")
  
  # Topic data
  topic = input("Enter a topic that you want to learn about : ")
  
  # Get the summary
  summary, image_url = get_wiki_summary(topic)
  
  print("\nSummary")
  # Print the summary
  print(summary)
  filename = f"{topic.replace(' ', '_')}.txt"
  save_summary(summary, filename)
  
  # Prints the image from the summary
  if image_url:
    filename = f"{topic.replace(' ', '_')}.jpg"
    save_img_from_url(image_url, filename)
  else:
    # Print an error message
    print("\nNo image found")
  
    
    

#############################
# Call Main()
#
#############################

if __name__ == "__main__":
  main()
  
  
  