f3::
loop
{
PostMessage, 0X100, 85, 1441793, Edit1, *test.txt - Windows �޸���
Sleep 30
PostMessage, 0X100, 73, 1507329, Edit1, *test.txt - Windows �޸���
Sleep 30
if Getkeystate("ESC")
break
}
return

f4::
ControlSend, Edit1, {shift}+{z}, *test.txt - Windows �޸���
ControlSend, Edit1, {A}, *test.txt - Windows �޸���
loop{
PostMessage, 0X100, 49, 131073, Edit1, *test.txt - Windows �޸���
Sleep 3
if Getkeystate("ESC")
break
}
return