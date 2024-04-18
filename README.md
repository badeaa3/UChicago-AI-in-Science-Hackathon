# Instructions for initial setup
```
git clone https://github.com/badeaa3/UChicago-AI-in-Science-Hackathon.git
cd UChicago-AI-in-Science-Hackathon
source setup.sh
```

Now you should have a virtual environment folder called hackathon. You can log onto the interactive now
```
sinteractive --account=pi-dfreedman -p schmidt-gpu --gres=gpu:1 --qos=schmidt --time 2:00:00 # works now
source setup.sh # you should be put into the UChicago-AI-in-Science-Hackathon repo automatically so the source should work
```

