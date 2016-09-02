import mido

mido.set_backend('mido.backends.rtmidi')

proxy_input = mido.open_input('Proxy Input', virtual=True)
proxy_output = mido.open_output('Proxy Output', virtual=True)
target_input = mido.open_input(u'nanoKONTROL2 36:0')
target_output = mido.open_output(u'nanoKONTROL2 36:0')

while True:
    for txmsg in proxy_input.iter_pending():
        target_output.send(txmsg)
        print('=> ' + str(txmsg))

    for rxmsg in target_input.iter_pending():
        proxy_output.send(rxmsg)
        print('<= ' + str(rxmsg))
