# Scripts for the EHRI 2 Project


## extractAccessPoints.py

Script to extrat access points from EAD files. 
The input for the script is a folder with a set of EAD files inside. 
The output is a set of tables of access points of following tipes: Subject, Person, Corporate Body, Place and Creator. The tables will have the same name as the folder with the access point type as a suffix.

The script extract for each access point following parameters
1. String of the access point
2. Source of the access point in the CHI (if provided as @source attribute)
3. Authority file number of the access point in the CHI (if provided as @authfilenumber attribute)
4. Frequency of the access point in the provide dataset

**Usage**
$ python extractAccessPoints.py EAD_folder

**Requirements**
Python 3
