Attribute VB_Name = "Mod_RodarPython"
Option Explicit

'https://www.youtube.com/watch?v=paEIQHI2KkY&list=PLmOO8X35BgB1rDGTZ1q4tzxCeK7RnFNqD&index=6&ab_channel=RonanVico

Sub ChamarPython()
    Dim CaminhoPythonExe        As String
    Dim CaminhoArquivoPython    As String

    Let CaminhoPythonExe = Environ$("USERPROFILE") & "\AppData\Local\Programs\Python\Python311\python.exe"
    'C:\Users\Windows\AppData\Local\Programs\Python\Python311
    Let CaminhoArquivoPython = ThisWorkbook.Path & "\MsgBox.py"

    Call VBA.Shell(CaminhoPythonExe & " " & CaminhoArquivoPython & " ""Mario"" ""Bros"" 3 ")

'    ## Styles:
'    ## 0 : OK
'    ## 1 : OK | Cancel
'    ## 2 : Abort | Retry | Ignore
'    ## 3 : Yes | No | Cancel
'    ## 4 : Yes | No
'    ## 5 : Retry | Cancel
'    ## 6 : Cancel | Try Again | Continue

    
End Sub
