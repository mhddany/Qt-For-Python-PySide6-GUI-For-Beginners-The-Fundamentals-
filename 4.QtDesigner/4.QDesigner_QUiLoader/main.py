import sys
import os
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader() #Set up a loader object

app = QtWidgets.QApplication(sys.argv)

# Get current working directory
cwd = os.getcwd()  # This is the folder where you run 'python main.py'

# Build the path to the .ui file safely, using os.path.join
ui_file = os.path.join(cwd,"4.QtDesigner",  "4.QDesigner_QUiLoader", "widget.ui")

# Check if the file exists
if not os.path.exists(ui_file):
    raise FileNotFoundError(f"UI file not found: {ui_file}")
# Load UI
window = loader.load(ui_file)

def do_something() :
    print(window.full_name_line_edit.text(),"is a ", window.occupation_line_edit.text())

#Changing the properties in the form
window.setWindowTitle("User data")

#Accessing widgets in the form
window.submit_button.clicked.connect(do_something)
window.show()
app.exec()