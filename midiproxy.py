import argparse
import mido
mido.set_backend('mido.backends.rtmidi')

def proxy(device_name):
    proxy_input = mido.open_input('Proxy Input', virtual=True)
    proxy_output = mido.open_output('Proxy Output', virtual=True)
    target_input = mido.open_input(device_name)
    target_output = mido.open_output(device_name)

    while True:
        for txmsg in proxy_input.iter_pending():
            target_output.send(txmsg)
            print('=> ' + str(txmsg))

        for rxmsg in target_input.iter_pending():
            proxy_output.send(rxmsg)
            print('<= ' + str(rxmsg))

parser = argparse.ArgumentParser(description='Proxy MIDI connection')
parser.add_argument('target')

args = parser.parse_args()
proxy(args.target)
