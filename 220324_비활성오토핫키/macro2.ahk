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
loop
{
PostMessage, 0X100, 55, 524289, Edit1, *test.txt - Windows �޸���
PostMessage, 0X100, 38, 21495809, Edit1, *test.txt - Windows �޸���
PostMessage, 0X100, 13, 1835009, Edit1, *test.txt - Windows �޸���
sleep 30
if Getkeystate("ESC")
break
}
return