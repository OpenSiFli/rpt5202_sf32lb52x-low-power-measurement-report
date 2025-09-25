# Measurement Results Summary
### Actually measured current as shown in figure:
The current values for Sniff mode and Scan in the table are incremental currents for those modes. Sleep is the sleep current. The actual average current equals the sum of incremental current and sleep current. For example, in Sniff mode, 500ms interval, attempt=4, 10dBm transmission power, average current is 23+16.6=39.6uA

### BT Power Consumption

| Mode | Condition | Power Supply Voltage 3.3V @TXpower=0dBm | Power Supply Voltage 3.3V @TXpower=4dBm | Power Supply Voltage 3.3V @TXpower=10dBm | Power Supply Voltage 3.3V @TXpower=13dBm | Unit |
|------|-----------|------------------------------------------|------------------------------------------|-------------------------------------------|-------------------------------------------|------|
| ∆BT Sniff Mode | 500ms (attempt=4) | 18.6 | 23.4 | 23 | 40.9 | uA |
| ∆Both Scan | Inquiry Scan and Page Scan | 52.6 | 52.6 | 52.6 | 52.6 | uA |
| Sleep | 16.6 | 16.6 | 16.6 | 16.6 | 16.6 | uA |
1. Scan receives 11.25ms every 1.28s, Both Scan receives 22.5ms every 1.28s.
2. bt 500ms sniff@TXpower10dBm: =23+16.6=39.6uA