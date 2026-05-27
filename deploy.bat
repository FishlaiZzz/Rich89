@echo off
chcp 950 >nul
title 天賦實戰班第89期黃金陣容網頁 - 一鍵部署工具

echo ==========================================================
echo       天賦實戰班第89期黃金陣容網頁 - 一鍵部署工具
echo ==========================================================
echo.
echo 正在偵測 Git 環境並準備部署專案至 GitHub 倉庫...
echo.

:: ================= 自動尋找 Git 執行檔路徑 =================
:: 如果環境變數中沒有 Git，這段會自動尋找常見安裝路徑
set "GIT_CMD=git"

if exist "C:\Program Files\Git\cmd\git.exe" (
    set "GIT_CMD=C:\Program Files\Git\cmd\git.exe"
) else if exist "C:\Program Files (x86)\Git\cmd\git.exe" (
    set "GIT_CMD=C:\Program Files\Git\cmd\git.exe"
) else if exist "%LocalAppData%\Programs\Git\cmd\git.exe" (
    set "GIT_CMD=%LocalAppData%\Programs\Git\cmd\git.exe"
)

:: 測試是否可執行 Git 指令
"%GIT_CMD%" --version >nul 2>&1
if errorlevel 1 goto error_no_git

:: 檢查是否設定了 Git 使用者資訊
"%GIT_CMD%" config user.email >nul 2>&1
if errorlevel 1 goto error_no_identity
:: =========================================================

:: 1. 初始化 Git (如果尚未初始化)
if not exist .git (
    echo [1/4] 正在初始化本地 Git 儲存庫...
    "%GIT_CMD%" init
) else (
    echo [1/4] 本地 Git 儲存庫已存在，跳過初始化。
)
echo.

:: 2. 設定 GitHub 遠端網址 (確保使用最新的 FishlaiZzz/Rich89)
echo [2/4] 正在設定遠端 GitHub 連結 (FishlaiZzz/Rich89)...
"%GIT_CMD%" remote remove origin >nul 2>&1
"%GIT_CMD%" remote add origin https://github.com/FishlaiZzz/Rich89.git
echo 遠端連結設定成功！
echo.

:: 3. 提交本地代碼
echo [3/4] 正在將代碼文件加入暫存區並提交變更...
"%GIT_CMD%" add .
"%GIT_CMD%" commit -m "deploy: update Rich89 talents parents webpage"
"%GIT_CMD%" branch -M main
echo 變更提交成功！
echo.

:: 4. 強制推送到 GitHub
echo [4/4] 正在推送代碼至 GitHub 遠端倉庫的 main 分支...
echo (注意：這會將網頁部署上傳，可能需要您在瀏覽器進行 GitHub 登入驗證)
echo.
"%GIT_CMD%" push -f origin main
if errorlevel 1 goto error_push
echo.

:success
echo ==========================================================
echo  [SUCCESS] 部署成功！
echo  請至您的 GitHub 檢查：https://github.com/FishlaiZzz/Rich89
echo  (若您已開啟 GitHub Pages，即可直接在線上瀏覽網頁了！)
echo ==========================================================
echo.
goto end

:error_push
echo ==========================================================
echo  [ERROR] 推送至 GitHub 失敗！
echo  請確認：
echo  1. 您的電腦是否已連接上網路？
echo  2. 您是否擁有此 GitHub 倉庫的權限？
echo  3. 您的 GitHub 登入驗證是否已成功？
echo ==========================================================
echo.
goto end

:error_no_git
echo ==========================================================
echo  [ERROR] 系統找不到 Git 程式！
echo  請確認您是否已安裝 Git，若剛安裝完畢，請重啟電腦後再試一次。
echo ==========================================================
echo.
goto end

:error_no_identity
echo ==========================================================
echo  [ERROR] 您尚未設定 Git 的使用者信箱與名稱！
echo  請在終端機中執行以下指令設定您的帳號：
echo.
echo  git config --global user.email "您的 GitHub 信箱"
echo  git config --global user.name "您的 GitHub 帳號"
echo ==========================================================
echo.
goto end

:end
pause
