#! /bin/bash

#This shell script will creat an executable for our project
#Ensure all python dependencies are install before running this script
#------NOTE------
#For some reason, numpy version 1.19.4 does not work well with pyinstaller
#only version 1.19.3 will work.

#creating executable
"pyinstaller" --onefile -i "media/dna.ico" --name="Sequence Analyzer" --noconsole main.py

#copying Logical Clock executable to project root
cp "dist/Sequence Analyzer" .

#removing Logical Clock.spec file created by pyinstaller
rm "Sequence Analyzer.spec"

#removing build folder created by pyinstaller
rm -r build

#removing dist folder created by pyinstaller
rm -r dist
