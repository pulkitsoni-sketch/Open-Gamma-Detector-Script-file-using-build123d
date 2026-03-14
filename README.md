# Open-Gamma-Detector-Script-file-using-build123d
My methodology was to import the original step file into Fusion360 using insert mesh option then going to modify tab and selecting convert mesh option, operation as base feature and method faceted I found out the dimensions of all the individual parts. Then the script file were made using these dimensions.
Time taken: 10 hours 

═════════════════════════════════════════════════════════════════
 Case Lower
═════════════════════════════════════════════════════════════════
  [ Volume Analysis ]
                                       ORIGINAL         REBUILT        DIFF
  ────────────────────────────────────────────────────────────────────────
  Volume (mm³)                         51975.99        51901.84     74.15
  Volume error                                                      0.143%

  [ Symmetric Difference Error ]
  Method                         exact boolean (manifold3d)
  Sym-diff volume (mm³)                 205.601
  Sym-diff as % of original              0.396%

═════════════════════════════════════════════════════════════════
  Case Upper
═════════════════════════════════════════════════════════════════

  [ Volume Analysis ]
                                       ORIGINAL         REBUILT        DIFF
  ────────────────────────────────────────────────────────────────────────
  Volume (mm³)                         94350.05        95345.66    995.61
  Volume error                                                      1.055%


  [ Symmetric Difference Error ]
  Skipped: Not all meshes are volumes (open shell)
  (open-shell meshes cannot be used for boolean ops)


═════════════════════════════════════════════════════════════════
  LCD Bezel
═════════════════════════════════════════════════════════════════

  [ Volume Analysis ]
                                       ORIGINAL         REBUILT        DIFF
  ────────────────────────────────────────────────────────────────────────
  Volume (mm³)                          4424.71         4424.78      0.07
  Volume error                                                      0.002%

  [ Symmetric Difference Error ]
  Method                         exact boolean (manifold3d)
  Sym-diff volume (mm³)                  59.684
  Sym-diff as % of original              1.349

═════════════════════════════════════════════════════════════════
  Panel Cover
═════════════════════════════════════════════════════════════════

  [ Volume Analysis ]
                                       ORIGINAL         REBUILT        DIFF
  ────────────────────────────────────────────────────────────────────────
  Volume (mm³)                          5313.28         5313.28      0.00
  Volume error                                                      0.000%

  [ Symmetric Difference Error ]
  Method                         exact boolean (manifold3d)
  Sym-diff volume (mm³)                   0.001
  Sym-diff as % of original              0.000%
  ✓  Symmetric diff error                0.000%
  ──────────────────────────────────────────────────────────────
  ✓ PASS — All metrics within tolerance  (4/4 metrics pass)
