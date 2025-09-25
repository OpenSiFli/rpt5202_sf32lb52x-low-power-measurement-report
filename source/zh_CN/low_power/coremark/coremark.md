# CoreMark
### HPSYS
1. * 打开串口调试工具，连接 HCPU 的 console 串口，连接测量设备与被测模块
2. * 复位，启动成功后在 HCPU 的 console 中出现如下图的 log

```{figure} assert/image4.png
:width: 60%
:align: center
```
3. * 发送命令run_coremark 192，指示 HCPU 在 192MHz 频率下执行 CoreMark 基准测试，测量此时的平均电流 C1，如下图所示，阶段 1 是 HCPU 跑在 192MHz 主频时 WFI 模式下的电流波形，开始执行 CoreMark后进入阶段 2，电流上升并保持至测试结束，阶段 3 为回到 WFI 模式的电流波形
![](assert/image5.png)
4. * 发送命令run_coremark 168，指示 HCPU 在 168MHz 下执行 CoreMark 基准测试，测量此时的平均电流C2，由此得到每 MHz 的电流增量为C=(C1-C2)/(192-168)
5. * 执行run_coremark 144和run_coremark 120，测量 144MHz 和 120MHz 的平均电流，得到 144MHz 的增量电流 C=(C1-C2)/(144-120)
6. * 执行run_coremark 48和run_coremark 24，测量 48MHz 和 24MHz 的平均电流，得到 48MHz 的增量电流C=(C1-C2)/(48-24)
7. * 执行run_coremark 24和run_coremark 12，测量 24MHz 和 12MHz 的平均电流，得到 24MHz 的增量电流C=(C1-C2)/(24-12)

48MHz/24MHz/12MHz 等频率下 coremark 执行时间会很长，不必等待测试完成，测量得到电流值后可以复位测试下一项。

