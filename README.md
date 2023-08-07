<div align="center">
  <h1>🎨 Discord Custom Presence Script</h1>
  <img src="https://img.shields.io/github/languages/count/ngn13/custom-presence">
  <img src="https://img.shields.io/github/directory-file-count/ngn13/custom-presence">
  <img src="https://img.shields.io/github/languages/code-size/ngn13/custom-presence">
  <br>
  <i>Simple python script for custom discord presence</i>
</div>

<br>

### 📀  Installation
- Make sure you have python version 3 installed:
```bash
which python
python --version
```
If you don't have it installed, you can install it
with your distribution's package manager
- Go to a temporary directory and clone the repo
```bash
cd /tmp
git clone https://github.com/ngn13/custom-presence.git
cd custom-presence
```
- Install the requirements
```bash
pip -r requirements.txt
```
- Run the install script
```bash
chmod +x install.sh
./install.sh
```
- Files will be copied into `/usr/bin`, which is probably
in your `PATH`, so you can launch the scripts from the terminal
```bash
which cp-cfg
which cp-run
```
- Then you can delete the directory
```bash
cd .. && rm -rf custom-presence
```

<br>

### 🚀  Usage
First you will need to create an application in the [developer portal](https://discord.com/developers/applications/)
name it whatever you want, and copy the client ID.

You can upload images in the `Rich Presence > Art Assets` section

After doing that, edit the presence config with `cp-cfg`.
Make sure you paste the client ID into the `Client ID` section.
You can use the images that you uploaded earlier in the `Large Image Name`
and `Small Image Name` section, leave them empty if you want no images.

If you are using the buttons, make sure to provide a valid URL that starts
with `http://` or `https://`

To start up the presence, run `cp-run`

<br>

### 🔎  Troubleshooting
If you can't see your presence:
- Make sure that client ID is valid.
- Make sure that `cp-run` is running
- Make sure that you have `Display current activity as status message` set to **ON** in your discord settings. 
You can find this setting in: `User Settings > Activity Privacy > Activity Status`
- If you still can't see your presence please create an [issue](https://github.com/ngn13/custom-presence/issues)

<br>
