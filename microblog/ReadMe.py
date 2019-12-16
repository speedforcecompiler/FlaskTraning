Tutorial link : 

	- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

Virtual env : 
	
	- In Python 3.7.3 you have to create virtual environments to store your project's Dependencies.
	- The virtual environment is your project specific environment that only refers to your projects directory.
	- In this way the Global installation of Python is not affected
	- Other Projects using some other versions are also not affected

	Commands :

	- Installing virtualenv
		$ pip install virtualenv

	- Make the virtual environment
		$ virtualenv venv
		- The above command will make the virtual environment in the project directory under the 'venv' directory or any other specified directory.

	- Activate the Virtual Environment
		$ venv\Scripts\activate
		- You need to activate the virtual environment so that any installation that you make go into this environment and not hamper the Global Environment
		- Now any installation will go into this environment
		- When you activate a virtual environment, the configuration of your terminal session is modified so that the Python interpreter stored inside it is the one that is invoked when you type python. Also, the terminal prompt is modified to include the name of the activated virtual environment. The changes made to your terminal session are all temporary and private to that session, so they will not persist when you close the terminal window. If you work with multiple terminal windows open at the same time, it is perfectly fine to have different virtual environments activated on each one.

__init__.py :

	- this file indicated that the directory is a package.
	