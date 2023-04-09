# this is an example code for paper use

import os
import shutil
import pydicom
from pathlib import Path


def create_dir(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)


PathDicom = '.......' # your dicom file path

NewPathDicom = '.......' # your new storage file path

dirs = os.listdir(PathDicom) # read dicom file

for dir in dirs:

    # select information(AcquisitionDate, PatientID, ...) from DICOM header
    dicomdate = pydicom.read_file(os.path.join(PathDicom, dir)).AcquisitionDate
    patientid = pydicom.read_file(os.path.join(PathDicom, dir)).PatientID

    # combine new path for DICOM slice
    newPath = os.path.join(NewPathDicom,patientid,dicomdate)

    # if new path doesn't exist, create this folder
    if Path(newPath).exists():
        pass
    else:
        create_dir(newPath)
        # move to new file slice by slice
        shutil.move(
            dir, newPath, copy_function = shutil.copytree)  # success
