import os
"""
os.system("wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz")
os.system("tar -xvzf geckodriver*")
os.system("chmod +x geckodriver")
way = input("Extracted file path : ")
os.system("export PATH=$PATH:/{}".format(way))
"""
print("""
1. Geckodriver
2. Chromedriver
""")
cho = int(
    input("Option : ")
)
if cho == 1:

    ## Geckodriver
    os.system("wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz")
    os.system("sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.23.0-linux64.tar.gz -O > /usr/bin/geckodriver'")
    os.system("sudo chmod +x /usr/bin/geckodriver")
    os.system("rm geckodriver-v0.23.0-linux64.tar.gz")
elif cho == 2:
    
    ## Chromedriver
    os.system("wget https://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip")
    os.system("unzip chromedriver_linux64.zip")
    os.system("sudo chmod +x chromedriver")
    os.system("sudo mv chromedriver /usr/bin/")
    os.system("rm chromedriver_linux64.zip")

else:
    print("Select 1 or 2")