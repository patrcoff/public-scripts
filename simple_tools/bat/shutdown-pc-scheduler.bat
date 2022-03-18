SCHTASKS /CREATE /SC WEEKLY /D TUE /TN "tuesday-restart-schedule" /TR "shutdown /r" /ST 17:19
SCHTASKS /CREATE /SC WEEKLY /D TUE /TN "tuesday-shutdown-schedule" /TR "shutdown /s /f /t 0" /ST 18:20
REM - restart then shutdown on tuesdays
SCHTASKS /CREATE /SC DAILY /TN "daily-shutdown-schedule" /TR "shutdown /s /f /t 60" /ST 17:21
REM - shutdown daily (1 minute after tuesday restart to ensure restart takes priority)