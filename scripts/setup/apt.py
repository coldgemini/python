import os

# install basics
os.system("sudo apt install -y git feh wget axel curl gdebi vim-gtk htop tree ncdu aria2 timeshift fcitx-table-wbpy xclip")
# os.system("sudo apt install -y vim-airline vim-airline-themes ")
os.system("sudo apt install -y vlc mpv")
os.system("sudo apt install -y zeal")
os.system("sudo apt install python python-pip")
os.system("sudo pip install virtualenvwrapper virtualenv")
os.system("sudo apt install -y i3 fonts-font-awesome rofi volumeicon-alsa")
os.system("sudo apt install -y fasd")
os.system("sudo apt install -y sox libsox-fmt-all")
os.system("sudo apt install -y alsa-utils pulseaudio")

os.system("git config --global user.email 'coldgemini@foxmail.com'")
os.system("git config --global user.name 'coldgemini'")
# editing .bashrc.user
# basic setup
os.system("mkdir -p ~/.Env")
os.system("cd ~/.Env; git clone git@github.com:coldgemini/ubuntu-settings.git -b thinkpad")
os.system("cd ~/.Env/ubuntu-settings/configs/link-files; bash setuplinks.sh")
os.system("git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim")
# in VIM :PluginInstall
# config gnome-terminal shotcut

# languages
sogou = 'http://cdn2.ime.sogou.com/dl/index/1524572264/sogoupinyin_2.2.0.0108_amd64.deb'
os.system("wget " + sogou)
os.system("sudo gdebi --non-interactive sogoupinyin*.deb")
# bash im-config choose fcitx
# bash fcitx-configtools

# setup proxy
os.system("sudo apt install -y polipo")
os.system("mkdir -p ~/Dev")
os.chdir('/home/xiang/Dev')
os.system("git clone git@github.com:ShadowsocksR-Live/shadowsocksr.git")
os.system("cp -r shadowsocksr /home/xiang/Apps")

# install apps
neteasemusic = 'http://d1.music.126.net/dmusic/netease-cloud-music_1.2.1_amd64_ubuntu_20190428.deb'
os.chdir('/home/xiang/Downloads')
os.system("wget " + neteasemusic)
os.system("sudo gdebi --non-interactive netease-*.deb")
virtualbox = 'https://download.virtualbox.org/virtualbox/6.0.8/virtualbox-6.0_6.0.8-130520~Ubuntu~bionic_amd64.deb'
os.system("wget " + virtualbox)
os.system("sudo gdebi --non-interactive virtualbox-*.deb")
chrome = 'wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'
os.system("wget " + chrome)
os.system("sudo gdebi --non-interactive google-chrome-*.deb")
pycharm = 'https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=linux&code=PCC'
os.system("wget " + pycharm)
os.system("tar xvf pycharm-community*.tar.gz")
os.system("rm pycharm-community*.tar.gz")
os.system("mv pycharm-community-* /home/xiang/Apps")
os.chdir('/home/xiang/Apps')
os.system("ln -s pycharm-community*/bin/pycharm.sh")
os.chdir('/home/xiang/Downloads')
zotero = 'https://download.zotero.org/client/release/5.0.66/Zotero-5.0.66_linux-x86_64.tar.bz2'
os.system("wget " + zotero)
os.system("tar xvf Zotero*.tar.gz")
os.system("rm Zotero*.tar.gz")
os.system("mv Zotero* /home/xiang/Apps")
os.chdir('/home/xiang/Apps')
os.system("ln -s Zotero_linux-x86_64/zotero")
os.chdir('/home/xiang/Downloads')
foxit = 'https://www.foxitsoftware.com/downloads/thanks.php?product=Foxit-Reader&platform=Linux-64-bit&version=2.4.4.0911&package_type=run&language=English'
os.system("wget " + foxit)
os.system("tar xvf Foxit*.tar.gz")
os.system("rm Foxit*.tar.gz")
stacer = 'https://github.com/oguzhaninan/Stacer/releases/download/v1.1.0/Stacer-1.1.0-x64.AppImage'
os.system("wget " + stacer)
os.system("mv Stacer*AppImage /home/xiang/Apps")
os.system("chmod +x /home/xiang/Apps/Stacer*AppImage")
milk = 'https://www.rememberthemilk.com/download/linux/debian/pool/main/r/rememberthemilk/rememberthemilk_1.1.12_amd64.deb'
os.system("wget " + milk)
os.system("sudo gdebi --non-interactive rememberthemilk*.deb")
simplenote = 'https://github.com/Automattic/simplenote-electron/releases/download/v1.5.0/Simplenote-linux-1.5.0-x86_64.AppImage'
os.system("wget " + simplenote)
os.system("mv Simplenote*AppImage /home/xiang/Apps")
os.system("chmod +x /home/xiang/Apps/Simplenote*AppImage")
gitkraken = 'https://release.gitkraken.com/linux/gitkraken-amd64.deb'
os.system("wget " + gitkraken)
os.system("sudo gdebi --non-interactive gitkraken*.deb")

# flatpak
os.system("flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo")
