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
  a. <del>PROJ Review - </del> Asset Projects    
  b. <del>PROJ Review - </del> Track Projects  

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
2. Rename feature <del>~~PROJ AddNew - </del>Add New Project  
3. Add `AssetID` [service](http://vtransmap01.aot.state.vt.us/arcgis/rest/services/Rail/AssetID/FeatureServer/0) to the map  
4. Rename <del>AssetID - </del> Asset ID Schema`  
5. Add Labels for `AssetID` field   
![Labels]()
6. Set visibility range to `1:144,448` or similar (too many features at full zoom)
7. Save Map (in folder `Projects`)
8. Share with `Organization`  
9. Share as a `GeoForm application` called `Add Project Form`    

**Geoform Configuration Steps:**

1. Select Webmap  
2. Select `Add New Project` Layer  
3. Title: `Add New Project`
4. Logo Image ~[logo](https://raw.githubusercontent.com/VTrans-Rail/Project-Web-GIS/master/img/logo-med.png)
5. Add description

>Use this form to add a new project to the database. Please note that certain fields are required, notably AssetID and FromMP.
> More things may need to be added later.

6. Add `Required` as Help Text on the `ProjectName`, `ProjectType`, `RailLine`, `FromMP`, and `AssetID`  
7. Add `See Map Below` as Hint on the `AssetID` field  
8. Change `ProjectDescription` section input to `Textarea`  
9. Choose the `Superhero` theme.  
10. Uncheck `My Location` and `Latitude & Longitude Coordinates` options  
11. Hit save
12. Hit `Close` and then `View Application Item`  
13. Click `Edit` and then add the thumbnail    

![Thumbnail](https://raw.githubusercontent.com/VTrans-Rail/Project-Web-GIS/master/img/PROJ_Add.png)
14. Hit `Share` and then select `Rail Program Managers`


###Project Status Update Form
_Steps_

![Thumbnail]()

###Project Review Dashboard
_Steps_

![Thumbnail]()
