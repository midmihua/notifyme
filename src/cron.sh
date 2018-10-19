#!/usr/bin/env bash

######## Help ########
#
# /etc/crontab
# * * * * * /actual/path/to/file/cron.sh
#
# crontab -u user_name -e
# crontab -u user_name -l
# crontab -u user_name -r
#
# service cron status
#
######################

# START_POINT is a real path to the src folder on a specific environment (local or production)
# It should be something like this: START_POINT=/home/username/Documents/www/notifyme/src/
START_POINT=/provide/actual/path/to/src_folder/

# Path to activate virtual env
VENV_ACTIVATE=${START_POINT}../venv/bin/activate


# Running the process

# 1. Go to src folder
cd ${START_POINT}
# 2. Activate virtual env
source ${VENV_ACTIVATE}
# 3. Run main process file
python run.py
# 4. Deactivate virtual env
deactivate
