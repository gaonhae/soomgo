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
loop
{
ControlSend, , {7}, �ٶ��� ����
send, {Up}
ControlSend, , {Enter}, �ٶ��� ����
sleep 30
if Getkeystate("ESC")
break
}
return