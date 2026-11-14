# CTM1051AMG (ZLG)

KiCad symbol: `CTM1051AMG:CTM1051AMG`
Footprint: `CTM1051AMG:ZLG_CTM1051AMG_12.8x10.2mm_P2.54mm`

Source: [ZLG CTM1051(A)MG datasheet V1.03, 2025-02-20](https://www.zlg.cn/data/upload/power/CTM1051%28A%29MG.pdf), page 3 (mechanical drawing and pin table), page 1 (3.3 V supply).
Prepared for the ZLG part; other manufacturers using the same part number have not been checked.

| Pin | Signal | Symbol electrical type |
| --- | --- | --- |
| 1 | RXD | output |
| 2 | TXD | input |
| 3 | GND | power_in |
| 4 | VCC | power_in |
| 5 | CANG | power_out (isolated ground) |
| 6 | CANL | bidirectional |
| 7 | CANH | bidirectional |

VCC is 3.3 V nominal for CTM1051AMG. CANG is the isolated bus-side ground and is separate from logic GND.

## Mechanical layout

Top-side PCB view, with origin at pin 1. Do not mirror the manufacturer's bottom view directly into a top-side footprint.

```
        7    6    5       y = -7.62 mm
   1    2    3    4       y =  0.00 mm
 x=0  2.54 5.08 7.62 mm
```

- Body: 12.80 x 10.20 mm; height 7.70 mm (datasheet).
- Pin pitch: 2.54 mm; row spacing: 7.62 mm (datasheet).
- Drill: 1.00 mm plated through-hole (manufacturer's recommended PCB layout).
- Copper pad: 1.80 mm, square pin 1 and round others (library design choice).
- Fab body centered on the four-column/two-row grid, as depicted by the manufacturer. Equal body-to-pin margins are inferred from the drawing; the drawing does not separately dimension them.
- Lower-left chamfer identifies pin 1; 0.99 x 1.72 mm from the mechanical drawing.
- Courtyard extends at least 0.65 mm beyond the nominal body (library design choice).
- No pin 8 and no 3D model.

Validated with KiCad 10: symbol/footprint SVG export and visual review; pad coordinates/drills inspected using pcbnew; standalone footprint test board DRC reported 0 violations. These checks do not represent validation of a complete PCB layout.
