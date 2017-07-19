'This script outputs to a .tsv file a list of applications installed on the computer
'Output file is software.tsv
'Usage: cscript applications.vbs

Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objTextFile = objFSO.CreateTextFile("C:\WINDOWS\system32\temp\software.tsv", True)

strComputer = "."
Set objWMIService = GetObject("winmgmts:" _
  & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colSoftware = objWMIService.ExecQuery _
  ("Select * from Win32_Product")

objTextFile.WriteLine "Caption" & vbtab & _
  "Description" & vbtab & "Identifying Number" & vbtab & _
  "Install Date" & vbtab & "Install Location" & vbtab & _
  "Install State" & vbtab & "Name" & vbtab & _ 
  "Package Cache" & vbtab & "SKU Number" & vbtab & "Vendor" & vbtab _
    & "Version" 

For Each objSoftware in colSoftware
  objTextFile.WriteLine objSoftware.Caption & vbtab & _
  objSoftware.Description & vbtab & _
  objSoftware.IdentifyingNumber & vbtab & _
  objSoftware.InstallDate2 & vbtab & _
  objSoftware.InstallLocation & vbtab & _
  objSoftware.InstallState & vbtab & _
  objSoftware.Name & vbtab & _
  objSoftware.PackageCache & vbtab & _
  objSoftware.SKUNumber & vbtab & _
  objSoftware.Vendor & vbtab & _
  objSoftware.Version
Next
objTextFile.Close

'This searches for a string of txt in a file

Dim FoundIt  'as boolean
FoundIt=false  'initialize it to false
With createobject("Scripting.FileSystemObject")
  on error resume next
  FoundIt = (InStr(1,.OpenTextFile("C:\WINDOWS\system32\temp\software.tsv",1,true,-2).ReadAll,"Microsoft .NET Framework 2.0",1) <> 0)
  on error goto 0
End With

'wscript.echo FoundIt

If FoundIt Then
  wscript.echo "true"
Else
  wscript.echo "false"
End If