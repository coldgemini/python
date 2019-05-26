import os

# basic setup
os.system("mkdir -p ~/Tmp")
os.system("cd ~/Tmp; pwd")
# install apps
neteasemusic = 'http://d1.music.126.net/dmusic/netease-cloud-music_1.2.1_amd64_ubuntu_20190428.deb'
os.chdir('/home/xiang/Downloads')
# os.system("wget " + neteasemusic)
os.system("sudo gdebi --non-interactive netease-*.deb")