import glob
from PyQt6.QtWidgets import QFileDialog, QWidget, QLineEdit
from json_to_csv import exportCSV

def input_path_dialog(parent: QWidget, connected_line_edit: QLineEdit) -> None:
    input_path = str(
        QFileDialog.getExistingDirectory(parent, "Select input Directory", "./")
    )
    connected_line_edit.setText(input_path)
    
def output_path_dialog(parent: QWidget, connected_line_edit: QLineEdit) -> None:
    output_path = str(
        QFileDialog.getExistingDirectory(parent, "Select Output Directory", "./")
    )
    connected_line_edit.setText(output_path)
    
def execute_submit(input_path: str, output_path: str) -> None:
    print("Start processing")
    
    file_list = glob.glob(f'{input_path}/*.json')
    
    for i in range(len(file_list)):
        exportCSV(file_list[i], output_path, str(i+1))
        print("Json " + str(i+1) + " process complete.")
        
    