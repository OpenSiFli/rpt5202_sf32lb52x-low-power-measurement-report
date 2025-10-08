# 🔋 SF32LB52x Low Power Test Report

Welcome to the SF32LB52x series chip low power test report!

::::{grid} 1 2 2 3
:gutter: 3

:::{grid-item-card} 📋 Chip Introduction
:link: brief_introduction
:link-type: doc

Introduction to the chip
:::

:::{grid-item-card} 🧪 Test Environment
:link: test_environment/index
:link-type: doc

Learn about the hardware environment, software configuration and testing tools required for testing
:::

:::{grid-item-card} 📡 BLE Low Power Test
:link: ble/index
:link-type: doc

Detailed test methods and results for Bluetooth Low Energy scenarios
:::

:::{grid-item-card} 🔵 BT Classic Bluetooth Test
:link: bt/index
:link-type: doc

Power consumption test data for classic Bluetooth application scenarios
:::

:::{grid-item-card} ⚡ Coremark Performance Test
:link: coremark/index
:link-type: doc

Power consumption performance analysis in benchmark performance testing
:::

::::

````{if-builder} html
```{toctree}
:maxdepth: 3
:hidden:

brief_introduction
test_environment/index
ble/index
bt/index
coremark/index
```
````

````{if-builder} simplepdf
```{toctree}
:maxdepth: 3
:hidden:
:numbered:

brief_introduction
test_environment/index
ble/index
bt/index
coremark/index
```
````
