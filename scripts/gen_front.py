# -*- coding: utf-8 -*-
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "translated")
os.makedirs(OUT, exist_ok=True)

def write(n, title, html):
    path = os.path.join(OUT, f"p{n:03d}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"<!--TITLE:{title}-->\n{html.strip()}\n")

write(1, "หน้าปก", """
<p class="small">CF-4700 FFT Comparator</p>
<h3 style="margin-top:4px">คู่มืออ้างอิงการควบคุมภายนอก</h3>
<p class="small">External Control Reference Guide</p>
""")

write(2, "หน้าว่าง", """
<p class="small">(หน้านี้ไม่มีเนื้อหาในต้นฉบับ)</p>
""")

write(3, "บทนำ", """
<p>คู่มืออ้างอิงการควบคุมภายนอกฉบับนี้อธิบาย RS-232C interface และฟังก์ชัน LAN external control ของเครื่อง CF-4700 FFT Comparator รวมถึงอุปกรณ์ที่ต้องใช้ สภาพแวดล้อมการทำงาน และข้อจำกัดต่างๆ</p>
<div class="warning"><strong>สำคัญ:</strong> ต้องอ่านคู่มือนี้ก่อนใช้งาน RS-232C interface หรือฟังก์ชัน LAN external control ทุกครั้ง</div>
<div class="subhead"><span class="sq"></span>วิธีใช้คู่มือนี้</div>
<p>คู่มืออ้างอิงนี้ใช้สัญลักษณ์ต่อไปนี้นอกเหนือจากสัญลักษณ์ความปลอดภัยทั่วไป กรุณาทำความเข้าใจสัญลักษณ์เหล่านี้ก่อนอ่านคำแนะนำในคู่มือ</p>
<div class="note"><strong>⚠ CAUTION (ข้อควรระวัง)</strong> — คำอธิบายเพิ่มเติมหรือข้อจำกัด แนะนำให้อ่านข้อมูลที่ตามหลังสัญลักษณ์นี้</div>
<div class="warning"><strong>⚠ Important (สำคัญ)</strong> — คำแนะนำสำคัญที่ต้องปฏิบัติตาม ต้องอ่านคำแนะนำที่ตามหลังสัญลักษณ์นี้เสมอ</div>
<div class="note">
<ul>
<li>เนื้อหาของเอกสารฉบับนี้อาจเปลี่ยนแปลงได้ในรุ่นถัดไปโดยไม่แจ้งล่วงหน้า</li>
<li>ห้ามพิมพ์ซ้ำหรือทำซ้ำเนื้อหาส่วนใดของเอกสารนี้โดยไม่ได้รับอนุญาต</li>
<li>แม้จะจัดทำเอกสารนี้ด้วยความพยายามอย่างดีที่สุด หากพบจุดที่ไม่ชัดเจน ข้อผิดพลาด หรือข้อสงสัยใดๆ กรุณาแจ้งให้เราทราบ</li>
<li>เราไม่รับผิดชอบต่อผลลัพธ์จากการใช้งานของท่าน แม้จะมีข้อความข้างต้นก็ตาม</li>
<li>ชื่อบริษัทและชื่อผลิตภัณฑ์ทั้งหมดที่ใช้ในเอกสารนี้เป็นเครื่องหมายการค้าหรือเครื่องหมายการค้าจดทะเบียนของเจ้าของแต่ละราย</li>
<li>Ono Sokki Co., Ltd. ไม่รับผิดชอบต่อความเสียหายใดๆ อันเกิดจากการไม่ปฏิบัติตามคำแนะนำในคู่มือนี้ หรือความเสียหายจากการใช้งานที่ไม่ถูกต้อง</li>
</ul>
</div>
""")

write(4, "ข้อตกลงการใช้งานผลิตภัณฑ์และซอฟต์แวร์", """
<p>ข้อตกลงการใช้งาน (License Agreement) ฉบับนี้เป็นข้อตกลงเรื่องสิทธิ์การใช้งานผลิตภัณฑ์ (ซอฟต์แวร์) นี้ ระหว่างผู้ซื้อผลิตภัณฑ์ในฐานะผู้ใช้งานปลายทาง กับผู้ผลิต Ono Sokki Co., Ltd. กรุณาอ่านอย่างละเอียดเนื่องจากมีข้อมูลเรื่องการรับประกันและเงื่อนไขอื่นๆ</p>
<p>การใช้งานผลิตภัณฑ์นี้ถือว่าท่านยอมรับข้อกำหนดและเงื่อนไขของข้อตกลงนี้ หากไม่ยอมรับข้อใดข้อหนึ่ง ให้หยุดใช้งานทันทีและส่งคืนผลิตภัณฑ์ทั้งชุด (รวม CD-ROM คู่มือการใช้งาน และส่วนประกอบอื่นๆ) แก่ตัวแทนจำหน่ายที่ซื้อมาเพื่อขอรับเงินคืน</p>
<div class="subhead"><span class="sq"></span>ลิขสิทธิ์ (Copyright)</div>
<p>ลิขสิทธิ์ของซอฟต์แวร์ในผลิตภัณฑ์นี้เป็นของ Ono Sokki Co., Ltd. ท่านต้องปฏิบัติต่อผลิตภัณฑ์และซอฟต์แวร์นี้เช่นเดียวกับงานที่มีลิขสิทธิ์อื่นๆ (หนังสือ นิตยสาร ฯลฯ) ยกเว้นสามารถทำสำเนาซอฟต์แวร์ไว้เพื่อสำรองข้อมูลได้เท่านั้น ห้ามทำสำเนาเพื่อวัตถุประสงค์อื่นในทุกรูปแบบ รวมถึงห้ามทำสำเนาเอกสารที่มาพร้อมกับซอฟต์แวร์นี้</p>
<div class="subhead"><span class="sq"></span>ขอบเขตการรับประกันและความรับผิดชอบ</div>
<p>การรับประกันผลิตภัณฑ์นี้จำกัดระยะเวลา 1 ปีนับจากวันที่ซื้อ Ono Sokki Co., Ltd. ไม่รับประกันไม่ว่าโดยชัดแจ้งหรือโดยนัย ในเรื่องคุณภาพ ประสิทธิภาพ ความสามารถทางการตลาด หรือความเหมาะสมกับวัตถุประสงค์เฉพาะใดๆ ผลิตภัณฑ์จะออกสู่ตลาดตามสภาพที่เป็นอยู่ ท่านต้องรับผิดชอบต่อคุณภาพและประสิทธิภาพของซอฟต์แวร์นี้เอง</p>
<p>Ono Sokki Co., Ltd. ไม่รับผิดชอบต่อความเสียหายทางตรง ทางอ้อม ความเสียหายพิเศษ อุบัติเหตุ หรือความเสียหายต่อเนื่องอันเกิดจากความล้มเหลวของซอฟต์แวร์นี้ แม้จะได้รับแจ้งความเป็นไปได้ของความเสียหายดังกล่าวมาก่อนก็ตาม รวมถึงไม่รับผิดชอบต่อการเรียกร้องให้กู้คืนโปรแกรมหรือข้อมูลของผลิตภัณฑ์และซอฟต์แวร์นี้ หรือที่จัดเก็บ/ใช้งานในผลิตภัณฑ์ของ Ono Sokki รวมถึงค่าใช้จ่ายในการกู้คืนที่เกี่ยวข้อง ตัวแทนจำหน่ายหรือพนักงานขายผลิตภัณฑ์ของ Ono Sokki ไม่มีสิทธิ์แก้ไข ขยาย หรือเพิ่มเติมความรับผิดชอบเหล่านี้</p>
<div class="subhead"><span class="sq"></span>เงื่อนไขการรับประกัน</div>
<p class="small">เงื่อนไขการรับประกันด้านล่างนี้ไม่จำกัดสิทธิ์ตามกฎหมายของลูกค้า สอบถามรายละเอียดอุปกรณ์เสริมได้ที่สำนักงานขายหรือตัวแทนจำหน่าย Ono Sokki ใกล้บ้านท่าน</p>
<ol>
<li>ระยะเวลารับประกันผลิตภัณฑ์คือ 1 ปีนับจากวันที่ซื้อ</li>
<li>ซ่อมฟรีเฉพาะในช่วงระยะเวลารับประกัน กรณีที่ผลิตภัณฑ์ชำรุดจากการใช้งานตามคำเตือนในคู่มือนี้และฉลากบนตัวเครื่องเท่านั้น</li>
<li>หากผลิตภัณฑ์ชำรุดในช่วงรับประกันและต้องการซ่อมฟรี ให้ติดต่อสำนักงานขายหรือตัวแทนจำหน่าย Ono Sokki ใกล้บ้านท่าน</li>
<li>กรณีต่อไปนี้จะไม่ได้รับการซ่อมฟรีแม้อยู่ในช่วงรับประกัน:
  <ul>
    <li>ก) ชำรุดหรือเสียหายจากการใช้งานผิดวิธี การซ่อมแซม หรือดัดแปลงที่ไม่ถูกต้อง</li>
    <li>ข) ชำรุดหรือเสียหายจากแรงกระแทก การตกหล่น หรือการปะทะ</li>
    <li>ค) ชำรุดหรือเสียหายจากภัยธรรมชาติ เช่น ไฟไหม้ แผ่นดินไหว ฟ้าผ่า หรือความผิดปกติทางไฟฟ้า/สาธารณูปโภค</li>
  </ul>
</li>
<li>การซ่อมที่ต้องเดินทางไปยังเกาะห่างไกลหรือพื้นที่ทุรกันดารจะมีค่าใช้จ่ายในการเดินทางตามจริง</li>
</ol>
""")

write(5, "โครงสร้างเอกสารประกอบ", """
<p>เอกสารที่มาพร้อมกับเครื่อง CF-4700 FFT Comparator มีดังนี้:</p>
<div class="table-wrap"><table>
<thead><tr><th>ชื่อเอกสาร</th><th>รายละเอียด</th></tr></thead>
<tbody>
<tr><td><strong>User&rsquo;s Guide</strong><br><span class="small">(คู่มือผู้ใช้งาน)</span></td><td>มาพร้อมกับตัวเครื่อง CF-4700 อธิบายการใช้งานพื้นฐาน เช่น การเปิด/ปิดเครื่อง ชื่อและหน้าที่ของปุ่มควบคุม และสเปกฮาร์ดแวร์ รวมถึงฟังก์ชัน DF-0473 (fluctuation component extraction), CF-0477 (USB mass storage), CF-0478 (power backup)</td></tr>
<tr><td><strong>General Reference Guide</strong><br><span class="small">(คู่มืออ้างอิงทั่วไป)</span></td><td>อยู่ใน CD-ROM ที่มาพร้อมเครื่อง อธิบายภาพรวมซอฟต์แวร์ การใช้งานพื้นฐาน คำสั่งอ้างอิง และศัพท์เทคนิค ครอบคลุมการเตรียมเครื่องและการวัด (FFT analysis), ฟังก์ชัน CF-0471 (tracking), Comparator (block/shape), CF-0472 (shape comparator), DF-0473, CF-0477, CF-0478</td></tr>
<tr><td><strong>External Control Reference Guide</strong><br><span class="small">(คู่มือฉบับนี้)</span></td><td>อยู่ใน CD-ROM ที่มาพร้อมเครื่อง อธิบาย RS-232C interface และฟังก์ชัน LAN external control พร้อมตัวอย่างโปรแกรม คำสั่งอ้างอิง และศัพท์เทคนิคด้านการสื่อสาร</td></tr>
<tr><td><strong>Installation Manual</strong><br><span class="small">(คู่มือติดตั้ง)</span></td><td>อยู่ใน CD-ROM ที่มาพร้อมเครื่อง อธิบายวิธีอัปเกรดซอฟต์แวร์แอปพลิเคชันที่ติดตั้งในเครื่อง CF-4700</td></tr>
</tbody>
</table></div>
""")

write(6, "สารบัญ (1/3)", """
<p class="small">Chapter 1 — RS-232C Interface Reference Guide</p>
<div class="table-wrap"><table>
<tbody>
<tr><td class="tabular">1.</td><td>ภาพรวม RS-232C Interface</td><td class="tabular">8</td></tr>
<tr><td class="tabular">1.1</td><td class="small">RS-232C Interface</td><td class="tabular">8</td></tr>
<tr><td class="tabular">1.2</td><td class="small">ข้อกำหนด RS-232C Interface</td><td class="tabular">8</td></tr>
<tr><td class="tabular">1.3</td><td class="small">โครงสร้างการเชื่อมต่อ RS-232C</td><td class="tabular">10</td></tr>
<tr><td class="tabular">1.4</td><td class="small">การตั้งค่าเงื่อนไขการสื่อสาร RS-232C</td><td class="tabular">11</td></tr>
<tr><td class="tabular">2.</td><td>ภาพรวมคำสั่ง RS-232C</td><td class="tabular">12</td></tr>
<tr><td class="tabular">2.1</td><td class="small">ประเภทของคำสั่ง</td><td class="tabular">12</td></tr>
<tr><td class="tabular">2.2</td><td class="small">การส่งคำสั่ง</td><td class="tabular">12</td></tr>
<tr><td class="tabular">2.3</td><td class="small">ข้อควรระวังการส่งคำสั่งแบบชุด</td><td class="tabular">13</td></tr>
<tr><td class="tabular">2.4</td><td class="small">การใช้คำสั่ง LAN External Control ผ่าน RS-232C</td><td class="tabular">13</td></tr>
<tr><td class="tabular">3.</td><td>รายการคำสั่ง RS-232C</td><td class="tabular">14</td></tr>
<tr><td class="tabular">3.1</td><td class="small">คำสั่งตั้งค่า Input</td><td class="tabular">15</td></tr>
<tr><td class="tabular">3.2</td><td class="small">คำสั่งตั้งค่า Display</td><td class="tabular">18</td></tr>
<tr><td class="tabular">3.3</td><td class="small">คำสั่งควบคุมการวัด</td><td class="tabular">20</td></tr>
<tr><td class="tabular">3.4</td><td class="small">คำสั่ง Start/Stop</td><td class="tabular">20</td></tr>
<tr><td class="tabular">3.5</td><td class="small">คำสั่งตั้งค่า Environment</td><td class="tabular">20</td></tr>
<tr><td class="tabular">3.6</td><td class="small">คำสั่งตั้งค่า Analysis</td><td class="tabular">21</td></tr>
<tr><td class="tabular">3.7</td><td class="small">คำสั่งตั้งค่า Memory</td><td class="tabular">21</td></tr>
<tr><td class="tabular">3.8</td><td class="small">คำสั่ง Control Key</td><td class="tabular">22</td></tr>
<tr><td class="tabular">3.9</td><td class="small">คำสั่งตั้งค่า System</td><td class="tabular">23</td></tr>
<tr><td class="tabular">3.10</td><td class="small">คำสั่ง Comparator</td><td class="tabular">24</td></tr>
<tr><td class="tabular">3.11</td><td class="small">คำสั่ง RS-232C Interface</td><td class="tabular">31</td></tr>
</tbody>
</table></div>
""")

write(7, "สารบัญ (2/3)", """
<div class="table-wrap"><table>
<tbody>
<tr><td class="tabular">3.12</td><td class="small">คำสั่ง Input Amplifier</td><td class="tabular">32</td></tr>
<tr><td class="tabular">3.13</td><td class="small">คำสั่งฟังก์ชัน Trigger</td><td class="tabular">33</td></tr>
<tr><td class="tabular">3.14</td><td class="small">คำสั่งฟังก์ชัน Analysis</td><td class="tabular">36</td></tr>
<tr><td class="tabular">3.15</td><td class="small">คำสั่งกระบวนการ Averaging</td><td class="tabular">37</td></tr>
<tr><td class="tabular">3.16</td><td class="small">คำสั่งฟังก์ชัน Secondary Processing</td><td class="tabular">38</td></tr>
<tr><td class="tabular">3.17</td><td class="small">คำสั่งฟังก์ชัน Display</td><td class="tabular">39</td></tr>
<tr><td class="tabular">3.18</td><td class="small">คำสั่ง List Display</td><td class="tabular">43</td></tr>
<tr><td class="tabular">3.19</td><td class="small">คำสั่งฟังก์ชัน Search</td><td class="tabular">44</td></tr>
<tr><td class="tabular">3.20</td><td class="small">คำสั่งฟังก์ชันเกี่ยวกับหน่วย (Unit)</td><td class="tabular">46</td></tr>
<tr><td class="tabular">3.21</td><td class="small">คำสั่ง Panel Condition Memory</td><td class="tabular">47</td></tr>
<tr><td class="tabular">3.22</td><td class="small">คำสั่ง Data Memory</td><td class="tabular">48</td></tr>
<tr><td class="tabular">3.23</td><td class="small">คำสั่งควบคุม Analysis</td><td class="tabular">50</td></tr>
<tr><td class="tabular">3.24</td><td class="small">คำสั่งอื่นๆ</td><td class="tabular">51</td></tr>
<tr><td class="tabular">3.25</td><td class="small">คำสั่ง Data Transfer</td><td class="tabular">51</td></tr>
<tr><td class="tabular">3.26</td><td class="small">คำสั่ง Inspection</td><td class="tabular">53</td></tr>
<tr><td class="tabular">4.</td><td>ความเข้ากันได้กับ CF-4500</td><td class="tabular">54</td></tr>
<tr><td class="tabular">4.1</td><td class="small">ความแตกต่างของช่วงแรงดัน (Voltage Range)</td><td class="tabular">54</td></tr>
<tr><td class="tabular">4.2</td><td class="small">คำสั่งที่เปลี่ยนแปลง</td><td class="tabular">58</td></tr>
</tbody>
</table></div>
<p class="small">Chapter 2 — LAN External Control Reference Guide</p>
<div class="table-wrap"><table>
<tbody>
<tr><td class="tabular">1.</td><td>ภาพรวมฟังก์ชัน LAN External Control</td><td class="tabular">60</td></tr>
<tr><td class="tabular">1.1</td><td class="small">ฟังก์ชัน LAN External Control ของ CF-4700</td><td class="tabular">60</td></tr>
<tr><td class="tabular">1.2</td><td class="small">เงื่อนไขสภาพแวดล้อมของฟังก์ชัน LAN External Control</td><td class="tabular">60</td></tr>
<tr><td class="tabular">1.3</td><td class="small">โครงสร้างการควบคุมภายนอก</td><td class="tabular">61</td></tr>
<tr><td class="tabular">1.4</td><td class="small">ขั้นตอนการทำงานพื้นฐานของฟังก์ชัน LAN External Control</td><td class="tabular">62</td></tr>
<tr><td class="tabular">2.</td><td>การเตรียมการใช้งานฟังก์ชัน LAN External Control</td><td class="tabular">63</td></tr>
<tr><td class="tabular">2.1</td><td class="small">การติดตั้ง Client Software</td><td class="tabular">63</td></tr>
</tbody>
</table></div>
""")

write(8, "สารบัญ (3/3)", """
<div class="table-wrap"><table>
<tbody>
<tr><td class="tabular">2.2</td><td class="small">การตั้งค่าเงื่อนไขเครือข่ายและการยืนยันการเชื่อมต่อ</td><td class="tabular">64</td></tr>
<tr><td class="tabular">2.3</td><td class="small">การสร้างโปรแกรมควบคุม</td><td class="tabular">68</td></tr>
<tr><td class="tabular">3.</td><td>รายการคำสั่งอ้างอิง (Command Reference)</td><td class="tabular">74</td></tr>
<tr><td class="tabular">3.1</td><td class="small">CF9000Controller Class</td><td class="tabular">74</td></tr>
<tr><td class="tabular">3.2</td><td class="small">ตารางเทียบคำสั่งกับ Setting Key ของ CF-4700</td><td class="tabular">78</td></tr>
<tr><td class="tabular">3.3</td><td class="small">ตารางเทียบคำสั่งกับ Dialog Box ของ CF-4700</td><td class="tabular">93</td></tr>
<tr><td class="tabular">3.4</td><td class="small">ตารางเทียบคำสั่ง Graph</td><td class="tabular">111</td></tr>
<tr><td class="tabular">3.5</td><td class="small">ตารางเทียบ Control Key</td><td class="tabular">113</td></tr>
<tr><td class="tabular">3.6</td><td class="small">ตารางเทียบคำสั่งอ่านสถานะ (Condition Acquisition)</td><td class="tabular">114</td></tr>
<tr><td class="tabular">3.7</td><td class="small">ตารางเทียบคำสั่งฟังก์ชันสำรองไฟ (Power Supply Backup)</td><td class="tabular">115</td></tr>
<tr><td class="tabular">4.</td><td>ภาคผนวก (Reference)</td><td class="tabular">116</td></tr>
<tr><td class="tabular">4.1</td><td class="small">ศัพท์เครือข่าย (Network Terms)</td><td class="tabular">116</td></tr>
</tbody>
</table></div>
""")

write(9, "Chapter 1 — คู่มืออ้างอิง RS-232C Interface", """
<p class="small">RS-232C Interface Reference Guide</p>
<div class="table-wrap"><table>
<tbody>
<tr><td class="tabular">1.</td><td>ภาพรวม RS-232C Interface</td><td class="tabular">8</td></tr>
<tr><td class="tabular">2.</td><td>ภาพรวมคำสั่ง RS-232C</td><td class="tabular">12</td></tr>
<tr><td class="tabular">3.</td><td>รายการคำสั่ง RS-232C</td><td class="tabular">14</td></tr>
<tr><td class="tabular">4.</td><td>ความเข้ากันได้กับ CF-4500</td><td class="tabular">54</td></tr>
</tbody>
</table></div>
""")

write(10, "1. ภาพรวม RS-232C Interface", """
<p>เนื้อหาส่วนนี้อธิบายภาพรวมของ RS-232C interface อุปกรณ์ที่ต้องใช้ สภาพแวดล้อมการทำงาน และข้อจำกัดต่างๆ</p>
<div class="subhead"><span class="sq"></span>1.1 RS-232C Interface</div>
<p>RS-232C interface ช่วยให้ผู้ใช้งานสามารถควบคุมเครื่อง CF-4700 FFT Comparator ผ่านทาง PC ของลูกค้าได้</p>
<div class="subhead"><span class="sq"></span>1.2 ข้อกำหนดของ RS-232C Interface</div>
<div class="subhead" style="margin-left:14px"><span class="sq"></span>ตำแหน่งขา (Pin Arrangement)</div>
<figure class="figure"><img src="__IMG_PIN__" alt="RS-232C pin arrangement"><figcaption>ต้นฉบับใช้ font สัญลักษณ์วาดรูป จึงแสดงเป็นรูปภาพแทนการแปลงเป็นข้อความ</figcaption></figure>
""")

write(11, "1.2 ข้อกำหนด RS-232C Interface (ต่อ)", """
<div class="subhead"><span class="sq"></span>ข้อกำหนดการสื่อสาร (Communication Specification)</div>
<div class="table-wrap"><table>
<tbody>
<tr><td><strong>ความยาวตัวอักษร (Character length)</strong></td><td class="tabular">7 / 8 บิต</td></tr>
<tr><td><strong>การตรวจสอบพาริตี (Parity check)</strong></td><td>NONE / ODD / EVEN</td></tr>
<tr><td><strong>ความยาว Stop bit</strong></td><td class="tabular">1 / 2 บิต</td></tr>
<tr><td><strong>การควบคุมการไหลของข้อมูล (Xon/Xoff)</strong></td><td>ไม่มี, X ON/OFF, Hardware</td></tr>
<tr><td><strong>อักขระปิดท้ายคำสั่ง (Terminator)</strong></td><td><span class="code">CR</span> หรือ <span class="code">CR+LF</span></td></tr>
<tr><td><strong>โหมดการสื่อสาร</strong></td><td>Asynchronous Full-duplex</td></tr>
<tr><td><strong>อัตราเร็วในการส่งข้อมูล</strong></td><td class="tabular">1200 / 2400 / 4800 / 9600 / 19200 / 38400 / 57600 / 115200 bps</td></tr>
<tr><td><strong>สายเชื่อมต่อ</strong></td><td>Cross cable (9-pin female &ndash; 9-pin male)</td></tr>
</tbody>
</table></div>
<div class="subhead"><span class="sq"></span>ค่าเริ่มต้นจากโรงงาน (Default Setting)</div>
<div class="table-wrap"><table>
<tbody>
<tr><td><strong>ความยาวตัวอักษร</strong></td><td class="tabular">8 บิต</td></tr>
<tr><td><strong>การตรวจสอบพาริตี</strong></td><td>None</td></tr>
<tr><td><strong>ความยาว Stop bit</strong></td><td class="tabular">1 บิต</td></tr>
<tr><td><strong>Terminator</strong></td><td><span class="code">CR</span></td></tr>
<tr><td><strong>อัตราเร็วในการส่งข้อมูล</strong></td><td class="tabular">9600 bps</td></tr>
</tbody>
</table></div>
<div class="subhead"><span class="sq"></span>รายละเอียดขาสัญญาณ (Connector Specifications)</div>
<div class="table-wrap"><table>
<thead><tr><th>Pin</th><th>สัญญาณ</th><th>หน้าที่</th><th>ทิศทาง</th></tr></thead>
<tbody>
<tr><td class="tabular">1</td><td>&mdash;</td><td>ไม่ได้ต่อใช้งาน</td><td>&mdash;</td></tr>
<tr><td class="tabular">2</td><td><span class="code">RXD</span></td><td>รับข้อมูล</td><td>Input</td></tr>
<tr><td class="tabular">3</td><td><span class="code">TXD</span></td><td>ส่งข้อมูล</td><td>Output</td></tr>
<tr><td class="tabular">4</td><td>&mdash;</td><td>ไม่ได้ต่อใช้งาน</td><td>&mdash;</td></tr>
<tr><td class="tabular">5</td><td><span class="code">GND</span></td><td>กราวด์สัญญาณ</td><td>&mdash;</td></tr>
<tr><td class="tabular">6</td><td>&mdash;</td><td>ไม่ได้ต่อใช้งาน</td><td>&mdash;</td></tr>
<tr><td class="tabular">7</td><td><span class="code">RTS</span></td><td>ขอส่งข้อมูล</td><td>Output</td></tr>
<tr><td class="tabular">8</td><td><span class="code">CTS</span></td><td>พร้อมรับการส่ง</td><td>Input</td></tr>
<tr><td class="tabular">9</td><td>&mdash;</td><td>ไม่ได้ต่อใช้งาน</td><td>&mdash;</td></tr>
</tbody>
</table></div>
""")

write(12, "1.3 โครงสร้างการเชื่อมต่อ RS-232C", """
<p>เชื่อมต่อ Client PC เข้ากับพอร์ต RS-232C ของเครื่อง CF-4700 FFT Comparator ด้วย Cross cable (9-pin female &ndash; 9-pin male)</p>
<div class="figure"><p class="small" style="margin:0">Client PC &nbsp;&#8660;&nbsp; Cross cable (9-pin female &ndash; 9-pin male) &nbsp;&#8660;&nbsp; RS-232C port &nbsp;&#8660;&nbsp; CF-4700 FFT Comparator</p></div>
<div class="warning"><strong>ข้อควรระวัง:</strong>
<ul>
<li>หากต้องการรายละเอียดการต่อระบบโดยใช้ RS-232C interface เพิ่มเติม ติดต่อสำนักงานขายหรือตัวแทนจำหน่าย Ono Sokki ใกล้บ้านท่าน</li>
<li>ดูหัวข้อ 1.4 &ldquo;การตั้งค่าเงื่อนไขการสื่อสาร RS-232C&rdquo; และตั้งค่าเงื่อนไขการสื่อสาร RS-232C ก่อนเชื่อมต่อ Client PC เข้ากับเครื่อง CF-4700 FFT Comparator ผ่าน RS-232C เสมอ</li>
</ul>
</div>
""")

write(13, "1.4 การตั้งค่าเงื่อนไขการสื่อสาร RS-232C", """
<p>แตะปุ่มซอฟต์คีย์ตามลำดับต่อไปนี้เพื่อเปิดหน้าต่างตั้งค่า RS-232C สำหรับกำหนดเงื่อนไขการสื่อสาร RS-232C:</p>
<p style="font-size:16px"><span class="code">Home</span> &rarr; <span class="code">Ext Control</span> &rarr; <span class="code">RS-232C</span></p>
<p class="small">(เมนู Ext Control มีปุ่มย่อย DI / DO / RS-232C)</p>
<p class="small">ดูรายละเอียดเพิ่มเติมได้ที่ General Reference Guide (PDF Help) ใน CD-ROM ที่มาพร้อมเครื่อง CF-4700 FFT Comparator</p>
""")

write(14, "2. ภาพรวมคำสั่ง RS-232C", """
<div class="subhead"><span class="sq"></span>2.1 ประเภทของคำสั่ง (Command Types)</div>
<p>คำสั่งของ RS-232C interface บนเครื่อง CF-4700 FFT Comparator แบ่งเป็น 4 ประเภทดังนี้ (badge สีนี้จะกำกับทุกคำสั่งตลอดทั้งเล่ม):</p>
<div class="type-legend">
<div class="type-legend-item"><span class="type-badge type-1"><span class="dot"></span>Type 1 &middot; Execute</span><p>ส่งคำสั่ง 3 ตัวอักษรแล้วจบทันที ไม่มีพารามิเตอร์</p></div>
<div class="type-legend-item"><span class="type-badge type-2"><span class="dot"></span>Type 2 &middot; Set</span><p>คำสั่ง 3 ตัวอักษร ตามด้วยพารามิเตอร์ที่จำเป็น</p></div>
<div class="type-legend-item"><span class="type-badge type-3"><span class="dot"></span>Type 3 &middot; Get</span><p>ส่งคำสั่ง 3 ตัวอักษรแล้วอ่านค่ากลับ (ข้อความ)</p></div>
<div class="type-legend-item"><span class="type-badge type-4"><span class="dot"></span>Type 4 &middot; Get Binary</span><p>ส่งคำสั่ง 3 ตัวอักษรแล้วอ่านค่ากลับ (ไบนารี)</p></div>
</div>
<div class="subhead"><span class="sq"></span>2.2 การส่งคำสั่ง</div>
<p>คำสั่งแต่ละคำสั่งส่งพร้อม terminator เสมอ คำสั่ง Type 1 และ Type 2 สามารถส่งรวมกันเป็นชุด (batch) ได้ ตัวอย่างเช่น ตั้งค่า Averaging Mode เป็น Power Spectrum Arithmetic Mean, ตั้งจำนวนการเฉลี่ยเป็น 16 ครั้ง แล้วเริ่ม Average:</p>
<div class="cmd-group">
<div class="cmd-card"><div class="cmd-head"><span class="cmd-code">AMS2</span><span class="type-badge type-2"><span class="dot"></span>Type 2</span><span class="cmd-desc">ตั้งค่า Averaging Mode เป็น Power Spectrum Arithmetic Mean</span></div></div>
<div class="cmd-card"><div class="cmd-head"><span class="cmd-code">AND16</span><span class="type-badge type-2"><span class="dot"></span>Type 2</span><span class="cmd-desc">ตั้งจำนวนครั้งของการเฉลี่ย (Averaging) เป็น 16</span></div></div>
<div class="cmd-card"><div class="cmd-head"><span class="cmd-code">AST</span><span class="type-badge type-1"><span class="dot"></span>Type 1</span><span class="cmd-desc">เริ่มการเฉลี่ย (Average Start)</span></div></div>
</div>
<p>ตัวอย่างการส่งคำสั่งทั้งสามรวมกัน:</p>
<div class="codeblock">AMS2AND16AST<span class="cm"> + terminator</span></div>
<div class="warning"><strong>ข้อควรระวัง:</strong> ห้ามใส่ช่องว่างระหว่างคำสั่งกับค่าตัวเลข (เช่น <span class="code">AMS2</span>, <span class="code">AMS2AND16AST</span>) มิฉะนั้นคำสั่งจะถูกปฏิเสธ เมื่อส่งคำสั่งเป็นชุด สามารถแนบคำสั่ง Type 3 ต่อท้ายชุดคำสั่งได้ หากตรวจพบข้อผิดพลาดหรือคำสั่ง/พารามิเตอร์ที่ไม่ถูกต้อง การทำงานจะหยุดที่จุดนั้นทันทีและกลับสู่สถานะรอรับคำสั่ง</div>
<p class="small">คำสั่งในคู่มือนี้เขียนด้วยตัวพิมพ์ใหญ่ แต่ตัวพิมพ์เล็กจะถูกแปลงเป็นตัวพิมพ์ใหญ่โดยอัตโนมัติและตรวจจับเป็นคำสั่งได้เช่นกัน</p>
""")

write(15, "2.3–2.4 ข้อควรระวัง / คำสั่ง LAN ผ่าน RS-232C", """
<div class="subhead"><span class="sq"></span>2.3 ข้อควรระวังการส่งคำสั่งแบบชุด</div>
<p>เมื่อส่งคำสั่งต่อเนื่องกัน การประมวลผลคำสั่งภายในเครื่อง CF-4700 FFT Comparator อาจทำงานตามไม่ทัน เพื่อป้องกันปัญหานี้ เครื่องมี buffer รับข้อมูลชั่วคราวขนาด 1024 ไบต์ สำหรับรองรับข้อมูลที่รับเข้ามาต่อเนื่อง</p>
<div class="warning"><strong>ข้อควรระวัง:</strong> หากส่งคำสั่งเป็นชุดต่อเนื่องกันมากเกินไป อาจเกินขนาด buffer และคำสั่งจะไม่ถูกประมวลผล ควรใส่เวลาหน่วง (standby time) ระหว่างคำสั่งตามความจำเป็นเมื่อส่งคำสั่งหลายชุดต่อเนื่องกัน</div>
<div class="subhead"><span class="sq"></span>2.4 การใช้คำสั่ง LAN External Control ผ่าน RS-232C</div>
<p>สามารถใช้คำสั่ง LAN External Control ผ่านทาง RS-232C interface ได้ โดยเติมตัวอักษร <span class="code">LAN</span> และจำนวนค่าตัวเลขที่คำสั่งนั้นต้องการไว้หน้าคำสั่ง</p>
<div class="subhead" style="margin-left:14px"><span class="sq"></span>ตัวอย่างคำสั่ง LAN External Control ผ่าน RS-232C</div>
<div class="cmd-group">
<div class="cmd-card"><div class="cmd-head"><span class="cmd-desc"><strong>ไม่มีค่าตัวเลข</strong> &mdash; เริ่มการวัด (Start)</span></div><div class="cmd-args"><div class="lbl">คำสั่ง</div><div class="val"><span class="code">LAN0,DoStart</span></div></div></div>
<div class="cmd-card"><div class="cmd-head"><span class="cmd-desc"><strong>ค่าตัวเลข 1 ค่า</strong> &mdash; ตั้งจำนวนตัวอย่างเป็น 1024</span></div><div class="cmd-args"><div class="lbl">คำสั่ง</div><div class="val"><span class="code">LAN1,SetSampleFrameFlag,4</span></div></div></div>
<div class="cmd-card"><div class="cmd-head"><span class="cmd-desc"><strong>ค่าตัวเลข 2 ค่า</strong> &mdash; ตั้งค่าอ้างอิง 0-dB เป็น 2.0E-5</span></div><div class="cmd-args"><div class="lbl">คำสั่ง</div><div class="val"><span class="code">LAN2,SetEUYCalibrationValue,0,2.0E-5</span></div></div></div>
</div>
""")

write(16, "3. รายการคำสั่ง RS-232C (สารบัญหมวดคำสั่ง)", """
<p>รายการหมวดคำสั่ง RS-232C ทั้งหมด 26 หมวด พร้อมเลขหน้าอ้างอิงในต้นฉบับ:</p>
<div class="table-wrap"><table>
<thead><tr><th>หมวดคำสั่ง</th><th>หน้าอ้างอิง</th></tr></thead>
<tbody>
<tr><td>3.1 คำสั่งตั้งค่า Input</td><td class="tabular">15</td></tr>
<tr><td>3.2 คำสั่งตั้งค่า Display</td><td class="tabular">18</td></tr>
<tr><td>3.3 คำสั่งควบคุมการวัด</td><td class="tabular">20</td></tr>
<tr><td>3.4 คำสั่ง Start/Stop</td><td class="tabular">20</td></tr>
<tr><td>3.5 คำสั่งตั้งค่า Environment</td><td class="tabular">20</td></tr>
<tr><td>3.6 คำสั่งตั้งค่า Analysis</td><td class="tabular">21</td></tr>
<tr><td>3.7 คำสั่งตั้งค่า Memory</td><td class="tabular">21</td></tr>
<tr><td>3.8 คำสั่ง Control Key</td><td class="tabular">22</td></tr>
<tr><td>3.9 คำสั่งตั้งค่า System</td><td class="tabular">23</td></tr>
<tr><td>3.10 คำสั่ง Comparator</td><td class="tabular">24</td></tr>
<tr><td>3.11 คำสั่ง RS-232C Interface</td><td class="tabular">31</td></tr>
<tr><td>3.12 คำสั่ง Input Amplifier</td><td class="tabular">32</td></tr>
<tr><td>3.13 คำสั่งฟังก์ชัน Trigger</td><td class="tabular">33</td></tr>
<tr><td>3.14 คำสั่งฟังก์ชัน Analysis</td><td class="tabular">36</td></tr>
<tr><td>3.15 คำสั่งกระบวนการ Averaging</td><td class="tabular">37</td></tr>
<tr><td>3.16 คำสั่งฟังก์ชัน Secondary Processing</td><td class="tabular">38</td></tr>
<tr><td>3.17 คำสั่งฟังก์ชัน Display</td><td class="tabular">39</td></tr>
<tr><td>3.18 คำสั่ง List Display</td><td class="tabular">43</td></tr>
<tr><td>3.19 คำสั่งฟังก์ชัน Search</td><td class="tabular">44</td></tr>
<tr><td>3.20 คำสั่งฟังก์ชันเกี่ยวกับหน่วย (Unit)</td><td class="tabular">46</td></tr>
<tr><td>3.21 คำสั่ง Panel Condition Memory</td><td class="tabular">47</td></tr>
<tr><td>3.22 คำสั่ง Data Memory</td><td class="tabular">48</td></tr>
<tr><td>3.23 คำสั่งควบคุม Analysis</td><td class="tabular">50</td></tr>
<tr><td>3.24 คำสั่งอื่นๆ</td><td class="tabular">51</td></tr>
<tr><td>3.25 คำสั่ง Data Transfer</td><td class="tabular">51</td></tr>
<tr><td>3.26 คำสั่ง Inspection</td><td class="tabular">53</td></tr>
</tbody>
</table></div>
""")

print("wrote pages 1-16")
