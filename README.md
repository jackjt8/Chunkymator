Chunkymator
===========

A json generator for Chunky

Requirements: python 3.x, numpy, scipy, and a batch of jsons from Chunky.)

Usage
=====
Create a couple of scenes in chunky that are of the same map. Ensure you pad by one scene at the beginning and end as these segments are removed!

Only attributes of the camera are interpolated. Sky, Sun, Water, etc. are currently not interpolated but can easily be added; however I do not recommend interpolating many of these and instead recommend generating them independantly to ensure that there isn't any weird time ramping.
  
Once ready copy the scene .jsons into \Source\, open interpT.py, and append all the scenes to keyscenes followed by the time you wish for that scene to occur. ie keyscenes.append(['Skyrim0.json', -0.5]). Edit other settings with the #SET label.

Then run the script.

Either copy generated .jsons from \Output\ to a chosen Chunky Scenes folder. A copy of ChunkyLauncher.jar should let you rerun the setup in a different folder, be sure to select current working directory for Chunky to place a new Scenes folder (this should not interfer with your main install).

Then use any batch rendering script to render the .jsons.
```
