import os
import xml.etree.ElementTree as ET
import argparse

parser = argparse.ArgumentParser(description="get_ip.py -d C:\\project\\ -o getip.txt")
parser.add_argument('-d', '--directory', type=str, required=True, help='nessus_目錄路徑')
parser.add_argument('-o', '--output', type=str, default='getscanip.txt', help='輸出檔案名稱預設為:getscanip.txt')

# 解析參數
args = parser.parse_args()


# 定義目錄路徑
directory = args.directory

all_ips = []
output_file = args.directory + "\\" + args.output # 定義輸出檔案
#output_file2 = "output_ips6.txt"  # 定義輸出檔案

# 打開文件寫入結果
with open(output_file, "w") as outfile:
    # 遍歷目錄中的所有 .nessus 檔案
    for filename in os.listdir(directory):
        if filename.endswith(".nessus"):  # 只處理 .nessus 檔案
            file_path = os.path.join(directory, filename)
            print(f"正在處理文件: {file_path}")

            # 解析 XML 文件
            try:
                tree = ET.parse(file_path)  # 打開並解析檔案
                root = tree.getroot()  # 取得 XML 根節點

                # 提取 IP 位址
                file_ips = []  # 儲存當前檔案的 IP 位址
                for report_host in root.findall(".//ReportHost"):
                    ip = report_host.get("name")
                    if ip:
                        file_ips.append(ip)
                        all_ips.append(ip)

                # 顯示當前檔案的 IP 數量
                print(f" {filename} 取得了 {len(file_ips)} 個 IP 位址")

                # 將當前檔案的 IP 位址寫入輸出檔案
                outfile.write("\n".join(file_ips) + "\n")

            except ET.ParseError as e:
                print(f"解析失敗: {file_path}, 錯誤: {e}")
            except Exception as e:
                print(f"處理檔案 {file_path} 時發生未知錯誤：{e}")

# 顯示所有取得 IP 位址的總數
print(f"總共取得 IP 位址數量: {len(all_ips)}")
'''
# 將所有提取的 IP 地址寫入文件
with open(output_file2, "w") as outfile2:
    outfile2.write("===== 匯總結果 =====\n")
    outfile2.write(f"總共提取的 IP 地址數量: {len(all_ips)}\n")
    outfile2.write("\n".join(all_ips) + "\n")
'''
# 最終提示
print(f"所有取得 IP 已存到檔案: {output_file}")