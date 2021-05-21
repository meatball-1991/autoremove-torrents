# flexget-autoremove-torrents
Automatically remove torrents for Flexget  
修改jerrymakesjelly/autoremove-torrents为flexget的plugin在flexget内使用  
  

使用说明:  
config设置参考config-template.yml

与原作者不同之处：  
1. 客户端只支持qbittorrent
2. qbittorrent host port等设置做了修改,具体参考.yml
3. strategy 禁用 freespace (remotefreespace可用),原因是freespace在flexget内提示缺dependencies  
4. 一个task只能设置一个autoremove的任务
