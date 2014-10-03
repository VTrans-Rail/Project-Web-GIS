Web Setup Steps
===============

The processing tasks are all automated, but I want to document the web setup steps.

###Setup Steps:
- Project Review Dashboard 
- Project Review Map 
- Project Creation Form 
- Project Status Update Form 


###Project Creation Form

Starting from a new map:  

1. Add project creation [service](http://vtransmap01.aot.state.vt.us/arcgis/rest/services/Rail/PROJ_AddNew/FeatureServer) to the map  

2. Rename feature <del>PROJ AddNew - </del>Add New Project  

3. Add `AssetID` [service](http://vtransmap01.aot.state.vt.us/arcgis/rest/services/Rail/AssetID/FeatureServer/0) to the map  

4. Rename <del>AssetID - </del> Asset ID Schema  

5. Add Labels for `AssetID` field ![Labels](https://raw.githubusercontent.com/VTrans-Rail/Project-Web-GIS/master/img/Create Labels.png)  
  
6. Set visibility range to `1:144,448` or similar (too many features at full zoom)  
  
7. Save Map (in folder `Projects`)  
  
8. Share with `Organization`  
  
9. Share as a `GeoForm application` called `Add Project Form`    
  
**Geoform Configuration Steps:**  
  
1. Select Webmap  

2. Select `Add New Project` Layer  

3. Title: `Add New Project Form`

4. Set logo image ![logo](https://raw.githubusercontent.com/VTrans-Rail/Project-Web-GIS/master/img/logo-med.png)

5. Add description:

> Use this form to add a new project to the database. This is the same as adding a new row to your projects spreadsheet. Fill this out once you want the project to appear on the map. The information you provide here doesn't have to be complete right away, but please note that certain fields are required, notably Project Name, Project Type, AssetID, Rail Line, and FromMP. Later edits will be slightly difficult, so the more you can provide up front the easier you make your life.
> 
> After filling out all the fields, just click anywhere on the map at the bottom. It doesn't matter if it's right on top of the project or in the Sahara desert - I extract the data from the fields to locate the project and then disregard the location you click.
> 
> If anything needs to be added to the drop-down lists, please let Stephen know before you fill out the form.
> 
> Project Naming Convention: 
> 
> Project Town Name (Proper Case) + Project Number
> 
> Example:
> 
> Arlington STP 0114(4)
> 
> Barre City STP 0261(42)
  
6. Add `Required` as Help Text on the `ProjectName`, `ProjectType`, `RailLine`, `FromMP`, and `AssetID`  
  
Add the following hints: `Starting Mile Post` to `FromMP`, `Ending Mile Post` to `ToMP`,
  
Add `Optional` to all fields below `Project Description`

Add `Do you want this included in reports and the map?`
  
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
Build the Web Map

1. Add [service](http://vtransmap01.aot.state.vt.us/arcgis/rest/services/Rail/PROJ_StatusUpdate/FeatureServer) to the map

2. Rename <del>PROJ StatusUpdate - </del>Project Status Update

3. Save Map (in folder `Projects`)

4. Tag `VTrans Rail`,`projects`

5. Share with `Organization`

Geoform Configuration Steps:
  
1. Select Webmap  

2. Select `Project Status Update` Layer  

3. Title: `Project Status Update Form`

4. Logo Image ![logo](https://raw.githubusercontent.com/VTrans-Rail/Project-Web-GIS/master/img/logo-med.png)

5. Add description

> Please fill out this form whenever the status changes. Please note the required fields <em>Project Name</em>, <em>Project Manager</em>. Once filled out, click <em>anywhere</em> on the map (it doesn't matter where) and hit <em>Submit</em>.
> More things may need to be added later.

6. Add `Required` as Help Text on the

7. Change the `Status Update` and `Action Items` fields to `Textarea`

8. Select Theme `United`

9. Uncheck `Share Geoform`, `My Location`, and `Latitude & Longitude Coordinates`

10. Click `View Application Item`

11. Set the thumbnail

![Thumbnail](https://raw.githubusercontent.com/VTrans-Rail/Project-Web-GIS/master/img/PROJ_Status.png)

12. Share the map with the `Rail Editors` and `Rail Program Managers` groups.

###Project Review Map

Starting from a new map:  

1. Add [projects](http://vtransmap01.aot.state.vt.us/arcgis/rest/services/Rail/PROJ_Review/FeatureServer) and [status geometry](http://vtransmap01.aot.state.vt.us/arcgis/rest/services/Rail/PROJ_StatusGeometry/MapServer) services to the map  
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



###Project Review Dashboard

Build the Dashboard

1. In Operations Dashboard, start a `Multi-Operational View`

2. Choose the `Project Review` map

3. Check the boxes next to the `Asset Projects`, `Track Projects`, `Project Status Points`, and `Project Status Lines`

4. While `Asset Projects` and `Track Projects` are selected, check the box on the right that says `Selectable`

5. In the `Capabilities` tab, check Show Pop Up, Highlight, Pan to, Select, Zoom To, and Feature Pop-ups

6. Hit `OK`

7. Add a List widget for the `Asset Projects` data and title it `Latest Asset Projects` and have it sort by `created_date` descending. Enable the following feature actions: `Show pop-up, Highlight, Pan to, Select, Zoom to` and set the Doule click action to `Zoom to`. Dock this on the right.

8. Add a List widget for the `Track Projects` data and title it `Latest Track Projects` and have it sort by `created_date` descending. Enable the following feature actions: `Show pop-up, Highlight, Pan to, Select, Zoom to` and set the Doule click action to `Zoom to`. Dock this below the `Latest Asset Projects` list widget.

9. Add a List widget for the `Track Projects` data and title it `Latest Project Status Updates` and have it sort by `created_date` descending. Enable the following feature actions: `Show pop-up, Highlight, Pan to, Select, Zoom to` and set the Doule click action to `Zoom to`. Dock this below the `Latest Asset Projects` list widget.

![Thumbnail]()
