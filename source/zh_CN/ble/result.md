# 测量结果汇总
表格中 ADV 与 Connection 的电流值为该模式的增量电流，Sleep 为睡眠电流，实际的平均电流等于增量电流与睡眠电流之和，例如 1 秒间隔的 ADV，4dBm 的发射功率，平均电流为 10.5+14.5=24.5uA

### BLE 功耗表

<table border="1" style="border-collapse: collapse; border: 1px solid black;">
<thead>
<tr>
<th style="border: 1px solid black; padding: 8px;">模式</th>
<th style="border: 1px solid black; padding: 8px;">条件</th>
<th style="border: 1px solid black; padding: 8px;">电源电压 3.3V<br/>@TXpower=0dBm</th>
<th style="border: 1px solid black; padding: 8px;">电源电压 3.3V<br/>@TXpower=4dBm</th>
<th style="border: 1px solid black; padding: 8px;">电源电压 3.3V<br/>@TXpower=10dBm</th>
<th style="border: 1px solid black; padding: 8px;">电源电压 3.3V<br/>@TXpower=13dBm</th>
<th style="border: 1px solid black; padding: 8px;">单位</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3" style="border: 1px solid black; padding: 8px; text-align: center; vertical-align: middle;"><strong>∆BLE ADV</strong></td>
<td style="border: 1px solid black; padding: 8px;">200ms</td>
<td style="border: 1px solid black; padding: 8px;">46</td>
<td style="border: 1px solid black; padding: 8px;">52.9</td>
<td style="border: 1px solid black; padding: 8px;">70.5</td>
<td style="border: 1px solid black; padding: 8px;">239.3</td>
<td style="border: 1px solid black; padding: 8px;">uA</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 8px;">500ms</td>
<td style="border: 1px solid black; padding: 8px;">18.4</td>
<td style="border: 1px solid black; padding: 8px;">20.8</td>
<td style="border: 1px solid black; padding: 8px;">29.8</td>
<td style="border: 1px solid black; padding: 8px;">103.5</td>
<td style="border: 1px solid black; padding: 8px;">uA</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 8px;">1s</td>
<td style="border: 1px solid black; padding: 8px;">8.9</td>
<td style="border: 1px solid black; padding: 8px;">10.5</td>
<td style="border: 1px solid black; padding: 8px;">14.6</td>
<td style="border: 1px solid black; padding: 8px;">53</td>
<td style="border: 1px solid black; padding: 8px;">uA</td>
</tr>
<tr>
<td rowspan="3" style="border: 1px solid black; padding: 8px; text-align: center; vertical-align: middle;"><strong>∆BLE Connection</strong></td>
<td style="border: 1px solid black; padding: 8px;">200ms</td>
<td style="border: 1px solid black; padding: 8px;">21</td>
<td style="border: 1px solid black; padding: 8px;">22</td>
<td style="border: 1px solid black; padding: 8px;">25.7</td>
<td style="border: 1px solid black; padding: 8px;">46.8</td>
<td style="border: 1px solid black; padding: 8px;">uA</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 8px;">500ms</td>
<td style="border: 1px solid black; padding: 8px;">9</td>
<td style="border: 1px solid black; padding: 8px;">9.3</td>
<td style="border: 1px solid black; padding: 8px;">10.9</td>
<td style="border: 1px solid black; padding: 8px;">19.3</td>
<td style="border: 1px solid black; padding: 8px;">uA</td>
</tr>
<tr>
<td style="border: 1px solid black; padding: 8px;">1s</td>
<td style="border: 1px solid black; padding: 8px;">5</td>
<td style="border: 1px solid black; padding: 8px;">5</td>
<td style="border: 1px solid black; padding: 8px;">6.1</td>
<td style="border: 1px solid black; padding: 8px;">10.3</td>
<td style="border: 1px solid black; padding: 8px;">uA</td>
</tr>
<tr>
<td style="padding: 8px; text-align: center;"><strong>Sleep</strong></td>
<td style="padding: 8px;"></td>
<td style="padding: 8px;">14.5</td>
<td style="padding: 8px;">14.5</td>
<td style="padding: 8px;">14.5</td>
<td style="padding: 8px;">14.5</td>
<td style="padding: 8px;">uA</td>
</tr>
</tbody>
</table>