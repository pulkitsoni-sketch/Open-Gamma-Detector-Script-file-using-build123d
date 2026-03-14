# Open-Gamma-Detector-Script-file-using-build123d
My methodology was to import the original step file into Fusion360 using insert mesh option then going to modify tab and selecting convert mesh option, operation as base feature and method faceted I found out the dimensions of all the individual parts. Then the script file were made using these dimensions.
Time taken: 10 hours 


 Case Lower
  Volume error                                                      0.143%
  Sym-diff as % of original              0.396%


  Case Upper
  Volume error                                                      1.055%
  [ Symmetric Difference Error ]
  Skipped: Not all meshes are volumes (open shell)
  (open-shell meshes cannot be used for boolean ops)

  LCD Bezel
  Volume error                                                      0.002%
  Sym-diff as % of original              1.349

  Panel Cover
  Volume error                                                      0.000%
  Sym-diff as % of original              0.000%
  ──────────────────────────────────────────────────────────────
  ✓ PASS — All metrics within tolerance  (4/4 metrics pass)
