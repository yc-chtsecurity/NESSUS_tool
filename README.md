
### get_ip.py

掃描整個網段沒有 IP 清單時，可以使用該工具幫忙抓取 IP 

範例:
```
    get_ip.py -d C:\\project\\ -o getip.txt
```
參數資訊:

```
    -d: 取得該目錄下所有 .nessus 檔案掃描到的 IP 
    -o: 將取得的 IP 資訊輸出到該檔案
```
### keep_host.py

需要取得特定 IP 的 .nessus 檔案，可以透過該程式幫忙快速篩選

範例:
```
     keep_host.py -d C:\\project\\ -od C:\\new_project\\ -i xxxx.txt
```
參數資訊:
```
    -d: 取得該目錄下所有 .nessus 檔案進行分析 
    -od: 將修改後的 .nessus 檔案儲存到該目錄下，所有檔案名稱前面會加上 new_ 前綴
    -i: 需要篩選的 IP 資訊，新的 .nessus 檔案會保留該檔案內的 IP 資訊
        檔案格式:   
                  192.168.1.1
                  192.168.2.2
                  192.168.3.3
```
