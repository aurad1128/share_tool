Set FSO = CreateObject("Scripting.FileSystemObject")
Set WshShell = CreateObject("WScript.Shell")

ProjectDir = FSO.GetParentFolderName(WScript.ScriptFullName)

Set Env = WshShell.Environment("Process")
Env("QT_QPA_PLATFORM_PLUGIN_PATH") = ProjectDir & "\venv\Lib\site-packages\PyQt5\Qt5\plugins"

WshShell.Run """" & ProjectDir & "\venv\Scripts\python.exe"" """ & ProjectDir & "\src\main.py""", 1, False
