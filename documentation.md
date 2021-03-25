# Documentation

## Installing Python

### WSL - Ubuntu
1. Open a **command prompt** and run the following command:
```
sudo apt update && upgrade
```
2. Once finished, also run the following command:
```
sudo apt install python3 python3-pip ipython3
```

### Windows 10

#### Method 1 - Python.org
1. Download Python 3.8 [Here](https://www.python.org/downloads/release/python-388/)
2. Scroll to the bottom of the page and choose the **Windows Installer** most suitable for your system (x32/x64)
4. Once the installer is downloaded, open it and make sure **"Install launcher for all users"** and **"Add Python 3.8 to PATH"** is checked and press **Install Now**
5. During the installation, accept any Windows prompts that comes up.
6. Once the installation finishes you've successfully installed Python and can close the window.

#### Method 2 - Microsoft Store
1. Open the *Microsoft Store* application
2. In the search bar, search for *Python 3.8* and select the *Python 3.8* application from *Python Software Foundation*
3. Once on the application page, click **Get**
4. If the program doesn't install automatically, click **Install** once the download finishes.

## Creating a virtual environment
Before proceeding, make sure you've followed the steps in [**Installing Python**](#Installing-Python).

### Installing virtualenv
1. Open a **command prompt** and type the following:
```
pip3 install virtualenv
```
or
```
pip install virtualenv
```
2. Once finished, virtualenv should now be installed on your system.

**Note:** for WSL you may need to type sudo before pip to get root permissions.

### Creating the virtual environment
1. Open a **command prompt** in the repository directory.
2. To create a virtual environment, type the following command:
```
virtualenv venv
```
3. Once finished you should now have created a virtual environment.

### Starting the virtual environment
1. Open a **command prompt** in the repository directory.
2. To start the environment, type the following command:
```
source venv/bin/activate
```
3. To stop the environment simply type:
```
deactivate
```

### Installing dependencies
1. Open a **command prompt** in the repository directory.
2. Start your virtual environment.
3. Type the following command:
```
pip3 install -r requirements.txt
```
or
```
pip install -r requirements.txt
```
4. Once all installations are done you're finished.

### Adding dependencies
1. Open a **command prompt** in the repository directory.
2. Start your virtual environment.
3. Type the following command:
```
pip3 freeze > requirements.txt
```
or
```
pip freeze > requirements.txt
```
4. After a few seconds it should be done.

## Creating a Jupyter Notebook
Before proceeding make sure you've followed the steps in [**Creating a virtual environment**](#Creating-a-virtual-environment)

1. Open a **command prompt** in the repository directory.
2. Start your virtual environment.
3. Type the following command:
```
Jupyter notebook
```
3. The notebook should now be available on http://localhost:8888/ along with a token ID listed in the prompt.
4. Once finished you should now have a Jupyter Notebook running on your system.
