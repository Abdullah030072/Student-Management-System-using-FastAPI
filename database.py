import csv
import os

from config import FILE_NAME


# ==========================================
# Create CSV File
# ==========================================

def create_file():

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "ID",
                "Name",
                "Age",
                "Course",
                "GPA"
            ])