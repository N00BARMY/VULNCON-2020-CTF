Using the same file from the previous chall, our objective now is to identify the ContainerID from theconnected USB Device. Basically, a ContainerID is likely an identifier for a physical device when loaded intoan Operating system. After several research, we found a Volatility plugin named ​usbstor​​that can be usedto extract all information from an usb device.

```
Commands Used: volatility --plugins=./volatility-plugins/ -f dump.raw --profile=Win7SP1x64 usbstor
```

