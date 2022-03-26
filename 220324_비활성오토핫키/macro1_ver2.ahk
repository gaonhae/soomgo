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
ControlSend, , +{z}, 바람의 나라
ControlSend, , {A}, 바람의 나라
loop
{
ControlSend, , {1 Down}, 바람의 나라
if Getkeystate("ESC")
break
}
return