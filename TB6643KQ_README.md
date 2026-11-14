# TB6643KQ KiCad library

- Symbol: `TB6643KQ.kicad_sym` (pins 1–7 per Toshiba datasheet).
- Footprint: `TB6643KQ.pretty/TB6643KQ_HSIP7_PCBHeatsink.kicad_mod`.
- Project library tables register both local libraries.

The footprint has a large front copper pad 8 beneath the rear metal plate, assigned as TAB_GND, to transfer heat into the PCB copper. Join pad 8 to GND in the schematic and use a large GND zone on both copper layers connected with thermal vias. Toshiba states the rear metal plate must be insulated or connected to ground. Confirm the actual package orientation and pad contact against the physical part before fabrication; the 7 lead holes are on 2.54 mm pitch with 1.0 mm drills.

Source: Toshiba TB6643KQ datasheet, package HSIP7-P-2.54A; pin functions and rear plate connection. https://toshiba.semicon-storage.com/info/docget.jsp?did=11271&prodName=TB6643KQ
