@echo off
set dist_dir="..\.build_and_dist\pyinstaller.build"

@echo on
cd %~dp0
pyinstaller pyinstaller_build.spec --clean --distpath %dist_dir% --workpath %dist_dir%
pause