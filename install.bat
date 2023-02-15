mkdir build
pip -r requirements.txt
echo "Copying 'src/config.py' to 'build/config.pyw'"
copy src/config.py build/config.pyw
echo "Copying 'src/presence.py' to 'build/presence.pyw'"
copy src/presence.py build/presence.pyw
echo "Copying 'src/config.ui' to 'build/config.ui'"
copy src/config.ui build/config.ui
echo "Done!"
