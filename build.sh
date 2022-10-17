#! /bin/bash
conda init zsh
conda activate pyside
pip install pyinstaller

pyinstaller main.spec
cp settings.json dist/main/

mkdir -p dist/main/gui
cp -r gui/themes/ dist/main/gui/themes
cp -r gui/images dist/main/gui/images
cp -r img dist/main/

mkdir dist/main/gui/fastfusion
mkdir dist/main/data
mkdir dist/main/moving_object_detection
mkdir dist/main/history_data
touch dist/main/moving_object_detection/process_rate.txt

echo "#########################################################"
echo "#########################################################"
echo "#########################################################"
echo "build finish please copy moving_object_detection and it's config to dist/main/moving_object_detection"
echo "please copy fastfusion and camera calib file to dist/main/fastfusion"

