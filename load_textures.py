import sys
import json

def verifyTextures(path):

  f = open("textures/"+path+"/pack.json", 'r')
  
  try:
    data = json.load(f)
  except:
    print("\nERROR: No pack.json file found while loading the texture pack! If this is your texture pack, please create a new pack.json file or make sure your pack.json file is inside the textures folder and not a sub folder.")
    sys.exit()
  
  print("\nTexture pack loaded!")
  
  try:
    print(f"\nName: {data['name']}\nDescription: {data['description']}\nMade by {data['author']}")
    fontLocs = [data["fonts"]["font1"]]
    return fontLocs
  except:
    print("\nERROR: The pack.json file provided is incomplete/has typoes. Please verify the file contains name, description and author and check for typoes.")
    sys.exit()