# Styler_test
前置作業：
如果在電腦搜尋不到git bash，請去下載
網址：https://gitbook.tw/chapters/environment/install-git-in-windows.html 

1.創自己的分支  

<img width="300"  src="https://user-images.githubusercontent.com/43847735/109404843-f5c72a80-79a4-11eb-96f6-57256dfffe66.png"/>
2.在某處創建資料夾，右鍵點選git bash，輸入git clone 網址。(此處網址用右鍵paste，不然無法貼上) (網址在github的dode )

<p float="left">
<img width="300"  src="https://user-images.githubusercontent.com/43847735/109404996-b0a3f800-79a6-11eb-9f47-d1ebbfdb6333.png"/><img width="450"  src="https://user-images.githubusercontent.com/43847735/109405012-eea11c00-79a6-11eb-949a-f23431c03b07.png"/>
</p>

<img width="450"  src="https://user-images.githubusercontent.com/43847735/109409976-f4602700-79d1-11eb-9803-45081bf4390a.png"/>

3.if clone 成功，資料夾會有Styler_test的東西，此時在git bash 輸入cd ~/Desktop/你的資料夾/Styler_test(將位置移到Styler_test)


<img width="450"  src="https://user-images.githubusercontent.com/43847735/109410028-486b0b80-79d2-11eb-99d6-1945f6b24c71.png"/>

4.輸入git branch，查看目前的分支

5.輸入git checkout main，可查看main 裡面長怎樣，git checkout 你的分支，同理。
  
<img width="450"  src="https://user-images.githubusercontent.com/43847735/109405558-a71d8e80-79ac-11eb-8b1c-e04984bb297a.png"/>
6.可嘗試在自己的分支做一些事，之後在upload files到github (記得切換成你要的分支，然後點選add file 裡的upload files)

<img width="450"  src="https://user-images.githubusercontent.com/43847735/109410563-a0a40c80-79d6-11eb-8c44-b3ad1e3cbe0b.png"/>

藉由切換不同branch ，同個檔案裡的東西可以不同!

<img width="450"  src="https://user-images.githubusercontent.com/43847735/109410833-c92d0600-79d8-11eb-9939-aab150378da1.png"/>

<img width="450"  src="https://user-images.githubusercontent.com/43847735/109410850-fd082b80-79d8-11eb-9f0f-d36909fa8dde.png"/>

7.git pull origin main，將github上新的東西載至本機端做更新

8.git log ，可察看紀錄; git checkout 版本名，可切換版本

  版本控制：允許你將檔案復原到之前的狀態、將整個專案復原到先前的狀態。
  舉例：首先輸入git log，將列出所有歷史紀錄，由上而下是新到舊的的紀錄，可藉由按鍵盤的上下瀏覽紀錄。按q將退出歷史列表。
        輸入git checkout e5a4f12f7cca8b55b56dfa55a567b5caab29277a，再看資料夾，會發現50%_singlepage_ver1.ipynb當時還沒改名。

<img width="450"  src="https://user-images.githubusercontent.com/43847735/110202396-2de9d400-7ea3-11eb-97da-89105207768f.png"/>
<img width="450"  src="https://user-images.githubusercontent.com/43847735/110202411-4eb22980-7ea3-11eb-80dd-9e8642011f32.png"/>

小提醒：

在git bash 上遇到奇怪的東西時 ，按 `q` 或`:q!` ，通常可以解決哈哈

放棄本地修改，強制從github更新：git reset --hard origin/你要的分支 (e.g. git reset --hard origin/main )

## 參考資料：
[GIT101 心得/筆記] GitHub 操作 -push , pull, clone , fork
https://medium.com/@brad61517/git101-%E5%BF%83%E5%BE%97-%E7%AD%86%E8%A8%98-github-%E6%93%8D%E4%BD%9C-push-pull-clone-fork-a414d4af64be 

[Git教學] 寫給 Git 初學者的入門 4 步驟
https://www.maxlist.xyz/2018/11/02/git_tutorial/

github基本教學 - 從無到有
https://www.youtube.com/watch?v=py3n6gF5Y00&list=LL&index=2

Git 版本管理 #7 分支 (branch) (教学 教程 tutorial)
https://www.youtube.com/watch?v=68CMwz3wMRE&list=LL&index=1

[第一週]版本控制與 Git 基本指令
https://miahsuwork.medium.com/%E7%AC%AC%E4%B8%80%E9%80%B1-%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6%E8%88%87-git-%E5%9F%BA%E6%9C%AC%E6%8C%87%E4%BB%A4-fa3c4ba286a2

