@echo off
REM 搜索包含 "pycache" 的文件夹脚本
REM 用法: 将此脚本放在要搜索的目录中双击运行

setlocal enabledelayedexpansion

# 停止所有正在运行的coverage进程
pkill -f "coverage run" 2>/dev/null

# 删除数据文件
python coverage erase

# 删除报告文件
rm htmlcov/ coverage.xml coverage.json .coverage.*

# 删除Python缓存文件夹
set "search_dir=%~dp0"
set "output_file=pycache_folders.txt"

echo searching: %search_dir%
echo search "pycache"  ing...
echo.

REM 清空或创建输出文件
echo Pycache list > "%output_file%"
echo ================== >> "%output_file%"
echo. >> "%output_file%"

set count=0

REM 使用 dir 命令递归搜索所有目录
for /f "delims=" %%d in ('dir /s /b /ad "%search_dir%"') do (
    set "folder_name=%%~nxd"
    
    REM 检查文件夹名是否包含 "pycache"
    echo !folder_name! | findstr /i "pycache" >nul
    if !errorlevel! equ 0 (
        REM 找到匹配项
        set /a count+=1
        echo !count!. %%d
        echo !count!. %%d >> "%output_file%"
    )
)

echo.
if %count% equ 0 (
    echo finded "pycache" failed
    echo find "pycache" failed >> "%output_file%"
) else (
    echo Found a total of %count% items that contain "pycache" 
    echo save file: %output_file%
)

echo.
for /f "delims=" %%d in ('dir /s /b /ad ^| findstr /i "pycache"') do (
    echo delete: %%d
    rd /s /q "%%d"
)

echo deleted "pycache"  finished
echo "✅ The coverage environment has been thoroughly cleaned "

endlocal
pause   