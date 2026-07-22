# Building and Flashing the Example
## Building
Navigate to the `example\pm\bt\project\hcpu` directory.

For the sf32lb52-core_n16r16 development board, build the example with the following command:

```
scons --board=sf32lb52-core_n16r16 -j8
```

For the sf32lb52-core_n4 development board, build the example with the following command:

```
scons --board=sf32lb52-core_n4 -j8
```

This generates the HCPU image file, which is stored in the `build` directory.

![](assert/image3.png)


## Flashing the Image
From the command-line directory where the project was built, run the following command to flash the generated image from the `build` directory. Make sure the board model is correct. If you are using an N4 board, change the board name accordingly.

```
build_sf32lb52-core_n16r16_hcpu\uart_download.bat
```

## Changing the Transmit Power
The project's default transmit power is 0 dBm. Use the `ble_tx_pwr_save x` command to change it, where `x` is the desired transmit power. For example, to set the transmit power to 10 dBm, run `ble_tx_pwr_save 10`. The board restarts automatically, and the new setting takes effect after the restart.
