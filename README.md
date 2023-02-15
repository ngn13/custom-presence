# Custom Presence
*Simple python script for custom discord presence*

## Installation
### Windows
- Download the repo as ZIP
- Extract from the ZIP
- Run `install.bat`
- Files will be copied into the `build` folder

### Linux
- Clone the repo
- Run `install.sh`
- Files will copied into `/usr/bin`, which is probably
in your `PATH`, so you can launch them from the terminal

## Usage
First you will need to create an application in the [developer portal](https://discord.com/developers/applications/)
name it whatever you want, and copy the client ID.

You can upload images in the `rich presence > art assets` section

After doing that, edit the presence config with `cp-cfg`.
Make sure you paste the client ID into the `Client ID` section.
You can use the images that you uploaded earlier in the `Large Image Name`
and `Small Image Name` section, leave them empty if you want no images.

If you are using the buttons, make sure to provide a valid URL that starts
with `http://` or `https://`

To start up the presence, run `cp-run`

### Troubleshooting
If you can't see your presence:
1. Make sure that client ID is valid.
2. Make sure that `cp-run` is running
3. Make sure that you have `Display current activity as status message` set to `ON` in your discord settings. 
You can find it in: `User Settings > Activity Privacy > Activity Status`

## License
See LICENSE.txt for more information
