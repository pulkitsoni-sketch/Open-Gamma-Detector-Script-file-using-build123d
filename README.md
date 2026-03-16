# Open-Gamma-Detector-Script-file-using-build123d
My methodology was to import the original step file into Fusion360 using insert mesh option then going to modify tab and selecting convert mesh option, operation as base feature and method faceted I found out the dimensions of all the individual parts. Then the script file were made using these dimensions.


**How Volumetric difference is calculated:** The script reads the raw triangles (mesh) directly from both STL files (original and rebuilt) and calculates the volumes of each mesh using Divergence theorem. It then simply subtracts one from the other.

**Divergence Theorem:**
V = 1/6 | n∑i=1 v1.(v2xv3) |
Where,
v1,v2,v3: 3 corner vertices of each triangle
X is cross product
. is dot product
n∑i=1, is sum over all n triangles in mesh

**How Symmetric difference is calculated:** Boolean operation are used via. trimesh and manifold3d,
Steps:
1) Both meshes are centre aligned by subtracting their bounding box midpoints
2) All 24 axis-aligned rotation (6 faces x 4 rotations about vertical axis (0,90,180,270 degrees) = 24) are generated to find best matching orientation btw the two meshes 
3) Once aligned it performs two boolean subtractions:
	3.1) B-A = material only in original
	3.2) A-B = material only in rebuilt
4 Add both leftover volumes together = total symmetric difference 

**Why it failed for Case_upper.stl**
The boolean operation in step 3 requires both meshes to be closed. It fails this because the inner cavity are cut all the down to Z = 0, which removes the bottom face entirely leaving the mesh open at the bottom like a box with no base  

**Time taken:** 10 hours 


** Case Lower**
  Volume error                                                      0.143%
  Sym-diff as % of original              0.396%


** Case Upper**
  Volume error                                                      1.055%
  [ Symmetric Difference Error ]
  Skipped: Not all meshes are volumes (open shell)
  (open-shell meshes cannot be used for boolean ops)

** LCD Bezel**
  Volume error                                                      0.002%
  Sym-diff as % of original              1.349

** Panel Cover**
  Volume error                                                      0.000%
  Sym-diff as % of original              0.000%
