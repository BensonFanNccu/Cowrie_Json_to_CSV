import csv
import json

def exportCSV(file_path: str, export_path: str, order: str) -> None:
    with open(file_path, 'r', encoding = 'utf-8') as f:
        file = [json.loads(line.strip()) for line in f.readlines()]
    
        keys = set()
        for item in file:
            if(item != "eventid" and item != "src_ip" and item != "dst_ip"):
                keys.update(item.keys())
                
        fields = ["eventid"] + ["src_ip"] + ["dst_ip"] + [key for key in keys]
        export_path = export_path + "/output" + order + ".csv"
        
        
        with open(export_path, 'w', newline='', encoding = 'utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fields)
            writer.writeheader()
        
            for item in file:
                writer.writerow(item)
            
            
        