@echo off
set "output_dir=.build_and_dist/"
set "icon_dir=docs/icon/delethon.ico"
set "package_name=delethon"

@echo on
cd %~dp0
cd ..\
pip install -r requirements.txt
nuitka "%package_name%" --standalone --output-dir %output_dir% --show-progress --show-scons --show-modules --windows-icon=%icon_dir% --assume-yes-for-downloads