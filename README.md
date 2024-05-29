# SFU Campus Time Estimation
This project estimates travel time between the Burnaby and Vancouver campuses of Simon Fraser University (SFU) using the Transit API.

Overview
We aimed to estimate travel time between the SFU Burnaby and Vancouver campuses. However, due to the lack of an appropriate dataset, we utilized a statistical method to overcome this obstacle.

Dependencies
Operating System: Windows
Install the necessary packages using pip:

bash
Copy code
pip install beautifulsoup4
pip install requests
pip install lxml
pip install Pillow
Installation
To install the SFU-campus-time-estimation package, use the following command:

bash
Copy code
pip install beautifulsoup4 requests lxml Pillow
Usage
Here's a basic example of how to use the translink_sfu module to get transit data and estimated time to leave:

python
Copy code
import translink_sfu

stop_bay1 = 51861 # SFU Transit Exchange @ Bay 1

# Get data from TransLink API
data = translink_sfu.get_data(stop_bay1)

# Estimate time to leave
estimated_time = translink_sfu.time_to_leave(data)

print(estimated_time)
If you run main.py, you can see the estimation results.

bash
Copy code
python main.py
Files
main.py: The main script to run the project.
translink_sfu.py: Contains functions to interact with the Transit API and process data.
gitignore.txt: Specifies intentionally untracked files to ignore.
Additional Information
The statistical methods applied in this project help to provide more accurate travel time estimations despite the initial data limitations. Future improvements could involve integrating more comprehensive datasets and refining the statistical models.
