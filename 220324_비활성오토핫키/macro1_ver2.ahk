f3::
loop
{
ControlSend, , {u}, �ٶ��� ����
Sleep 30
ControlSend, , {i}, �ٶ��� ����
Sleep 30
if Getkeystate("ESC")
break
}
return

f4::
ControlSend, , +{z}, �ٶ��� ����
ControlSend, , {A}, �ٶ��� ����
loop
{
ControlSend, , {1 Down}, �ٶ��� ����
if Getkeystate("ESC")
break
}
return