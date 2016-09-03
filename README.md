# midiproxy
Proxies a MIDI connection for sniffing both sides of the communication

This program connects to the input and output of a target device, creates virtual input and output ports then relays messages between them. It also prints out the messages to stdout which is useful for reverse-engineering vendor-specific messages.

## Prerequisites

 * [Mido](https://github.com/olemb/mido/)
 * [python-rtmidi](https://pypi.python.org/pypi/python-rtmidi)

## Example usage

### Get a list of potential target devices:

    $ ./midiproxy -h
    usage: midiproxy [-h]
                     {KMidimon 129:0,Midi Through 14:0,RtMidiIn Client
                     130:0,RtMidiIn Client 132:0,nanoKONTROL2 36:0}
    
    Proxy MIDI connection
    
    positional arguments:
      {KMidimon 129:0,Midi Through 14:0,RtMidiIn Client 130:0,RtMidiIn Client 132:0,nanoKONTROL2 36:0}
                            Target device name
    
    optional arguments:
      -h, --help            show this help message and exit

### Run the proxy:

    $ ./midiproxy "nanoKONTROL2 36:0"
    
### Check the ports are up:

    $ aconnect -l
    [...]
    client 131: 'RtMidiIn Client' [type=user]
        0 'Proxy Input     '
    client 132: 'RtMidiOut Client' [type=user]
        0 'Proxy Output    '
    client 133: 'RtMidiIn Client' [type=user]
        0 'RtMidi Input    '
        Connected From: 36:0
    client 134: 'RtMidiOut Client' [type=user]
        0 'RtMidi Output   '
        Connecting To: 36:0[real:0]

### Connect an application to the proxy:

![Application port configuration](https://raw.githubusercontent.com/miek/midiproxy/master/img/app-ports.png)

### Log some messages:

    $ ./midiproxy "nanoKONTROL2 36:0"
    => F0 7E 7F 06 01 F7
    <= F0 7E 00 06 02 42 13 01 00 00 03 00 01 00 F7
    => F0 42 40 00 01 13 00 1F 12 00 F7
    <= F0 42 40 00 01 13 00 5F 42 00 F7

