# Conda Environment Setup
I downlaoded the files manually and saved in: `~/Documents/PLUS_softwaredev_2025_01/repos/`
<img width="1035" alt="files-download" src="https://github.com/user-attachments/assets/8592bd9d-e55d-4c5a-99d7-d964e9059b71" />

# Creating Environment from v1 File
I used the command: `conda env create -f software_dev_v1.yml` and got errors.
<img width="1037" alt="error" src="https://github.com/user-attachments/assets/c47cc7b2-23c9-4095-a339-7fe76d197817" />


# Creating Environment from v2 File
I used the command: `conda env create -f software_dev_v2.yml.` I didn't get any error, and the packages were installed successfully.
<img width="1038" alt="env 2" src="https://github.com/user-attachments/assets/26eb9e7f-cfef-4653-aa85-04ca33b0504a" />


# Activating the Environment
I used the command: `conda activate software_dev_v2` to activate the environment.
<img width="1032" alt="conda-activated" src="https://github.com/user-attachments/assets/60ad2994-f2fb-4275-9a74-237cc9dd422b" />


# Checking the installed packages
I used the command: `conda list` to check the installed packages.
<img width="1033" alt="conda-activated-pkgs" src="https://github.com/user-attachments/assets/8dad91ef-8f0a-4553-a27c-ac4801e86e2c" />

# Summary
When using **software_dev_v1.yml**, I got an error related to incompatible or missing packages. So I used the **software_dev_v2.yml** file instead, which worked perfectly. The environment was recreated successfully using **software_dev_v2.yml**. All packages were installed and verified using **conda list**. Errors from **software_dev_v1.yml** were resolved by switching to version 2. :) 
