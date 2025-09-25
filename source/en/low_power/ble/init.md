# Device Initialization
When using the development board to test Bluetooth for the first time, the following initialization commands need to be executed after power-on (after programming the file system image, the Bluetooth address will be lost and needs to be reconfigured). Commands are executed in the HCPU console, and the wake-up PIN needs to be connected to low level to prevent HPSYS from entering low power mode, otherwise HCPU cannot process commands.
*  nvds reset_all 1
*  nvds update addr 6 <Bluetooth address>

For example: nvds update addr 6 1234567890C8. Note that the Bluetooth address format needs to be maintained in a certain format. It is recommended not to change C8, and users can change other parts. After command execution is completed, press the Reset key to restart the device.
