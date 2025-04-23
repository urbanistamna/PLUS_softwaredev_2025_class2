# Conda Environment Setup
My files were manually downlaoded and saved in: `~/Documents/PLUS_softwaredev_2025_01/repos/`
![files-download](files-download.png)

# Creating Environment from v1 File
I used the command: conda env create -f software_dev_v1.yml and got errors.
![error](error.png)

# Creating Environment from v2 File
I used the command: conda env create -f software_dev_v2.yml I didn't get any error and the packages were installed successfully.
![env 2](env 2.png)

# Activating the Environment
I used command: conda activate software_dev_v2 to activate the environment.
![conda-activated](conda-activated.png)

# Checking the installed packages
I used command: conda list to check the installed pakcages.
![conda-activated-pkgs](cconda-activated-pkgs.png)

# Summary
When using software_dev_v1.yml, I got an error related to incompatible or missing packages. So I used the software_dev_v2.yml file instead, which worked perfectly. The environment was recreated successfully using software_dev_v2.yml. All packages were installed and verified using conda list. Errors from software_dev_v1.yml were resolved by switching to version 2. :) 