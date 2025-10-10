#  SF32LB52x Chip Introduction

##  Chip Architecture Overview

**SF32LB52x** is an innovative dual-core architecture SoC chip based on **Arm Cortex-M33 STAR-MC1** processor.

:::::{grid} 1 2 2 2
:gutter: 3

::::{grid-item-card}  High Performance Core
:class-header: bg-primary text-white

**Maximum Operating Frequency**: 240MHz
^^^
Specifically designed for high-performance computing scenarios:
-  Graphics processing
-  Audio processing  
-  Neural network computation
::::

::::{grid-item-card}  Low Power Core (LCPU)
:class-header: bg-success text-white

**Maximum Operating Frequency**: 48MHz
^^^
Optimized for low power scenarios:
-  Bluetooth protocol stack Controller layer
-  Real-time task processing
-  Standby state management
::::

:::::



##  Test Content Overview

This document provides power consumption test methods and reference results for SF32LB52x series chips in various usage scenarios:

```{list-table} Test Scenario Overview
:header-rows: 1
:widths: 20 30 50

* - Category
  - Test Scenario
  - Description
* - **Wireless Communication**
  - BLE Bluetooth Low Energy
  - Typical scenarios such as advertising, connection, data transmission
* - **Wireless Communication**
  - BT Classic Bluetooth
  - Various application modes of traditional Bluetooth protocol
* - **Performance Test**
  - Coremark Benchmark Test
  - Power consumption performance in standardized CPU performance testing
* - **Basic Test**
  - While Loop
  - Power consumption baseline for basic loop operations
* - **Standby Mode**
  - Shutdown Mode
  - Power consumption data in the lowest power state
```

##  Important Notice

```{warning}
**Test results are for reference only**

The test results in this document are closely related to software and hardware environments, and differences may exist in actual applications.
```

###  Key Factors Affecting Power Consumption

:::::{grid} 1 2 2 3
:gutter: 3

::::{grid-item-card}  Chip Factors
- Individual differences of the chip itself
- Manufacturing process batch variations
::::

::::{grid-item-card}  Hardware Factors
- Selection and quality of peripheral components
- External inductor for chip built-in Buck
- PCB design and routing
::::

::::{grid-item-card}  Test Environment
- Accuracy and calibration of test equipment
- Power supply stability and ripple
- Environmental temperature and humidity conditions
::::

::::{grid-item-card}  Software Configuration
- Firmware version and compilation options
- I/O pin configuration status
- Clock and power management settings
::::

::::{grid-item-card}  Environmental Conditions
- Operating temperature range
- Electromagnetic interference level
- Power supply voltage fluctuation
::::

:::::


