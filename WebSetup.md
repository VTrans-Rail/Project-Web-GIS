Web Setup Steps
===============

The processing tasks are all automated, but I want to document the web setup steps.

###Setup Steps:
- Project Review Dashboard 
- Project Review Map 
- Project Creation Form 
- Project Status Update Form 

###Project Review Map
Starting from a new map:
1. Add [service](http://vtransmap01.aot.state.vt.us/arcgis/rest/services/Rail/PROJ_Review/FeatureServer) to the map
2. Rename features:  
  a. `~PROJ Review - ~Asset Projects`  
  b. `~PROJ Review - ~Track Projects`  
3. Add [Rail Lines](http://vtransmap01.aot.state.vt.us/arcgis/rest/services/Rail/Rail_Lines/MapServer)
4. Add [Rail Mile Posts](http://vtransmap01.aot.state.vt.us/arcgis/rest/services/Rail/Rail_MilePosts/MapServer)
5. Save Map (in folder `Projects`)
6. Tag `VTrans Rail`,`projects`
7. Share with `Organization`, `Program Managers` and `Rail Editors` groups.
8. Add Thumbnail   

![Thumbnail](https://raw.githubusercontent.com/VTrans-Rail/Project-Web-GIS/master/img/PROJ_Review.png)

###Project Creation Form
Starting from a new map:
1. Add [service](http://vtransmap01.aot.state.vt.us/arcgis/rest/services/Rail/PROJ_AddNew/FeatureServer) to the map
2. Rename feature `~PROJ AddNew - ~Add New Project`
3. Add `AssetID` [service](http://vtransmap01.aot.state.vt.us/arcgis/rest/services/Rail/AssetID/FeatureServer/0) to the map
4. Rename `~AssetID - ~Asset ID Schema`
5. Add Labels for `AssetID` field 
![Labels]()
6. Set visibility range to `1:144,448` or similar (too many features at full zoom)
7. Save Map (in folder `Projects`)
8. Share with `Organization`, `Program Managers` and `Rail Editors` groups.
8. Add Thumbnail   
![Thumbnail](https://raw.githubusercontent.com/VTrans-Rail/Project-Web-GIS/master/img/PROJ_Add.png)


###Project Status Update Form
_Steps_

![Thumbnail]()

###Project Review Dashboard
_Steps_

![Thumbnail]()
