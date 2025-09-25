# CoreMark
### HPSYS
1. * Open serial debugging tool, connect to HCPU console serial port, connect measurement device to the module under test
2. * Reset, after successful startup the log shown below appears in HCPU console

```{figure} assert/image4.png
:width: 60%
:align: center
```
3. * Send command run_coremark 192, instructing HCPU to execute CoreMark benchmark test at 192MHz frequency, measure average current C1 at this time. As shown below, phase 1 is the current waveform in WFI mode when HCPU runs at 192MHz main frequency. After starting CoreMark execution, it enters phase 2, current rises and maintains until test completion. Phase 3 is the current waveform returning to WFI mode.
![](assert/image5.png)
4. * Send command run_coremark 168, instructing HCPU to execute CoreMark benchmark test at 168MHz, measure average current C2 at this time, thus obtaining current increment per MHz as C=(C1-C2)/(192-168)
5. * Execute run_coremark 144 and run_coremark 120, measure average current at 144MHz and 120MHz, obtain incremental current at 144MHz as C=(C1-C2)/(144-120)
6. * Execute run_coremark 48 and run_coremark 24, measure average current at 48MHz and 24MHz, obtain incremental current at 48MHz as C=(C1-C2)/(48-24)
7. * Execute run_coremark 24 and run_coremark 12, measure average current at 24MHz and 12MHz, obtain incremental current at 24MHz as C=(C1-C2)/(24-12)

CoreMark execution time will be very long at frequencies like 48MHz/24MHz/12MHz. It's not necessary to wait for test completion. After measuring current values, you can reset to test the next item.

