$NetAdapter = Get-WMIObject Win32_NetworkAdapter -filter "Ethernet adapter vEthernet (test switch)'"
$NetAdapter.Disable()
$NetAdapter.Enable()