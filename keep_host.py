import os
import xml.etree.ElementTree as ET
import argparse


parser = argparse.ArgumentParser(description="keep_host.py -d C:\\project\\ -od C:\\new_project\\ -i xxxx.txt")
parser.add_argument('-d', '--directory', type=str, required=True, help='nessus_目錄路徑')
parser.add_argument('-od', '--odirectory', type=str, required=True, help='輸出新nessus_目錄路徑')
parser.add_argument('-i', '--input', type=str, required=True, help='保留的 IP 檔案')

# 解析參數
args = parser.parse_args()


# 定義目錄路徑
directory = args.directory  # 請將此替換為實際的目錄路徑
directory_output = args.odirectory

# 讀取要保留的 IP 位址列表（從檔案中讀取）
ips_to_keep = []
with open( args.input , "r") as f:
    ips_to_keep = [line.strip() for line in f.readlines()]

# 顯示讀取的 IP 位址列表
print(f"需要保留的 IP 位址：{ips_to_keep}")

# 遍歷目錄中的所有 .nessus 檔案
for filename in os.listdir(directory):
    if filename.endswith(".nessus"):  # 只處理 .nessus 檔案
        file_path = os.path.join(directory, filename)
        output_file_path = os.path.join(directory_output, 'new_' + filename)
        
        print(f"正在處理檔案: {file_path}")

        # 解析 XML 檔案
        try:
            tree = ET.parse(file_path)  # 打開並解析檔案
            root = tree.getroot()  # 取得 XML 根節點
            
            # 找到 Report 節點
            report_node = root.find(".//Report")
            if report_node is None:
                print(f"錯誤：未找到 Report 節點 in {file_path}")
                continue

            # 收集需要刪除的 ReportHost 節點
            hosts_to_remove = []
            for report_host in report_node.findall("ReportHost"):
                ip = report_host.get("name")
                
                print(f"當前 IP: {ip}")
                print(f"是否在保留列表中: {ip in ips_to_keep}")
                
                if ip not in ips_to_keep:
                    hosts_to_remove.append(report_host)

            # 刪除不需要的節點
            if hosts_to_remove:
                print(f"將刪除 {len(hosts_to_remove)} 個 IP")
                for host in hosts_to_remove:
                    report_node.remove(host)
                    print(f"已刪除 IP 位址: {host.get('name')}")
            else:
                print("沒有要刪除的 IP")

            # 保存更新後的 XML 檔案到新目錄
            tree.write(output_file_path, encoding="utf-8", xml_declaration=True)
            print(f"已更新並保存檔案: {output_file_path}")

        except ET.ParseError as e:
            print(f"解析失敗: {file_path}, 錯誤: {e}")
        except Exception as e:
            print(f"處理檔案 {file_path} 時發生未知錯誤：{e}")

print("篩選完成")