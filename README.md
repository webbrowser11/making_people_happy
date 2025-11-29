# making_people_ahppy
A quick way to make people happy, if you know what you are doing.

# Things You Need to Know
Before running anything, make sure you update all usernames, passwords, and system paths in the files. Double-check everything so the system actually points to your setup.

# Setup Guide

### 1. Download the files
Download all the Python scripts onto a Linux machine and place them in a folder named `programs`.

**Important:** Only put the `.py` files inside `programs` — nothing else.

### 2. Install Python
Download and install Python from the official website:  
https://www.python.org/downloads/

### 3. Place the startup script
Download `start_system.sh` into the folder *above* the `programs` directory.  
Example:
- Python scripts: `/home/youruser/programs/`
- Startup script: `/home/youruser/start_system.sh`

### 4. Create a virtual environment
From inside the folder with your Python scripts:

```bash
py -m venv venv
```

### 5. Install ScratchAttach
Inside the venv, install the library:

```bash
py -m pip install scratchattach
```

### 6. Run the system
Navigate to the directory where `start_system.sh` is located and run:
```bash
./start_system.sh
```
