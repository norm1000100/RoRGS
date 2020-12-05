#! /bin/bash

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
