f3::
loop
{
ControlSend, , {u}, 바람의 나라
Sleep 30
ControlSend, , {i}, 바람의 나라
Sleep 30
if Getkeystate("ESC")
break
}
return

f4::
loop
{
ControlSend, , {7}, 바람의 나라
send, {Up}
ControlSend, , {Enter}, 바람의 나라
sleep 30
if Getkeystate("ESC")
break
}
return