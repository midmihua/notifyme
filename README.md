**How to setup the very basic configuration**

- `Git clone` project to local dir
- Go to the root folder of the project (`notifyme`)
- Create new virtualenv (`virtualenv venv`)
- Activate venv (`source venv/bin/activate`)
- Execute `pip install -r requirements.txt` to install all necessary libs
- Execute `pip freeze` and verify if the libs are installed
- Open `src/config/live.py` file
- Provide valid credentials to communicate with your Telegram Bot

`Telegram section: TOKEN = 'provide-token', CHAT_ID = 'provide-chat-id'`

- Go to `src` folder, there should be **run.py** file
- Execute command `python run.py`
- There should be the following debug info in the terminal:

`(venv) mypc@UD12345:~/Documents/pycharm/projects/notifyme/src$ python run.py`
`{'search_by': 1, 'url': 'https://api.etherscan.io/api?module=account&action=balance&address=blablaxxxxx', 'name': 'balance', 'param': 'result'}`
`{'_address': 'blablaxxxxx', 'url': 'https://etherscan.io/readContract?a=blablaxxxxx&v=blablaxxxxx', 'search_by': 2, 'name': 'userDividendsWei', 'delay': 3}`
`{'userDividendsWei': {'result': '99999993220338983'}, 'balance': {'result': '888888444125868886170'}}`

- Test message should be sent to your Telegram Bot

**_Google how to create personal Telegram Bot and get its TOKEN and CHAT_ID_**

Some links:

- New bot and its TOKEN: https://core.telegram.org/bots
- Chat_Id: https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id

**How to setup cron job execution** 

- Find the `cron.sh` file in the `src` folder
- Edit it according to its internal comments
- Execute `chmod +x cron.sh` command in terminal to make the file executable
- To open crontab file to edit it, execute `crontab -u user_name -e` command
- Add specific config to run the cron.sh file as a background process. For instance, to run the *.sh file every minute, add line: `* * * * * /actual/path/to/the/cron.sh`